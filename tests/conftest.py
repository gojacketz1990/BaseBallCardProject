import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests on (chrome, firefox, safari)"
    )
    parser.addoption(
        "--environment_name", action="store", default="QA", help="Environment to test against (QA, UAT)"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

@pytest.fixture(scope="function")
def setup_and_teardown(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    environment_name = request.config.getoption("environment_name")
    headless = request.config.getoption("--headless")

    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name.lower() == "safari":
        if headless:
            raise ValueError("Safari does not support headless mode.")
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Browser '{browser_name}' is not supported!")

    if environment_name == "QA":
        driver.get("http://localhost:3000/")
    elif environment_name == "UAT":
        driver.get("http://localhost:3000/")
    else:
        raise ValueError(f"Environment '{environment_name}' is not supported!")

    driver.maximize_window()
    request.cls.driver = driver
    request.node.driver = driver  # Attach driver to request node

    yield driver  # Yield driver for test functions
    driver.quit()

def pytest_html_results_table_header(cells):
    """Modify the report table to include a 'Description' column."""
    cells.insert(2, "<th>Description</th>")

def pytest_html_results_table_row(report, cells):
    """Insert the test case description into the report."""
    description = dict(report.user_properties).get("description", "Not a description provided")
    cells.insert(2, f"<td>{description}</td>")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)

def pytest_runtest_makereport(item, call):
    """Hook to add the description from CSV into the test report."""
    outcome = yield
    report = outcome.get_result()

    # Default description if not found
    description = "No description provided"

    # Check if 'row' parameter is in the test case (from parametrize)
    if "row" in item.funcargs:
        row = item.funcargs["row"]
        if "description" in row:
            description = row["description"]

    # Store description as a user property (MUST be a list of tuples)
    report.user_properties = [("description", description)]

    # Take a screenshot if the test fails
    if report.when == "call" and report.failed:
        driver = getattr(item.cls, "driver", None) or getattr(item, "driver", None)

        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved to {screenshot_name}")

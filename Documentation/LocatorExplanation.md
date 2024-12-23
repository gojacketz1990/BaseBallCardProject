# Locator Setup and Information

## Page Object Locators
All locators are housed in the individual page classes.  They will be defined as a list of tuples.  For example:

    username_locator = [
        ("name", "user-name"),
        ("id", "user-name"),
        ("xpath", "//input[@placeholder='Username']")

Each locator for the individual web element has a tuple which contains an ordered list of strings.  You can iterate over the list to access each tuple:

    for locator in username_locator:
        locator_type, locator_value = locator


Which calls the _get_by_method and returns the locator By Method to use:

    def _get_by_method(self, locator_type):
        """Retrieve the Selenium By method for a given locator type."""
        if locator_type not in self.LOCATOR_DICT:
            raise ValueError(f"Invalid locator type: {locator_type}. Valid types are: {list(self.LOCATOR_DICT.keys())}")
        return self.LOCATOR_DICT[locator_type]

For example, "name" is the locator type and "user-name" is the locator value.
In the BasePage class we have defined a dictionary of all of the locator types and mapped them to the values:

    LOCATOR_DICT = {
        "id": By.ID,
        "name": By.NAME,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "class_name": By.CLASS_NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "tag_name": By.TAG_NAME,
    }

The locators are done this way to build in a self-healing functionality in the case that one or more of the locators has changed in the DOM (Document Object Model).
The get_element methods are an extension of find_element and will use the _get_by_method to locate the locator type value.
If an element is not found, the method will self-heal by using a second or third method to find the element.
This will work on any of the custom methods also (such as wait_presence_element and wait_and_click_element).


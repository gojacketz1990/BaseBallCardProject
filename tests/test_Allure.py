import random
from faker import Faker
import pytest
import allure


from faker import Faker
import pytest
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import configparser


# Load CSV data as a class attribute
file_path = '../TestData/AddCardValidation.csv'
csv_data = read_csv(file_path)  # Returns a list of dictionaries

# Create a list of tuples: (row, test_id)
test_cases = [(row, row['TestName']) for row in csv_data]

#To run:  pytest --alluredir=allure-results
#to generate report allure generate allure-results --clean -o allure-report
#to view:  allure open allure-report
#@pytest.mark.usefixtures("setup_and_teardown")  # Ensure setup from BaseTests is applied
class TestUserHomePage(BaseTests):

    @pytest.mark.parametrize("row", csv_data, ids=lambda row: row['TestName'])
    @allure.title("Test Add Card Form")
    @allure.description("This test validates the add card form using data from CSV")
    def test_add_card_form(self, row, request):
        with allure.step("Start test for adding a card"):
            test_name = row.get('TestName')
            allure.attach(name="Test Case", body=f"Running Test: {test_name}", attachment_type=allure.attachment_type.TEXT)


        print(f"Running Test: {test_name}")


        log = self.getLogger()
        #cardCatalogHome = CardCatalogHome(self.driver)
        with allure.step("Authenticate the user"):
            #authenticationPage = cardCatalogHome.header.navigate_authenticate()
            #userHomePage = authenticationPage.login_to_site(self.username, self.password)
            print("step")

        with allure.step("Navigate to Add Card Page"):
            #addCardPage = userHomePage.header.navigate_addcard()
            print("step 2")
        # Generate fak
        # e data
        fake = Faker()
        fake_name = fake.name()
        fake_address = fake.address()
        random_number = random.randint(1000, 9999)

        generated_description = fake_name + "\n" + fake_address
        # Call the addCardFormValidation method
        allure.dynamic.description(row["description"])
           # Determine if description from CSV should be used
        with allure.step("Prepare form data"):
            use_generated_description = row.get('description').strip().lower() == 'true'
            description = generated_description if use_generated_description else row.get('DescriptionText', '')

            choices = ["Bo.jpg", "fermin.jpeg", "hogan.jpeg", "Skenes.jpeg", "trout.jpeg"]
            random_choice = random.choice(choices)
            use_file = row.get('file').strip().lower() == 'true'
            filePath = f'/Users/gojacketz/PycharmProjects/BaseballCardProject/TestData/{random_choice}' if use_file else ""

            allure.attach(name="Generated Data", body=f"Card Name: {fake_name}\nFilePath: {filePath}", attachment_type=allure.attachment_type.TEXT)


        with allure.step("Validate Add Card Form"):
            print("testing")



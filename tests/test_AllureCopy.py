import random
from faker import Faker
import pytest
import allure
from utilities.BaseTests import BaseTests
from utilities.csv_utils import read_csv

# Load CSV data
file_path = '../TestData/AddCardValidation.csv'
csv_data = read_csv(file_path)

class TestUserHomePage(BaseTests):

    @pytest.mark.parametrize("row", csv_data, ids=lambda row: row['TestName'])
    @allure.title("Test Add Card Form")
    def test_add_card_form(self, row):
        test_name = row.get('TestName')
        description = row.get('DescriptionText', 'No description provided')

        # Attach description dynamically
        allure.dynamic.description(f"{description}\nRunning Test: {test_name}")

        # Attach all relevant data
        allure.attach(name="Test Case Data", body=str(row), attachment_type=allure.attachment_type.TEXT)

        fake = Faker()
        fake_name = fake.name()
        fake_address = fake.address()
        generated_description = fake_name + "\n" + fake_address

        use_generated_description = row.get('description').strip().lower() == 'true'
        description_to_use = generated_description if use_generated_description else row.get('DescriptionText', '')

        choices = ["Bo.jpg", "fermin.jpeg", "hogan.jpeg", "Skenes.jpeg", "trout.jpeg"]
        random_choice = random.choice(choices)
        use_file = row.get('file').strip().lower() == 'true'
        file_path = f'/Users/gojacketz/PycharmProjects/BaseballCardProject/TestData/{random_choice}' if use_file else ""

        allure.attach(name="Generated Data", body=f"Card Name: {fake_name}\nFilePath: {file_path}\nDescription: {description_to_use}", attachment_type=allure.attachment_type.TEXT)

        # Your test logic here...
        print("testing")

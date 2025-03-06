import random
import pytest
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import configparser

# Load CSV data as a class attribute
file_path = '../TestData/AddCardValidation.csv'
csv_data = read_csv(file_path)  # Returns a list of dictionaries
# Create a list of tuples: (row, test_id)
test_cases = [(row, row['TestName']) for row in csv_data]

#@pytest.mark.usefixtures("setup_and_teardown")  # Ensure setup from BaseTests is applied
class TestUserHomePage():

    @pytest.mark.parametrize("row", csv_data, ids=lambda row: row['TestName'])

    def test_random_mycard_form(self, row, record_property):
        # Store description in request.node for later use
        description = row.get('description')  # Extract description
        print(description)

        # Store the description in the report
        record_property("description", description)
        test_name = row.get('TestName')

        print(f"Running Test: {test_name}")



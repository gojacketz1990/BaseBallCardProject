import random
from faker import Faker
import pytest
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import time
from faker import Faker
import pytest
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import configparser

# Load CSV data as a class attribute
file_path = '../TestData/UpdateCardValidation.csv'
csv_data = read_csv(file_path)  # Returns a list of dictionaries

# Create a list of tuples: (row, test_id)
test_cases = [(row, row['cardname']) for row in csv_data]

#pytest --html=report.html --self-contained-htmlcd

@pytest.mark.usefixtures("setup_and_teardown")  # Ensure setup from BaseTests is applied
class TestUserHomePage(BaseTests):

    def test_delete_rows(self):

        log = self.getLogger()
        cardCatalogHome = CardCatalogHome(self.driver)
        authenticationPage = cardCatalogHome.click_authenticate()
        userHomePage = authenticationPage.login_to_site(self.username, self.password)
        myCardPage = userHomePage.click_mycards()
        time.sleep(3)

        for i in range(1, 1501):
            myCardPage.deleteFirstCard()
            time.sleep(3)

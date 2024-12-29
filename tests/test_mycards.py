import random
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import time
import configparser
class TestMyCardsPage(BaseTests):

    def test_userlink(self):
        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()

        userHomePage = authenticationPage.login_to_site(self.username, self.password)

        myCardPage = userHomePage.click_userlink()
        time.sleep(3)

    def test_delete_mycard_form(self):
        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()

        userHomePage = authenticationPage.login_to_site('gojacketz@icloud.com', 'reapit')

        myCardPage = userHomePage.click_mycards()

        myCardPage.deleteCard('Kayla Harrison')

    def test_update_mycard_form(self):
        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()

        userHomePage = authenticationPage.login_to_site('gojacketz@icloud.com', 'reapit')

        myCardPage = userHomePage.click_mycards()

        myCardPage.deleteCard('Kayla Harrison')





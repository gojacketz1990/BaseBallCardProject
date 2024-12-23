import random
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import time

class TestUpdateCardsPage(BaseTests):


    def test_update_mycard_form(self):
        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()

        userHomePage = authenticationPage.login_to_site('gojacketz@gmail.com', 'reapit')

        myCardPage = userHomePage.click_mycards()

        updateCardPage = myCardPage.editCard('Nicholas Clarke')

        #updateCardPage.updatecardname('Homer J Simpson')

        time.sleep(3)

        myCardPage = updateCardPage.updateCardAllFields("Football", "Howie Feltersnatch", "8373672", "True")





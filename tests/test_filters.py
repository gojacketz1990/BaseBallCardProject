import random
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import time
import configparser

class TestMyCardsPage(BaseTests):

    def test_filter(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.header.navigate_authenticate()

        userHomePage = authenticationPage.login_to_site(self.username, self.password)

        myCardPage = userHomePage.header.navigate_userlink()
        time.sleep(3)

        cardsbeforefilter = myCardPage.countCards()
        print(cardsbeforefilter)

        myCardPage.selectCompanyFilter("Bowman")
        myCardPage.selectReleaseFilter("Draft")
        cardsafterfilter = myCardPage.countCards()
        print(cardsafterfilter)





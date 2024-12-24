import random
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import time
class TestMyCardsPage(BaseTests):

    def test_filter(self):
        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()

        userHomePage = authenticationPage.login_to_site('gojacketz@gmail.com', 'reapit')

        myCardPage = userHomePage.click_userlink()
        time.sleep(3)

        cardsbeforefilter = myCardPage.countCards()
        print(cardsbeforefilter)

        myCardPage.selectCompanyFilter("Bowman")
        myCardPage.selectReleaseFilter("Draft")
        cardsafterfilter = myCardPage.countCards()
        print(cardsafterfilter)





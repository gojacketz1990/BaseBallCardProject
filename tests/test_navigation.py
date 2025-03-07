import random
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import time
import configparser
from pages.HeaderComponents import HeaderComponent


class TestMyCardsPage(BaseTests):

    def test_navigation_between_pages(self):
        log = self.getLogger()

        # Start at the home page
        cardCatalogHome = CardCatalogHome(self.driver)

        # Click Authenticate (from Header)
        authenticationPage = cardCatalogHome.click_authenticate()

        # Login
        userHomePage = authenticationPage.login_to_site(self.username, self.password)

        # Navigate to My Cards Page
        myCardsPage = userHomePage.click_mycards()
        #assert "My Cards" in myCardsPage.driver.title  # Validate navigation
        time.sleep(2)
        # Navigate to Card Summary from My Cards Page
        cardSummaryPage = myCardsPage.header.navigate_cardsummary()
        #assert "Card Summary" in cardSummaryPage.driver.title  # Validate navigation
        time.sleep(2)
        # Navigate to Graded Card Summary
        gradedCardSummaryPage = cardSummaryPage.header.navigate_gradedcardsummary()
        #assert "Graded Card Summary" in gradedCardSummaryPage.driver.title
        time.sleep(2)
        # Navigate back to User Home from Card Summary Page
        userHomePage = gradedCardSummaryPage.header.navigate_userlink()
        #assert "User Home" in userHomePage.driver.title  # Validate navigation
        time.sleep(2)
        # Navigate to Graded Card Summary

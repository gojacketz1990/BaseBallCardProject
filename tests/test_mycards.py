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

    # def test_cardsummary(self):
    #     log = self.getLogger()
    #
    #     cardCatalogHome = CardCatalogHome(self.driver)
    #
    #     authenticationPage = cardCatalogHome.click_authenticate()
    #
    #     userHomePage = authenticationPage.login_to_site(self.username, self.password)
    #
    #     myCardPage = userHomePage.click_mycards()
    #
    #
    #     time.sleep(8)
    #
    # def test_userlink(self):
    #     log = self.getLogger()
    #
    #     cardCatalogHome = CardCatalogHome(self.driver)
    #
    #     authenticationPage = cardCatalogHome.navigate_to_authentication()
    #
    #     userHomePage = authenticationPage.login_to_site("gojacketz@icloud.com", "reapit")
    #
    #     myCardSummary = userHomePage.click_cardsummary()
    #     time.sleep(3)
    #
    # def test_delete_mycard_form(self):
    #     log = self.getLogger()
    #
    #     cardCatalogHome = CardCatalogHome(self.driver)
    #
    #     authenticationPage = cardCatalogHome.navigate_to_authentication()
    #
    #     userHomePage = authenticationPage.login_to_site(self.username, self.password)
    #
    #     myCardPage = userHomePage.click_mycards()
    #
    #     myCardPage.deleteCard('Kayla Harrison')
    #
    # def test_update_mycard_form(self):
    #     log = self.getLogger()
    #
    #     cardCatalogHome = CardCatalogHome(self.driver)
    #
    #     authenticationPage = cardCatalogHome.click_authenticate()
    #
    #     userHomePage = authenticationPage.login_to_site(self.username, self.password)
    #
    #     myCardPage = userHomePage.click_mycards()
    #
    #     myCardPage.deleteCard('Kayla Harrison')
    #
    #
    #
    #


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
        authenticationPage = cardCatalogHome.header.navigate_authenticate()

        # Login
        userHomePage = authenticationPage.login_to_site(self.username, self.password)

        # Navigate to My Cards Page
        myCardsPage = userHomePage.header.navigate_mycards()
        assert myCardsPage.is_text_present("Sort by Number"), "Text not found on page"
        time.sleep(2)


        # Navigate to Card Summary from My Cards Page
        cardSummaryPage = myCardsPage.header.navigate_cardsummary()

        assert cardSummaryPage.is_text_present("Card Release"), "Text not found on page"


        time.sleep(1)
        # Navigate to Graded Card Summary
        gradedCardSummaryPage = cardSummaryPage.header.navigate_gradedcardsummary()
        assert gradedCardSummaryPage.is_text_present("Grade"), "Text not found on page"
        time.sleep(1)
        # Navigate back to User Home from Card Summary Page
        userHomePage = gradedCardSummaryPage.header.navigate_userlink()
        assert userHomePage.is_text_present("Matthew"), "Text not found on page"
        time.sleep(1)
        # Navigate to Graded Card Summary

        addCardPage = userHomePage.header.navigate_addcard()
        time.sleep(1)

        assert addCardPage.is_text_present("Is this card an Insert"), "Text not found on page"

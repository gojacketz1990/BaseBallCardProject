
import random
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import time
import configparser
from pages.HeaderComponents import HeaderComponent
from pages.UserHomePage import UserHomePage

class TestMyCardsPage(BaseTests):

    def test_navigation_between_pages(self):
        log = self.getLogger()

        # Start at the home page
        cardCatalogHome = CardCatalogHome(self.driver)

        # Click Authenticate (from Header)
        authenticationPage = cardCatalogHome.header.navigate_authenticate()

        # Login

        result = authenticationPage.login_to_site(self.username, self.password)

        # ✅ Fix: Check if `result` is a dictionary before looking for "error"
        if isinstance(result, dict) and "error" in result:
            expected_error = "Invalid credentials, could not log you in."
            assert result["error"] == expected_error, f"Expected '{expected_error}', but got '{result['error']}'"

        else:
            # ✅ If login was successful, assert that we are on the correct page
            assert isinstance(result, UserHomePage), "Login returned an unexpected result!"
            userHomePage = result

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

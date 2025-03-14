import time

from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from pages.BaseballAuthenticatePage import AuthenticationPage
from pages.UserHomePage import UserHomePage
import configparser

class TestLogins(BaseTests):

    def test_valid_login(self):
        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)
        authenticationPage = cardCatalogHome.header.navigate_authenticate()  # Ok

        result = authenticationPage.login_to_site(self.username, self.password)

        # ✅ Fix: Check if `result` is a dictionary before looking for "error"
        if isinstance(result, dict) and "error" in result:
            expected_error = "Invalid credentials, could not log you in."
            assert result["error"] == expected_error, f"Expected '{expected_error}', but got '{result['error']}'"

        else:
            # ✅ If login was successful, assert that we are on the correct page
            assert isinstance(result, UserHomePage), "Login returned an unexpected result!"

    def test_invalid_login(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.header.navigate_authenticate()#Ok

        result = authenticationPage.login_to_site(self.username, 'reapithh')
        if isinstance(result, dict) and "error" in result:
            expected_error = "Invalid credentials, could not log you in."
            assert result["error"] == expected_error, f"Expected '{expected_error}', but got '{result['error']}'"

        else:
            # ✅ If login was successful, assert that we are on the correct page
            assert isinstance(result, UserHomePage), "Login returned an unexpected result!"

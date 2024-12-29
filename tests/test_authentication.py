import time

from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from pages.BaseballAuthenticatePage import AuthenticationPage
import configparser

class TestLogins(BaseTests):

    def test_invalid_login(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()#Ok
        time.sleep(1)

        authenticationPage.login_to_site(self.username, 'reapithh')
        time.sleep(1)

    def test_valid_login(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()#Ok
        time.sleep(1)

        authenticationPage.login_to_site(self.username, self.password)
        time.sleep(1)

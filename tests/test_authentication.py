import time

from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from pages.BaseballAuthenticatePage import AuthenticationPage


class TestLogins(BaseTests):

    def test_invalid_login(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()#Ok
        time.sleep(1)

        authenticationPage.login_to_site('gojacketz@icloud.com', 'reapithh')
        time.sleep(1)

    def test_valid_login(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()#Ok
        time.sleep(1)

        authenticationPage.login_to_site('gojacketz@icloud.com', 'reapit')
        time.sleep(1)

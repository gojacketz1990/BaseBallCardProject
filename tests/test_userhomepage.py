import time

from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from pages.BaseballAuthenticatePage import AuthenticationPage
from pages.UserHomePage import UserHomePage
import configparser
class TestUserHomePage(BaseTests):

    def test_mycard_link(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()#Ok
        time.sleep(2)

        userHomePage = authenticationPage.login_to_site(self.username, self.password)
        time.sleep(1)


        userHomePage.click_mycards()
        time.sleep(3)




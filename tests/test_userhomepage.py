import time

from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from pages.BaseballAuthenticatePage import AuthenticationPage
from pages.UserHomePage import UserHomePage

class TestUserHomePage(BaseTests):

    def test_mycard_link(self):

        log = self.getLogger()

        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()#Ok
        time.sleep(2)

        userhomepage = authenticationPage.login_to_site('gojacketz@icloud.com', 'reapit')
        time.sleep(1)

        #userhomepage = UserHomePage(self.driver)

        userhomepage.click_mycards()
        time.sleep(3)




from selenium.common.exceptions import TimeoutException
from pages.BasePage import BasePage

from utilities.BaseTests import BaseTests
from locators.card_catalog_home_locators import CardCatalogHomeLocators
from pages.BaseballAuthenticatePage import AuthenticationPage
from pages.HeaderComponents import HeaderComponent

class CardCatalogHome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CardCatalogHomeLocators = CardCatalogHomeLocators()
        self.header = HeaderComponent(driver)

    # def click_cardcatalogHome(self):
    #     self.element_click( self.CardCatalogHomeLocators.card_catalog_home_locator)
    #
    #
    #
    # def click_authenticate(self):
    #     return self.header.navigate_authenticate()
    #
    # def click_allusers(self):
    #     self.element_click( self.CardCatalogHomeLocators.all_users_locator)



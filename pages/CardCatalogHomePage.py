from selenium.common.exceptions import TimeoutException
from pages.BasePage import BasePage

from utilities.BaseTests import BaseTests
from locators.card_catalog_home_locators import CardCatalogHomeLocators
from pages.BaseballAuthenticatePage import AuthenticationPage



class CardCatalogHome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CardCatalogHomeLocators = CardCatalogHomeLocators()

    def click_cardcatalogHome(self):
        self.element_click( self.CardCatalogHomeLocators.card_catalog_home_locator)



    def click_authenticate(self):
        self.element_click( self.CardCatalogHomeLocators.authenticate_locator)
        return AuthenticationPage(self.driver)

    def click_allusers(self):
        self.element_click( self.CardCatalogHomeLocators.all_users_locator)

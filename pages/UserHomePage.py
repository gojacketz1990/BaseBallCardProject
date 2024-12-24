

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from locators.users_home_page_locators import UsersHomePageLocators

class UserHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.usersHomePageLocators = UsersHomePageLocators()

    def click_addCard(self):
        from pages.AddCardPage import AddCardPage  # Lazy import to avoid circular dependency
        self.element_click(self.usersHomePageLocators.add_card_link_locator)
        return AddCardPage(self.driver)

    def click_mycards(self):
        from pages.MyCardsPage import MyCardsPage  # Lazy import to avoid circular dependency
        self.element_click(self.usersHomePageLocators.my_cards_link_locator)
        return MyCardsPage(self.driver)

    def click_userlink(self):
        from pages.MyCardsPage import MyCardsPage  # Lazy import to avoid circular dependency
        self.element_click( self.usersHomePageLocators.user_link_locator)
        return MyCardsPage(self.driver)

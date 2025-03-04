

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from locators.users_home_page_locators import UsersHomePageLocators
from pages.HeaderComponents import HeaderComponent


class UserHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)

    # def click_addCard(self):
    #     return self.header.navigate_addcard()
    #
    # def click_mycards(self):
    #     return self.header.navigate_mycards()
    #
    # def click_userlink(self):
    #     return self.header.navigate_userlink()
    #
    # def click_cardsummary(self):
    #     return self.header.navigate_cardsummary()
    #
    # def click_gradedcardsummary(self):
    #     return self.header.navigate_gradedcardsummary()


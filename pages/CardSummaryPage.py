from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from pages.HeaderComponents import HeaderComponent
from locators.card_summary_page_locators import CardSummaryPageLocators

import time
import random
class CardSummaryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cardSummaryPageLocators = CardSummaryPageLocators()
        self.header = HeaderComponent(driver)

    def card_summary(self):
        return self.header.navigate_cardsummary()



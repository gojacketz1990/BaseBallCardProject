from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from locators.graded_card_summary_page_locators import GradedCardSummaryPageLocators
from pages.HeaderComponents import HeaderComponent
import time
import random
from pages.HeaderComponents import HeaderComponent

class GradedCardSummaryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.gradedCardSummaryPageLocators = GradedCardSummaryPageLocators()
        self.header = HeaderComponent(driver)

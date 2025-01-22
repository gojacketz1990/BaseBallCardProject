from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from locators.my_cards_page_locators import MyCardsPageLocators
from selenium.webdriver.support import expected_conditions as EC

import time
import random

class MyCardsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.myCardsPageLocators = MyCardsPageLocators()

    def selectSportFilter(self, sport):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.sportfilterdropdown_locator, sport)

    def selectCompanyFilter(self, cardcompany):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.cardcompanyfilterdropdown_locator, cardcompany)

    def selectReleaseFilter(self, release):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.cardreleasefilterdropdown_locator, release)

    def selectYearFilter(self, year):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.yearfilterdropdown_locator, year)

    def selectCardNameFilter(self, cardname):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.cardname_locator, cardname)

    def parallelTypeFilter(self, paralleltype):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.parallelfilterdropdown_locator, paralleltype)

    def insertTypeFilter(self, inserttype):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.insertfilterdropdown_locator, inserttype)

    def autoFilter(self, isAuto):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.autographfilterdropdown_locator, isAuto)

    def relicFilter(self, isRelic):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.relicfilterdropdown_locator, isRelic)

    def gradeFilter(self, grade):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.gradefilterdropdown_locator, grade)

    def sortbyNumber(self, sort):
        self.select_from_dropdown_by_visible_text(self.myCardsPageLocators.sortoderdropdown_locator, sort)

    def deleteFirstCard(self):
        self.element_click(self.myCardsPageLocators.first_delete_locator)
        self.element_click(self.myCardsPageLocators.confirm_delete_button_locator)

    def deleteCard(self,cardname):

        cards = self.get_elements(self.myCardsPageLocators.cards_locator)
        print(len(cards))
        item_found = False

        for card in cards:
            cardText = self.retrieve_child_element_text(card, self.myCardsPageLocators.cardname_locator)
            print(cardText)
            if cardText == cardname:
                time.sleep(3)
                self.element_child_click(card, self.myCardsPageLocators.delete_locator)
                time.sleep(3)
                self.element_click(self.myCardsPageLocators.confirm_delete_button_locator)
                time.sleep(2)

    def editCard(self,cardname):
        from pages.UpdateCardPage import UpdateCardPage  # Lazy import to avoid circular dependency
        cards = self.get_elements(self.myCardsPageLocators.cards_locator)
        #print(len(cards))
        item_found = False

        for card in cards:
            cardText = self.retrieve_child_element_text(card, self.myCardsPageLocators.cardname_locator)
            #print(cardText)
            if cardText == cardname:
                time.sleep(3)
                self.element_child_click(card, self.myCardsPageLocators.edit_locator)
                time.sleep(3)
                return UpdateCardPage(self.driver)


    def countCards(self):
        from pages.UpdateCardPage import UpdateCardPage  # Lazy import to avoid circular dependency
        cards = self.get_elements(self.myCardsPageLocators.cards_locator)
        #print(len(cards))
        return len(cards)


    def userHome(self):
        from pages.UserHomePage import UserHomePage
        self.element_click(self.myCardsPageLocators.userhome)
        return UserHomePage(self.driver)

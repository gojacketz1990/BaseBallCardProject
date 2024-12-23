from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from locators.update_card_page_locators import UpdateCardPageLocators

import time
import random

class UpdateCardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.updateCardPageLocators = UpdateCardPageLocators()

    def updatecardname(self, cardname):
        self.wait_presence_element(self.updateCardPageLocators.cardname_locator)
        self.type_into_element_clear(cardname,self.updateCardPageLocators.cardname_locator)
        time.sleep(3)

    def updateCardNumber(self,cardnumber):
        self.type_into_element_clear(cardnumber,self.updateCardPageLocators.cardnumber_locator)

    def updatecardbutton(self):
        self.element_click(self.updateCardPageLocators.update_card_button_locator)
        time.sleep(2)


    def updateSport(self, sport):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.sport_dropdown_locator, sport)

    def removeSport(self):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.sport_dropdown_locator, "-- Select Sport --")


    def uploadFile(self,filePath):
        self.sendKeys_into_element(filePath, self.updateCardPageLocators.hidden_imageinput_locator)





    def randomselectCardCompany(self):
        self.select_random_in_dropdown(self.updateCardPageLocators.companydropdown_locator)

    def selectCardCompany(self, company):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.companydropdown_locator, company)

    def randomselectRelease(self):
        self.select_random_in_dropdown(self.updateCardPageLocators.cardreleasedropdown_locator)

    def selectRelease(self, release):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.cardreleasedropdown_locator, release)

    def randomselectYear(self):
        self.select_random_in_dropdown(self.updateCardPageLocators.year_locator)

    def selectYear(self, year):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.year_locator, year)

    def click_addcardbutton(self):
        self.element_click(self.updateCardPageLocators.addcardbutton_locator)

    def select_parallel(self):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.isparallel_dropdown_locator, "Yes")

    def select_random_parallel(self):
        self.select_random_in_dropdown(self.updateCardPageLocators.paralleltype_dropdown_locator)

    def select_paralleltype(self, parallel):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.paralleltype_dropdown_locator, parallel)

    def select_insert(self):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.isinsert_dropdown_locator,"Yes")

    def select_random_insert(self):
        self.select_random_in_dropdown(self.updateCardPageLocators.inserttype_dropdown_locator)

    def select_inserttype(self, insert):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.inserttype_dropdown_locator, insert)

    def select_isgraded(self):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.isgraded_locator,"Yes")

    def select_random_gradecompany(self):
        self.select_random_in_dropdown(self.updateCardPageLocators.gradecompany_locator)

    def select_gradecompany(self, gradecompany):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.gradecompany_locator, gradecompany)


    def select_random_grade(self):
        self.select_random_in_dropdown(self.updateCardPageLocators.grade_locator)

    def select_grade(self, grade):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.grade_locator, grade)

    def enterCertID(self,certnumber):
        self.type_into_element_clear(certnumber,self.updateCardPageLocators.certid_locator)

    def isAuto(self):
        self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.isautograph_locator,"Yes")

    def isRelic(self):
             self.select_from_dropdown_by_visible_text(self.updateCardPageLocators.isrelic_locator,"Yes")

    def select_numbered(self,OnOff):
        self.check_checkbox(self.updateCardPageLocators.isnumbered_checkbox_locator,OnOff)

    def set_number(self, number):
        self.type_into_element_clear(number, self.updateCardPageLocators.number_locator)

    def set_number_out_of(self, numberoutof):
        self.type_into_element_clear(numberoutof, self.updateCardPageLocators.numberoutof_locator)

    def enterDescription(self,description):
        self.type_into_element_clear(description,self.updateCardPageLocators.description_locator)

    def isUpdateFormActive(self):
       return self.isButtonActive(self.updateCardPageLocators.update_card_button_locator)


    def updateCardAllFields(self, sport, cardname, cardnumber,cardcompany, cardrelease, isParallel, paralleltype, isInsert,
                              inserttype, isGraded, gradecompany, grade, certnumber, isRelic, isAuto, isnumbered, number, numberoutof,
                                notes, year, file, expectedstate):
        from pages.MyCardsPage import MyCardsPage
        if sport != '':
            self.updateSport(sport)
        else:
            self.updateSport("-- Select Sport --")
        if cardname != '':
            self.updatecardname(cardname)
        if cardnumber !='':
            self.updateCardNumber(cardnumber)



        if cardcompany != '':
            self.selectCardCompany(cardcompany)
            if cardrelease != '':
                self.selectRelease(cardrelease)
            else:
                self.selectRelease("-- Select Card Release --")
        else:
            self.selectCardCompany("-- Select Card Company --")



        if isParallel == True:
            self.select_parallel()
            if paralleltype != '':
                self.select_paralleltype(paralleltype)

        if isInsert == True:
            self.select_insert()
            if inserttype != '':
                self.select_inserttype(inserttype)


        if isGraded == True:
            self.select_isgraded()
            if gradecompany != '':
                self.select_gradecompany(gradecompany)
                if grade != '':
                    self.select_grade(grade)
                    if certnumber != '':
                        self.enterCertID(certnumber)


        if isRelic == True:
            self.isRelic()

        if isAuto == True:
            self.isAuto()

        if isnumbered == True:
            self.select_numbered("ON")
            if number != '':
                self.set_number(number)
            if numberoutof != '':
                self.set_number_out_of(numberoutof)


        self.enterDescription(notes)

        if year != '':
            self.selectYear(year)
        else:
            self.selectYear("-- Select Year --")
        time.sleep(5)


        if file != '':
            self.uploadFile(file)

        isActive = self.isUpdateFormActive()

        expectedstate = bool(expectedstate)  # Normalize expectedState to boolean



        assert isActive == expectedstate, f"The Update Card Button state mismatch: Expected {expectedstate}, but got {isActive}."

        # Navigate to My Cards

        if isActive:
            self.element_click(self.updateCardPageLocators.update_card_button_locator)
            time.sleep(1)

            return MyCardsPage(self.driver)
        else:
            print("isActive is False. Skipping the action.")
            # Do something else or handle the case where isActive is False

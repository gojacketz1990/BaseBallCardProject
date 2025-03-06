from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from locators.add_card_page_locators import AddCardPageLocators
from pages.HeaderComponents import HeaderComponent

import time
import random

class AddCardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.addCardPageLocators = AddCardPageLocators()

    def click_mycards(self):
        self.element_click(self.addCardPageLocators.my_cards_link_locator)
    def selectSport(self, sport):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.sport_dropdown_locator, sport)

    def removeSport(self):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.sport_dropdown_locator, "-- Select Sport --")
    def enterCardName(self,cardname):
        self.wait_presence_element(self.addCardPageLocators.cardname_locator)
        self.type_into_element(cardname,self.addCardPageLocators.cardname_locator)

    def uploadFile(self,filePath):
        self.sendKeys_into_element(filePath, self.addCardPageLocators.hidden_imageinput_locator)


    def enterCardNumber(self,cardnumber):
        self.type_into_element(cardnumber,self.addCardPageLocators.cardnumber_locator)


    def randomselectCardCompany(self):
        self.select_random_in_dropdown(self.addCardPageLocators.companydropdown_locator)

    def selectCardCompany(self, company):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.companydropdown_locator, company)

    def randomselectRelease(self):
        self.select_random_in_dropdown(self.addCardPageLocators.cardreleasedropdown_locator)

    def selectRelease(self, release):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.cardreleasedropdown_locator, release)

    def randomselectYear(self):
        self.select_random_in_dropdown(self.addCardPageLocators.year_locator)

    def selectYear(self, year):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.year_locator, year)

    def click_addcardbutton(self):
        self.element_click(self.addCardPageLocators.addcardbutton_locator)

    def select_parallel(self):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.isparallel_dropdown_locator, "Yes")

    def select_random_parallel(self):
        self.select_random_in_dropdown(self.addCardPageLocators.paralleltype_dropdown_locator)

    def select_paralleltype(self, parallel):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.paralleltype_dropdown_locator, parallel)

    def select_insert(self):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.isinsert_dropdown_locator,"Yes")

    def select_random_insert(self):
        self.select_random_in_dropdown(self.addCardPageLocators.inserttype_dropdown_locator)

    def select_inserttype(self, insert):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.inserttype_dropdown_locator, insert)

    def select_isgraded(self):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.isgraded_locator,"Yes")

    def select_random_gradecompany(self):
        self.select_random_in_dropdown(self.addCardPageLocators.gradecompany_locator)

    def select_gradecompany(self, gradecompany):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.gradecompany_locator, gradecompany)


    def select_random_grade(self):
        self.select_random_in_dropdown(self.addCardPageLocators.grade_locator)

    def select_grade(self, grade):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.grade_locator, grade)

    def enterCertID(self,certnumber):
        self.type_into_element(certnumber,self.addCardPageLocators.certid_locator)

    def isAuto(self):
        self.select_from_dropdown_by_visible_text(self.addCardPageLocators.isautograph_locator,"Yes")

    def isRelic(self):
             self.select_from_dropdown_by_visible_text(self.addCardPageLocators.isrelic_locator,"Yes")

    def select_numbered(self,OnOff):
        self.check_checkbox(self.addCardPageLocators.isnumbered_checkbox_locator,OnOff)

    def set_number(self, number):
        self.type_into_element(number, self.addCardPageLocators.number_locator)

    def set_number_out_of(self, numberoutof):
        self.type_into_element(numberoutof, self.addCardPageLocators.numberoutof_locator)

    def enterDescription(self,description):
        self.type_into_element(description,self.addCardPageLocators.description_locator)

    def isAddFormActive(self):
       return self.isButtonActive(self.addCardPageLocators.addcardbutton_locator)

    def addRandomCard(self, sport, cardname, cardnumber, certnumber, filePath,description):
        from pages.UserHomePage import UserHomePage  # Lazy import to avoid circular dependency

        self.selectSport(sport)

        self.enterCardName(cardname)

        self.enterCardNumber(cardnumber)
        self.randomselectCardCompany()
        self.randomselectRelease()

        if random.choice([True, False]):

            self.select_insert()
            self.select_random_insert()

        if random.choice([True, False]):
            self.select_parallel()
            self.select_random_parallel()

        if random.choice([True, False]):
            self.select_isgraded()
            self.select_random_gradecompany()
            self.select_random_grade()
            self.enterCertID(certnumber)

        if random.choice([True, False]):
            self.isAuto()
        if random.choice([True, False]):
            self.isRelic()
        self.enterDescription(description)


        self.randomselectYear()
        self.uploadFile(filePath)
        #time.sleep(1)
        self.click_addcardbutton()
        time.sleep(1)
        return UserHomePage(self.driver)


    def addCardFormValidation(self, sport, cardname, cardnumber, cardcompany, cardrelease, isParallel, paralleltype, isInsert,
                              inserttype, isGraded, gradecompany, grade, certnumber, isRelic, isAuto, isnumbered, number, numberoutof,
                                notes, year, file, expectedstate):

        from pages.UserHomePage import UserHomePage  # Lazy import to avoid circular dependency

        # Set the form fields
        if sport != '':
            self.selectSport(sport)

        if cardname != '':
            self.enterCardName(cardname)

        if cardnumber != '':
            self.enterCardNumber(cardnumber)

        if cardcompany != '':
            self.selectCardCompany(cardcompany)

        if cardrelease != '':
            self.selectRelease(cardrelease)


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

        if file != '':
            self.uploadFile(file)

        # Wait for the form to update

        # Check the state of the Add Card button
        isActive = self.isAddFormActive()

        expectedstate = bool(expectedstate)  # Normalize expectedState to boolean

        assert isActive == expectedstate, f"The Add Card Button state mismatch: Expected {expectedstate}, but got {isActive}."

        # Navigate to My Cards
        self.click_mycards()

        return UserHomePage(self.driver)


    def addCard(self, sport, cardname, cardnumber, cardcompany, cardrelease, isParallel, paralleltype, isInsert,
                              inserttype, isGraded, gradecompany, grade, certnumber, isRelic, isAuto, isnumbered, number, numberoutof,
                                notes, year, file):

        from pages.UserHomePage import UserHomePage  # Lazy import to avoid circular dependency

        # Set the form fields
        if sport != '':
            self.selectSport(sport)

        if cardname != '':
            self.enterCardName(cardname)

        if cardnumber != '':
            self.enterCardNumber(cardnumber)

        if cardcompany != '':
            self.selectCardCompany(cardcompany)

        if cardrelease != '':
            self.selectRelease(cardrelease)


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

        if file != '':
            self.uploadFile(file)

        # Wait for the form to update

        # Check the state of the Add Card button
        isActive = self.isAddFormActive()

        #expectedstate = bool(expectedstate)  # Normalize expectedState to boolean

        #assert isActive == expectedstate, f"The Add Card Button state mismatch: Expected {expectedstate}, but got {isActive}."

        # Add Card
        self.click_addcardbutton()

        time.sleep(3)

        return UserHomePage(self.driver)


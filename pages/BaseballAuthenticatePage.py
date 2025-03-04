from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
#from pages.navigation import Navigator

from utilities.BaseTests import BaseTests
from locators.card_authentication_page_locators import AuthenticationPageLocators
from pages.UserHomePage import UserHomePage

import time

class AuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.authenticationPageLocators = AuthenticationPageLocators()



    def enter_username(self, username):
        self.type_into_element(username, self.authenticationPageLocators.name_locator)

    def enter_password(self, password):
        self.type_into_element(password, self.authenticationPageLocators.password_locator)

    def enter_email(self, email):
        self.type_into_element(email, self.authenticationPageLocators.email_locator)

    def click_switch_mode(self):
        self.element_click(self.authenticationPageLocators.switch_auth_mode_locator)


    def click_login_button(self):
        self.element_click(self.authenticationPageLocators.loginbutton_locator)
        #return UserHomePage(self.driver)
        try:
            error_message = self.wait_presence_element(self.authenticationPageLocators.login_error_locator).text
            print(error_message)
            time.sleep(2)
            self.element_child_click(self.authenticationPageLocators.error_okay_locator)
            return self#next page goes here
        except TimeoutException:
            #self.logger.info(f"Login successful for User")
            return UserHomePage(self.driver)

    def click_signup_button(self):
        self.element_click(self.authenticationPageLocators.signupbutton_locator)
        #self.element_click(self.authenticationPageLocators.error_okay_locator)
        try:
            error_message = self.wait_presence_element(self.authenticationPageLocators.login_error_locator).text
            print(error_message)
            time.sleep(2)
            self.element_child_click(self.authenticationPageLocators.error_okay_locator)
            time.sleep(2)
            #self.logger.error(f"Login failed for Username: {username}, Password: {password}. Error: {error_message}")
            return self#next page goes here
        except TimeoutException:
            print("Timeout")
            #self.logger.info(f"Login successful for Username: {username}, Password: {password}.")
            return UserHomePage(self.driver)


    def dismiss_invalid_credentials_error(self):
        self.element_click(self.authenticationPageLocators.error_okay_locator)
        return self


    def login_to_site(self, email, password):
        self.enter_email(email)
        time.sleep(2)
        self.enter_password(password)
        time.sleep(2)
        self.click_login_button()
        return UserHomePage(self.driver)


    def login_to_site_invalid(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.dismiss_invalid_credentials_error()
        return self

    def signup_and_login_to_site(self, username, password, email):
        self.click_switch_mode()
        self.enter_username(username)
        self.enter_password(password)
        self.enter_email(email)
        return self.click_signup_button()

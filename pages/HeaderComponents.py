
from locators.header_locators import HeaderLocators
from pages.BasePage import BasePage

class HeaderComponent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.headerLocators = HeaderLocators()

    def navigate_authenticate(self):
        from pages.BaseballAuthenticatePage import AuthenticationPage
        self.element_click(self.headerLocators.authenticate_locator)
        return AuthenticationPage(self.driver)


    def navigate_userlink(self):
        from pages.UserHomePage import UserHomePage
        self.element_click(self.headerLocators.user_link_locator)
        return UserHomePage(self.driver)

    def navigate_mycards(self):
        from pages.MyCardsPage import MyCardsPage
        self.element_click(self.headerLocators.my_cards_link_locator)
        return MyCardsPage(self.driver)


    def navigate_addcard(self):
        from pages.AddCardPage import AddCardPage  # Lazy import to avoid circular dependency
        self.element_click(self.headerLocators.add_card_link_locator)
        return AddCardPage(self.driver)

    def navigate_cardsummary(self):
        from pages.CardSummaryPage import CardSummaryPage  # Lazy import to avoid circular dependency
        self.element_click(self.headerLocators.card_summary_link_locator)
        return CardSummaryPage(self.driver)

    def navigate_gradedcardsummary(self):
        from pages.GradedCardSummaryPage import GradedCardSummaryPage  # Lazy import to avoid circular dependency
        self.element_click(self.headerLocators.graded_card_summary_link_locator)
        return GradedCardSummaryPage(self.driver)

    def navigate_logout(self):
        from pages.CardCatalogHomePage import CardCatalogHome  # Lazy import to avoid circular dependency
        self.element_click(self.headerLocators.logout_link_locator)
        return CardCatalogHome(self.driver)

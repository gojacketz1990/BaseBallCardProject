import time

from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
import pytest


class TestCardCatalogHome(BaseTests):

    def test_cardcatalog(self):

        log = self.getLogger()
        cardcataloghome = CardCatalogHome(self.driver)

        cardcataloghome.click_authenticate()
        time.sleep(5)
        cardcataloghome.click_allusers()
        time.sleep(5)
        cardcataloghome.click_cardcatalogHome()
        time.sleep(5)

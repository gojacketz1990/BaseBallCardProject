import random
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv

class TestUserHomePage(BaseTests):
    def test_random_mycard_form(self):
        log = self.getLogger()
        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.click_authenticate()

        userHomePage = authenticationPage.login_to_site('gojacketz@gmail.com', 'reapit')



        file_path = '../TestData/AddCardValidation.csv'
        data = read_csv(file_path)

        for row in data:
            addCardPage = userHomePage.click_addCard()
            fake = Faker()
            fake_name = fake.name()
            fake_address = fake.address()
            random_number = random.randint(1000, 9999)
            random_cert_number = random.randint(100000, 999999)

            sportchoices = ["Baseball", "Football", "Basketball"]
            random_sport = random.choice(sportchoices)

            print(fake_name)
            print(random_number)

            description = fake_name + "\n" + fake_address

            choices = ["Bo.jpg", "fermin.jpeg", "hogan.jpeg", "Skenes.jpeg", "trout.jpeg"]
            random_choice = random.choice(choices)

            userHomePage = addCardPage.addCardFormValidation(
                sport=row.get('Sport'),
                cardname=fake_name,
                cardnumber=random_number,
                cardcompany=row.get('CardCompany'),
                cardrelease=row.get('CardRelease'),
                isParallel=False,
                paralleltype="",
                isInsert=False,
                inserttype="",
                isGraded=False,
                gradecompany="",
                grade="",
                certnumber="",
                isRelic=False,
                isAuto=False,
                filePath="",
                description="",
                year="2023",
                expectedState=True
            )

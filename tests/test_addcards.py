import random
import pytest
from faker import Faker
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv
import configparser

# Load CSV data as a class attribute
file_path = '../TestData/AddCardValidation.csv'
csv_data = read_csv(file_path)  # Returns a list of dictionaries
# Create a list of tuples: (row, test_id)
test_cases = [(row, row['TestName']) for row in csv_data]

@pytest.mark.usefixtures("setup_and_teardown")  # Ensure setup from BaseTests is applied
class TestUserHomePage(BaseTests):

    @pytest.mark.parametrize("row", csv_data, ids=lambda row: row['TestName'])
    def test_random_mycard_form(self, row, request):
        # Store description in request.node for later use
        #request.node.description = row.get('description', 'No description provided')

        #request.node.description = row.get('description','No description provided')
        request.node.user_properties = {"Description": row.get('description', 'N/A')} #Change MyNewColumn to the name of your new column.

        print(request.node.user_properties)

        test_name = row.get('TestName')
        print(f"Running Test: {test_name}")

        log = self.getLogger()
        cardCatalogHome = CardCatalogHome(self.driver)

        authenticationPage = cardCatalogHome.header.navigate_authenticate()

        userHomePage = authenticationPage.login_to_site(self.username, self.password)

        addCardPage = userHomePage.header.navigate_addcard()
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

        use_file = row.get('file').strip().lower() == 'true'
        filePath = '/Users/gojacketz/PycharmProjects/BaseballCardProject/TestData/' + random_choice if use_file else ""

        addCardPage.addCard(
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
            isnumbered='',
            number="",
            numberoutof='',
            certnumber="",
            isRelic=False,
            isAuto=False,
            file=filePath,
            notes="",
            year="2023",
        )


        addCardPage.addCardScreenshot(test_name+"_add_card.png")

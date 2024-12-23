import random
from faker import Faker
import pytest
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv

from faker import Faker
import pytest
from utilities.BaseTests import BaseTests
from pages.CardCatalogHomePage import CardCatalogHome
from utilities.csv_utils import read_csv


# Load CSV data as a class attribute
file_path = '../TestData/UpdateCardValidation.csv'
csv_data = read_csv(file_path)  # Returns a list of dictionaries

# Create a list of tuples: (row, test_id)
test_cases = [(row, row['cardname']) for row in csv_data]

#pytest --html=report.html --self-contained-html

@pytest.mark.usefixtures("setup_and_teardown")  # Ensure setup from BaseTests is applied
class TestUserHomePage(BaseTests):


    @pytest.mark.parametrize("row", csv_data, ids=lambda row: row['cardname'])
    def test_update_card_form(self, row, request):
        # Attach testdescription from the CSV file to the test node
        request.node._description = row.get('description', 'No description provided')

        test_name = row.get('cardname')
        print(f"Running Test: {test_name}")

        log = self.getLogger()
        cardCatalogHome = CardCatalogHome(self.driver)
        authenticationPage = cardCatalogHome.click_authenticate()
        userHomePage = authenticationPage.login_to_site('gojacketz@icloud.com', 'reapit')
        myCardPage = userHomePage.click_mycards()

        updateCardPage = myCardPage.editCard(row.get('cardname'))

        # Generate fake data
        fake = Faker()
        fake_name = fake.name()
        fake_address = fake.address()
        random_number = random.randint(1000, 9999)

        # Generate notes using Faker
        generated_notes = fake_name + "\n" + fake_address

        # Safely get the value of 'notes' from the CSV and default to empty if not present
        notes_field = row.get('notes', '').strip().lower()  # Default to empty string if 'notes' is missing

        # Determine the final value for notes
        notes = generated_notes if notes_field == 'true' else ''

        choices = ["Bo.jpg", "fermin.jpeg", "hogan.jpeg", "Skenes.jpeg", "trout.jpeg"]
        random_choice = random.choice(choices)

        use_file = row.get('file').strip().lower() == 'true'
        filePath = '/Users/gojacketz/PycharmProjects/BaseballCardProject/TestData/' + random_choice if use_file else ""

        updateCardPage.updateCardAllFields(
            sport=row.get('Sport'),
            cardname = f"{row.get('cardname')} - Updated",
            cardnumber=row.get('cardname'),
            cardcompany=row.get('CardCompany'),
            cardrelease=row.get('CardRelease'),
            isParallel=row.get('Parallel').strip().lower() == 'true',
            paralleltype=row.get('ParallelType'),
            isInsert=row.get('Insert').strip().lower() == 'true',
            inserttype=row.get('InsertType'),
            isGraded=row.get('isGraded').strip().lower() == 'true',
            gradecompany=row.get('GradeCompany'),
            grade=row.get('Grade'),
            certnumber=row.get('Certnumber'),
            isRelic=row.get('Relic').strip().lower() == 'true',
            isAuto=row.get('Auto').strip().lower() == 'true',
            isnumbered=row.get('isnumbered').strip().lower() == 'true',
            number=row.get('number'),
            numberoutof=row.get('numberoutof'),
            notes=notes,
            year=row.get('Year'),
            file=filePath,
            expectedstate=row.get('expectedState').strip().lower() == 'true'
        )

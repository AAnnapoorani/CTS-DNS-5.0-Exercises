from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InputFormPage(BasePage):

    # ==================================================
    # LOCATORS
    # ==================================================

    # Current TestMu AI page uses placeholder attributes
    # reliably for the form input fields.

    NAME = (
        By.CSS_SELECTOR,
        "input[placeholder='Name']"
    )

    EMAIL = (
        By.CSS_SELECTOR,
        "input[placeholder='Email']"
    )

    PASSWORD = (
        By.CSS_SELECTOR,
        "input[placeholder='Password']"
    )

    COMPANY = (
        By.CSS_SELECTOR,
        "input[placeholder='Company']"
    )

    WEBSITE = (
        By.CSS_SELECTOR,
        "input[placeholder='Website']"
    )

    COUNTRY = (
        By.TAG_NAME,
        "select"
    )

    CITY = (
        By.CSS_SELECTOR,
        "input[placeholder='City']"
    )

    ADDRESS1 = (
        By.CSS_SELECTOR,
        "input[placeholder='Address 1']"
    )

    ADDRESS2 = (
        By.CSS_SELECTOR,
        "input[placeholder='Address 2']"
    )

    STATE = (
        By.CSS_SELECTOR,
        "input[placeholder='State']"
    )

    ZIP = (
        By.CSS_SELECTOR,
        "input[placeholder='Zip code']"
    )

    SUBMIT = (
        By.XPATH,
        "//button[normalize-space()='Submit']"
    )

    # ==================================================
    # FORM METHODS
    # ==================================================

    def fill_form(
        self,
        name,
        email,
        password,
        company,
        website,
        city,
        address1,
        address2,
        state,
        zip_code
    ):

        self.enter_text(self.NAME, name)

        self.enter_text(self.EMAIL, email)

        self.enter_text(self.PASSWORD, password)

        self.enter_text(self.COMPANY, company)

        self.enter_text(self.WEBSITE, website)

        self.enter_text(self.CITY, city)

        self.enter_text(self.ADDRESS1, address1)

        self.enter_text(self.ADDRESS2, address2)

        self.enter_text(self.STATE, state)

        self.enter_text(self.ZIP, zip_code)

    # ==================================================
    # COUNTRY DROPDOWN
    # ==================================================

    def select_country(self, country):

        country_element = self.wait_for_element(
            self.COUNTRY
        )

        dropdown = Select(country_element)

        dropdown.select_by_visible_text(country)

    # ==================================================
    # SUBMIT FORM
    # ==================================================

    def submit_form(self):

        self.click(self.SUBMIT)
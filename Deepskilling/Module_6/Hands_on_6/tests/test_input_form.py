import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from pages.input_form_page import InputFormPage


def test_input_form():

    # ==================================================
    # BROWSER SETUP
    # ==================================================

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()

    try:

        # ==============================================
        # OPEN INPUT FORM PAGE
        # ==============================================

        driver.get(
            "https://www.testmuai.com/"
            "selenium-playground/input-form-demo/"
        )

        page = InputFormPage(driver)

        # ==============================================
        # FILL FORM
        # ==============================================

        page.fill_form(

            name="Annapoorani",

            email="annapoorani@test.com",

            password="Password@123",

            company="Cognizant",

            website="https://www.cognizant.com",

            city="Chennai",

            address1="GST Road",

            address2="Tambaram",

            state="Tamil Nadu",

            zip_code="600045"
        )

        print(
            "✓ All form fields filled successfully"
        )

        # ==============================================
        # SELECT COUNTRY
        # ==============================================

        page.select_country(
            "India"
        )

        print(
            "✓ Country selected successfully"
        )

        # ==============================================
        # CREATE SCREENSHOT FOLDER
        # ==============================================

        os.makedirs(
            "screenshots",
            exist_ok=True
        )

        # Screenshot before submission

        driver.save_screenshot(
            "screenshots/form_filled.png"
        )

        print(
            "✓ Form filled screenshot saved"
        )

        # ==============================================
        # SUBMIT FORM
        # ==============================================

        page.submit_form()

        print(
            "✓ Submit button clicked successfully"
        )

        time.sleep(2)

        # Screenshot after submission

        driver.save_screenshot(
            "screenshots/form_submission.png"
        )

        print(
            "✓ Form submission screenshot saved"
        )

    finally:

        # Browser will close even if the test fails.

        driver.quit()
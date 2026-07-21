import os
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.input_form_page import InputFormPage


def test_data_driven():

    # Read CSV file
    data = pd.read_csv("test_data/input_data.csv")

    # Create screenshots folder
    os.makedirs("screenshots", exist_ok=True)

    # Execute test for each record
    for index, row in data.iterrows():

        print(f"\n========== Executing Test {index + 1} ==========\n")

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

        driver.maximize_window()

        try:

            driver.get(
                "https://www.testmuai.com/selenium-playground/input-form-demo/"
            )

            page = InputFormPage(driver)

            # Fill Form
            page.fill_form(

                name=row["name"],

                email=row["email"],

                password=row["password"],

                company=row["company"],

                website=row["website"],

                city=row["city"],

                address1=row["address1"],

                address2=row["address2"],

                state=row["state"],

                zip_code=str(row["zip"])
            )

            # Select Country
            page.select_country(row["country"])

            print(f"✓ Form Filled for {row['name']}")

            # Screenshot before submit
            driver.save_screenshot(
                f"screenshots/{row['name']}_filled.png"
            )

            # Submit Form
            page.submit_form()

            print("✓ Form Submitted")

            time.sleep(2)

            # Screenshot after submit
            driver.save_screenshot(
                f"screenshots/{row['name']}_submitted.png"
            )

            print("✓ Screenshot Saved")

        finally:

            driver.quit()

    print("\n========== ALL TESTS COMPLETED ==========")
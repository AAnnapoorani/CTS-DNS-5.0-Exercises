from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
wait = WebDriverWait(driver, 15)
driver.get( "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

print("\n========== BOOTSTRAP ALERT DEMO ==========\n")

button = wait.until(
    EC.element_to_be_clickable(( By.XPATH, "//button[contains(text(),'Autoclosable Success Message')]" ))
)

button.click()

print("✓ Success Button Clicked")

try:
    alert = wait.until(
        EC.visibility_of_element_located(
            ( By.XPATH,"//div[contains(@class,'alert') and contains(.,'success')]")
        )
    )

    print("\nAlert Message:")
    print(alert.text)
    print("\n✓ Explicit Wait Passed")
except TimeoutException:
    print("Alert not found.")

print("\n========== time.sleep() ==========\n")

time.sleep(3)
print("Program resumed after 3 seconds.")
print("""
Difference

time.sleep()
--------------
• Waits fixed time.
• Even if element loads early,
  it still waits.

Explicit Wait
--------------
• Waits only until element appears.
• Faster.
• Recommended.
""")

print("\n========== FLUENT WAIT ==========\n")

fluent_wait = WebDriverWait( driver, timeout=20, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])

try:
    fluent_wait.until(
        EC.presence_of_element_located(
            ( By.XPATH, "//button[contains(text(),'Autoclosable Success Message')]" )
        )
    )

    print("✓ Fluent Wait Successful")

except TimeoutException:

    print("Fluent Wait Failed")

driver.quit()
print("\nProgram Executed Successfully.")
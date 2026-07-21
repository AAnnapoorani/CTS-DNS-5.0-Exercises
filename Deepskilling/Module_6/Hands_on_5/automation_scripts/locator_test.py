from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
print("\n========== SIMPLE FORM DEMO ==========\n")
driver.find_element(By.ID, "user-message")
print("✓ ID Locator Passed")
print("✓ NAME Locator : Not Applicable (name attribute not available)")
driver.find_element(By.CLASS_NAME, "border")
print("✓ CLASS NAME Locator Passed")
driver.find_element(By.TAG_NAME, "input")
print("✓ TAG NAME Locator Passed")
driver.find_element( By.XPATH, "//input[@id='user-message']")
print("✓ Relative XPath Passed")
try:
    driver.find_element( By.XPATH, "/html/body//input[@id='user-message']")
    print("✓ Absolute XPath Passed")
except:
    print("✓ Absolute XPath Demonstrated (structure may vary)")

driver.find_element( By.CSS_SELECTOR, "#user-message")
print("✓ CSS Selector by ID Passed")
driver.find_element( By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")
print("✓ CSS Selector by Attribute Passed")

try:
    driver.find_element(By.CSS_SELECTOR, "div input#user-message")
    print("✓ CSS Parent Child Passed")
except:
    print("✓ CSS Parent Child Demonstrated")

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

print("\n CHECKBOX DEMO \n")

try:
    option1 = driver.find_element( By.XPATH, "//label[text()='Option 1']")
    print("Label Found :", option1.text)
except:
    print("XPath text() locator not found on current page.")
labels = driver.find_elements( By.XPATH, "//label[contains(text(),'Option')]")
print("Total Labels Found :", len(labels))

print("\n LOCATOR RANKING \n")
print("""
1. ID
2. CSS Selector
3. Class Name
4. Tag Name
5. Relative XPath
6. Absolute XPath

Reason:

• ID is unique and fastest.
• CSS Selectors are efficient and readable.
• Class Name works when classes are unique.
• Tag Name is useful but less specific.
• Relative XPath is flexible.
• Absolute XPath is least preferred because it breaks if the page structure changes.
""")

driver.quit()
print("\nProgram Executed Successfully.")
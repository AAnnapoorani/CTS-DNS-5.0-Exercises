"""
Hands-On 4 – Task 1

Selenium Components:

1. WebDriver
   - Acts as a bridge between Selenium scripts and browsers.
   - Sends commands to the browser and receives responses.

2. Selenium Grid
   - Allows tests to run on multiple browsers and machines simultaneously.
   - Useful for parallel execution and cross-browser testing.

3. Selenium IDE
   - Browser extension used for record-and-playback testing.
   - Generates automation scripts quickly.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:", driver.title)

driver.quit()
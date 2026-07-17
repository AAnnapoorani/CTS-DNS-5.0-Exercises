from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

# Open Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Open Simple Form Demo
driver.find_element(
    By.LINK_TEXT,
    "Simple Form Demo"
).click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("URL Verification Passed")

# Go Back
driver.back()

# Open New Tab
driver.execute_script(
    'window.open("https://www.google.com");'
)

# Display handles
print("Window Handles:", driver.window_handles)

# Switch to Google tab
driver.switch_to.window(
    driver.window_handles[1]
)

print("Google Title:", driver.title)

# Return to Playground
driver.switch_to.window(
    driver.window_handles[0]
)

# Screenshot
driver.save_screenshot(
    "playground_screenshot.png"
)

print("Screenshot Saved")

# Window size
print("Current Size:",
      driver.get_window_size())

driver.set_window_size(
    1280,
    800
)

print("New Size:",
      driver.get_window_size())

driver.quit()
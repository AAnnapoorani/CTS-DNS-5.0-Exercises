# Module 6: Selenium WebDriver Automation Testing

## Overview
This module covers web automation and testing using Selenium WebDriver. It demonstrates how to automate browser interactions, write reliable test scripts, implement Page Object Model (POM), and perform data-driven testing.

## Module Structure
```
Module_6/
├── Hands_on_1/              # Selenium basics
├── Hands_on_2/              # Locators and elements
├── Hands_on_3/              # Interactions and actions
├── Hands_on_4/              # Navigation and waits
│   ├── automation_scripts/
│   │   ├── setup_test.py    # Setup test
│   │   └── navigation_test.py
│   └── conftest.py          # Pytest configuration
├── Hands_on_5/              # Waits and synchronization
│   ├── automation_scripts/
│   │   ├── waits_test.py    # Wait strategies
│   │   └── locator_test.py
│   └── conftest.py
├── Hands_on_6/              # Page Object Model (POM)
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_input_form.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py     # Base page class
│   │   └── input_form_page.py
│   └── conftest.py
├── Hands_on_7/              # Data-Driven Testing
│   ├── tests/
│   │   └── test_data_driven.py
│   ├── pages/
│   │   ├── base_page.py
│   │   └── input_form_page.py
│   ├── test_data/
│   │   └── input_data.csv
│   └── conftest.py
└── Output/                  # Screenshots, reports, logs
```

## Topics Covered

### Selenium Fundamentals
- WebDriver API
- Browser instantiation
- Element locating strategies
- Element interactions
- Navigation and waits
- Screenshot and logging
- Exception handling

### Locator Strategies
- ID
- Name
- Class Name
- Tag Name
- CSS Selector
- XPath
- Link Text
- Partial Link Text

### Element Interactions
- Click
- Send keys
- Submit
- Clear
- Select options (dropdown)
- Drag and drop
- Scroll

### Waits and Synchronization
- Implicit waits
- Explicit waits (WebDriverWait)
- Expected conditions
- Fluent waits
- Custom wait conditions

### Page Object Model (POM)
- Base page class
- Page object encapsulation
- Locators management
- Reusable methods
- Test independence

### Data-Driven Testing
- CSV data sources
- Excel data sources
- JSON data sources
- Parameterized tests
- Multiple test scenarios

### Test Framework
- pytest
- Fixtures
- Parametrization
- Test organization
- Reporting

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of web technologies (HTML, CSS)
- Selenium knowledge
- Understanding of OOP concepts
- Familiarity with pytest

### Installation

```bash
# Install required packages
pip install -r requirements.txt

# Verify Selenium installation
python -c "import selenium; print(selenium.__version__)"

# Verify webdriver-manager
python -c "from webdriver_manager.chrome import ChromeDriverManager; print(ChromeDriverManager().install())"
```

### Browser Drivers
The `webdriver-manager` package automatically downloads and manages browser drivers:
- Chrome WebDriver (chromedriver)
- Firefox WebDriver (geckodriver)
- Edge WebDriver (msedgedriver)
- Safari WebDriver (included in Safari)

No manual driver installation needed!

## Usage

### Running Tests

#### Run All Tests
```bash
pytest Hands_on_6/tests/ -v
pytest Hands_on_7/tests/ -v
```

#### Run Specific Test
```bash
pytest Hands_on_6/tests/test_input_form.py -v
pytest Hands_on_6/tests/test_input_form.py::test_form_submission -v
```

#### Run with HTML Report
```bash
pytest Hands_on_6/tests/ -v --html=Output/report.html
```

#### Run with Logging
```bash
pytest Hands_on_6/tests/ -v -s
```

#### Run in Parallel
```bash
pytest Hands_on_6/tests/ -n 4
```

## Selenium Examples

### Basic Browser Automation
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

try:
    # Navigate to website
    driver.get("https://example.com")
    
    # Maximize window
    driver.maximize_window()
    
    # Find element by ID
    element = driver.find_element(By.ID, "element_id")
    
    # Click element
    element.click()
    
    # Send text
    element.send_keys("Hello World")
    
    # Submit form
    element.submit()
    
    # Wait
    time.sleep(2)
    
finally:
    # Close browser
    driver.quit()
```

### Finding Elements
```python
from selenium.webdriver.common.by import By

# Single element
element = driver.find_element(By.ID, "myId")
element = driver.find_element(By.NAME, "myName")
element = driver.find_element(By.CLASS_NAME, "myClass")
element = driver.find_element(By.TAG_NAME, "div")
element = driver.find_element(By.CSS_SELECTOR, ".myClass > p")
element = driver.find_element(By.XPATH, "//div[@id='myId']")
element = driver.find_element(By.LINK_TEXT, "Click Here")

# Multiple elements
elements = driver.find_elements(By.CLASS_NAME, "myClass")

# Within an element
subelement = element.find_element(By.TAG_NAME, "input")
```

### Waits and Expected Conditions
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Explicit wait
wait = WebDriverWait(driver, 10)

# Wait for element to be visible
element = wait.until(
    EC.visibility_of_element_located((By.ID, "myElement"))
)

# Wait for element to be clickable
element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']"))
)

# Wait for presence
element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "notification"))
)

# Custom condition
def custom_condition(driver):
    element = driver.find_element(By.ID, "status")
    return "Success" in element.text

wait.until(custom_condition)
```

### Interactions
```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Action chains
actions = ActionChains(driver)

# Hover
actions.move_to_element(element).perform()

# Drag and drop
source = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")
actions.drag_and_drop(source, target).perform()

# Double click
actions.double_click(element).perform()

# Right click
actions.context_click(element).perform()

# Keyboard
actions.send_keys(Keys.TAB).perform()
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Select dropdown
from selenium.webdriver.support.select import Select
select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_visible_text("Option 1")
select.select_by_value("value1")
select.select_by_index(0)
```

### Scrolling
```python
# Scroll by pixels
driver.execute_script("window.scrollBy(0, 1000)")

# Scroll to element
element = driver.find_element(By.ID, "target")
driver.execute_script("arguments[0].scrollIntoView();", element)

# Scroll to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

### Window and Frame Handling
```python
# Switch to frame
driver.switch_to.frame("frameName")
driver.switch_to.frame(0)  # By index
driver.switch_to.frame(frame_element)  # By element

# Switch back to main content
driver.switch_to.default_content()

# Switch to window
driver.switch_to.window(window_handle)

# Get window handles
handles = driver.window_handles
driver.switch_to.window(handles[1])
```

### Screenshots and Logging
```python
# Take screenshot
driver.save_screenshot("screenshot.png")

# Get logs
driver.get_log("browser")
driver.get_log("driver")
```

## Page Object Model Example

### Base Page Class
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
```

### Page Object
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InputFormPage(BasePage):
    # Locators
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    
    def fill_form(self, name, email):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
    
    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
```

### Test Case
```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.input_form_page import InputFormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()

def test_form_submission(driver):
    page = InputFormPage(driver)
    driver.get("https://example.com/form")
    
    page.fill_form("John Doe", "john@example.com")
    page.submit_form()
    
    message = page.get_success_message()
    assert "Success" in message
```

## Data-Driven Testing Example

### CSV Data File (test_data/input_data.csv)
```csv
name,email,password,country
John Doe,john@example.com,Pass123!,USA
Jane Smith,jane@example.com,Pass456!,UK
Bob Wilson,bob@example.com,Pass789!,Canada
```

### Test with Data-Driven Approach
```python
import pandas as pd
import pytest

@pytest.fixture(params=pd.read_csv("test_data/input_data.csv").iterrows(), 
                ids=lambda x: x[1]['name'])
def test_data(request):
    return request.param[1]

def test_form_with_data(driver, test_data):
    page = InputFormPage(driver)
    driver.get("https://example.com/form")
    
    page.fill_form(
        name=test_data['name'],
        email=test_data['email'],
        password=test_data['password']
    )
    page.select_country(test_data['country'])
    page.submit_form()
    
    assert page.is_success_message_displayed()
```

## Best Practices

1. **Use Page Object Model**: Encapsulate element locators and interactions
2. **Use Explicit Waits**: Avoid hardcoded sleeps, use WebDriverWait
3. **Handle Exceptions**: Use try-finally to ensure driver cleanup
4. **Keep Tests Independent**: Each test should be runnable independently
5. **Use Descriptive Names**: Test names should describe what they test
6. **Avoid Brittle Selectors**: Use ID/Name when available, avoid XPath when possible
7. **Use Fixtures**: Leverage pytest fixtures for setup/teardown
8. **Take Screenshots on Failure**: Capture state when tests fail
9. **Parallel Execution**: Run tests in parallel using pytest-xdist
10. **Meaningful Assertions**: Use clear assertion messages

## Locator Best Practices

### Good Locators (in order of preference)
1. **ID**: `By.ID, "unique_id"`
2. **Name**: `By.NAME, "element_name"`
3. **CSS Selector**: `By.CSS_SELECTOR, "#id"` or `.class-name`
4. **Simple XPath**: `By.XPATH, "//button[@id='submit']"`

### Avoid
- Complex XPath with indexes
- Multiple class names
- Non-unique identifiers
- Brittle relative paths

## Headless Browser Testing
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
```

## Troubleshooting

### Element Not Found
- Verify element exists in DOM
- Use explicit waits
- Check iframe presence
- Verify correct locator

### Stale Element Reference
- Re-find element after page changes
- Use explicit waits
- Avoid storing element references across page loads

### Timeout Issues
- Increase wait timeout
- Check element visibility
- Verify page load completion
- Check for JavaScript execution

### WebDriver Crashes
- Ensure driver cleanup (finally block)
- Check available system memory
- Update ChromeDriver
- Use headless mode for resources

## Output Files
- Screenshots saved in `Output/` directory
- Test reports in `Output/report.html`
- Logs stored in `Output/logs/`

## Test Execution Commands
```bash
# Run all tests with verbose output
pytest -v

# Run with HTML report
pytest --html=report.html

# Run in parallel (4 workers)
pytest -n 4

# Run with specific marker
pytest -m "smoke"

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run last failed
pytest --lf
```

## Learning Objectives
- Automate web browser interactions
- Implement Page Object Model pattern
- Create reliable automated tests
- Handle waits and synchronization
- Perform data-driven testing
- Generate test reports
- Debug test failures
- Optimize test performance

## Further Reading
- Selenium Official Documentation
- Selenium with Python Tutorial
- Test Automation Best Practices
- Page Object Model Guide
- pytest Documentation

## Notes
- Each hands_on builds progressively
- Start with basics in Hands_on_1
- Hands_on_6 introduces POM best practices
- Hands_on_7 demonstrates data-driven approach
- Always use explicit waits instead of time.sleep()
- Run tests frequently during development

## Author
CTS DNS 5.0 Exercises

## License
Educational - Use for learning purposes

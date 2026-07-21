from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

    # Navigate to a URL

    def navigate_to(self, url):

        self.driver.get(url)

    # Get page title

    def get_title(self):

        return self.driver.title

    # Wait until element is visible

    def wait_for_element(
        self,
        locator,
        timeout=15
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(
                locator
            )
        )

    # Enter text into an input field

    def enter_text(
        self,
        locator,
        text
    ):

        element = self.wait_for_element(
            locator
        )

        element.clear()

        element.send_keys(text)

    # Click an element

    def click(
        self,
        locator
    ):

        element = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

        element.click()

    # Get text from an element

    def get_text(
        self,
        locator
    ):

        element = self.wait_for_element(
            locator
        )

        return element.text
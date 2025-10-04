from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_displayed(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.execute_script("window.scrollTo(0, 0);")
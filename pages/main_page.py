from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class MainPage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g')])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    def close_cookie_banner(self):
        try:
            cookie_button = self.find_element(('xpath', "//button[text()='да все привыкли']"), time=3)
            cookie_button.click()
            time.sleep(1)
        except:
            pass

    def click_order_button_top(self):
        self.close_cookie_banner()
        self.find_element(self.ORDER_BUTTON_TOP).click()

    def click_order_button_bottom(self):
        self.close_cookie_banner()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        order_btn = self.find_element(self.ORDER_BUTTON_BOTTOM)
        order_btn.click()

    def click_scooter_logo(self):
        self.find_element(self.SCOOTER_LOGO).click()
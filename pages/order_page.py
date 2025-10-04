from .base_page import BasePage
from .locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_name(self, name):
        self.find_element(self.locators.NAME_FIELD).send_keys(name)

    def fill_surname(self, surname):
        self.find_element(self.locators.SURNAME_FIELD).send_keys(surname)

    # ... остальные методы
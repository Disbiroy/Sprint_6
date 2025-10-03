import pytest
import allure
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.main_page import MainPage


class TestOrder:
    @allure.title("Проверка кнопок заказа")
    @pytest.mark.parametrize("button_type", ["top", "bottom"])
    def test_order_buttons(self, driver, button_type):
        main_page = MainPage(driver)
        main_page.go_to_site()

        if button_type == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        assert "order" in driver.current_url

    @allure.title("Проверка логотипа Самоката")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()

        main_page.click_order_button_top()
        main_page.click_scooter_logo()

        assert driver.current_url == main_page.base_url
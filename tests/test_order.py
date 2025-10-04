import pytest
import allure
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.main_page import MainPage
from urls import Urls


class TestOrder:
    @allure.title("Проверка верхней кнопки заказа")
    def test_top_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_button_top()

        # Проверяем через метод страницы, а не прямое обращение к driver
        assert main_page.is_on_order_page(), "Не произошел переход на страницу заказа"

    @allure.title("Проверка нижней кнопки заказа")
    def test_bottom_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_button_bottom()

        # Проверяем через метод страницы, а не прямое обращение к driver
        assert main_page.is_on_order_page(), "Не произошел переход на страницу заказа"

    @allure.title("Проверка логотипа Самоката")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_button_top()
        main_page.click_scooter_logo()

        # Проверяем через метод страницы, а не прямое обращение к driver
        assert main_page.is_on_main_page(), "Не произошел возврат на главную страницу"
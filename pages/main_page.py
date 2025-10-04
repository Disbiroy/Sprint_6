from .base_page import BasePage
from .locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def close_cookie_banner(self):
        """Закрытие баннера с куками с явным ожиданием"""
        try:
            cookie_button = self.find_clickable_element(self.locators.COOKIE_BANNER, time=3)
            cookie_button.click()
            # Ждем исчезновения баннера вместо sleep
            self.wait_for_element_to_disappear(self.locators.COOKIE_BANNER, time=3)
        except:
            # Если баннера нет или он уже закрыт - просто продолжаем
            pass

    def click_order_button_top(self):
        """Клик по верхней кнопке заказа"""
        self.close_cookie_banner()
        self.click_element(self.locators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        """Клик по нижней кнопке заказа"""
        self.close_cookie_banner()
        # Скролл к нижней кнопке вместо скролла до конца страницы
        order_btn = self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        # Ждем пока кнопка станет кликабельной после скролла
        order_btn = self.find_clickable_element(self.locators.ORDER_BUTTON_BOTTOM)
        order_btn.click()

    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(self.locators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_element(self.locators.YANDEX_LOGO)

    def click_question(self, question_number):
        """Клик по вопросу по номеру (1-8)"""
        question_locator = getattr(self.locators, f"QUESTION_{question_number}")
        self.click_element(question_locator)

    def get_answer_text(self, answer_number):
        """Получение текста ответа по номеру (1-8)"""
        answer_locator = getattr(self.locators, f"ANSWER_{answer_number}")
        return self.find_visible_element(answer_locator).text

    def wait_for_answer_to_appear(self, answer_number):
        """Ожидание появления ответа"""
        answer_locator = getattr(self.locators, f"ANSWER_{answer_number}")
        return self.find_visible_element(answer_locator)

    def is_on_order_page(self):
        """Проверка, что находимся на странице заказа"""
        return self.is_on_page(Urls.ORDER_PAGE)

    def is_on_main_page(self):
        """Проверка, что находимся на главной странице"""
        return self.is_on_page(Urls.MAIN_PAGE) or self.get_current_url() == Urls.MAIN_PAGE
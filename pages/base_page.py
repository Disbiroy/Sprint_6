from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.BASE_URL
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator, time=10):
        """Поиск элемента с ожиданием"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable_element(self, locator, time=10):
        """Поиск кликабельного элемента"""
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )

    def find_visible_element(self, locator, time=10):
        """Поиск видимого элемента"""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_disappear(self, locator, time=10):
        """Ожидание исчезновения элемента"""
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator)
        )

    def go_to_site(self):
        """Переход на базовый URL"""
        return self.driver.get(self.base_url)

    def scroll_to_element(self, locator):
        """Скролл к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def scroll_to_bottom(self):
        """Скролл вниз страницы"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """Скролл вверх страницы"""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def click_element(self, locator):
        """Клик по элементу"""
        element = self.find_clickable_element(locator)
        element.click()

    def wait_for_page_load(self, time=10):
        """Ожидание загрузки страницы"""
        return WebDriverWait(self.driver, time).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    def is_on_page(self, expected_url):
        """Проверка, что находимся на ожидаемой странице"""
        current_url = self.get_current_url()
        return expected_url in current_url

    def wait_for_url_change(self, previous_url, timeout=10):
        """Ожидание изменения URL"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url != previous_url
        )
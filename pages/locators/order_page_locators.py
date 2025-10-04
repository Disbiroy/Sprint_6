from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы заказа"""

    # Поля формы
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопки
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
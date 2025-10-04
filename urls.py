class Urls:
    """Класс для хранения всех URL проекта"""

    # Основные URL
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    MAIN_PAGE = BASE_URL
    ORDER_PAGE = f"{BASE_URL}order"

    # API endpoints (если нужны)
    API_BASE = "https://qa-scooter.praktikum-services.ru/api/v1/"
    CREATE_COURIER = f"{API_BASE}courier"
    LOGIN_COURIER = f"{API_BASE}courier/login"
    CREATE_ORDER = f"{API_BASE}orders"

    # Другие страницы
    TRACK_ORDER = f"{BASE_URL}track"
    FAQ_PAGE = f"{BASE_URL}faq"
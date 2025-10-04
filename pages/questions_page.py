from selenium.webdriver.common.by import By
from .base_page import BasePage


class QuestionsPage(BasePage):
    def get_question_locator(self, question_number):
        return (By.ID, f"accordion__heading-{question_number}")

    def get_answer_locator(self, question_number):
        return (By.ID, f"accordion__panel-{question_number}")

    def click_question(self, question_number):
        question_locator = self.get_question_locator(question_number)
        self.click_element(question_locator)

    def get_answer_text(self, question_number):
        answer_locator = self.get_answer_locator(question_number)
        return self.get_element_text(answer_locator)

    def is_answer_displayed(self, question_number):
        answer_locator = self.get_answer_locator(question_number)
        return self.is_element_displayed(answer_locator)

    def scroll_to_questions(self):
        self.scroll_to_bottom()

    # Дополнительный метод для скролла к конкретному вопросу
    def scroll_to_question(self, question_number):
        question_locator = self.get_question_locator(question_number)
        self.scroll_to_element(question_locator)
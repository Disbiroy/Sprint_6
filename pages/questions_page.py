from selenium.webdriver.common.by import By
from .base_page import BasePage


class QuestionsPage(BasePage):
    def click_question(self, question_number):
        question_locator = (By.ID, f"accordion__heading-{question_number}")
        self.find_element(question_locator).click()

    def get_answer_text(self, question_number):
        answer_locator = (By.ID, f"accordion__panel-{question_number}")
        return self.find_element(answer_locator).text

    def is_answer_displayed(self, question_number):
        answer_locator = (By.ID, f"accordion__panel-{question_number}")
        return self.find_element(answer_locator).is_displayed()

    def scroll_to_questions(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
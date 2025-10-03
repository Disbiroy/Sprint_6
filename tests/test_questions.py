import pytest
import allure
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.main_page import MainPage
from pages.questions_page import QuestionsPage


class TestQuestions:
    @allure.title("Проверка вопросов о важном")
    @pytest.mark.parametrize("question_id", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_questions_dropdown(self, driver, question_id):
        main_page = MainPage(driver)
        questions_page = QuestionsPage(driver)

        main_page.go_to_site()
        questions_page.scroll_to_questions()
        questions_page.click_question(question_id)

        assert questions_page.is_answer_displayed(question_id)
        answer_text = questions_page.get_answer_text(question_id)
        assert answer_text and len(answer_text) > 0
import pytest
import allure
from data import Answers


class TestMainPage:
    @allure.title('Тестируем вопрос-ответ')
    @pytest.mark.parametrize('q_num, expected_result',
                             [(0, Answers.ANSWER_Q_0),
                              (1, Answers.ANSWER_Q_1),
                              (2, Answers.ANSWER_Q_2),
                              (3, Answers.ANSWER_Q_3),
                              (4, Answers.ANSWER_Q_4),
                              (5, Answers.ANSWER_Q_5),
                              (6, Answers.ANSWER_Q_6),
                              (7, Answers.ANSWER_Q_7)])
    def test_questions_and_answer(self, main_page, q_num, expected_result):
        main_page.click_on_cookie()
        main_page.scroll_page_to_last_qestion()
        result = main_page.click_to_question_get_answer_text(q_num)
        assert result == expected_result

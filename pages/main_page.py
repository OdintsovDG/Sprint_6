import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Соглашаемся на использование куки')
    def click_on_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE)

    @allure.step('Прокручиваем страницу до последнего вопроса')
    def scroll_page_to_last_qestion(self):
        self.scroll_page(MainPageLocators.QUESTION_LAST)

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, num):
        question_loc = self.extraction_locator(MainPageLocators.QUESTION, num)
        self.click_on_element(question_loc)

    @allure.step('Получаем текст ответа')
    def get_text_from_answer(self, num):
        answer_loc = self.extraction_locator(MainPageLocators.ANSWER, num)
        return self.get_text_from_element(answer_loc)

    @allure.step('Кликаем на вопрос и получаем текст ответа')
    def click_to_question_get_answer_text(self, num):
        self.click_on_question(num)
        return self.get_text_from_answer(num)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_on_order_button(self, button):
        self.click_on_element(button)

import allure
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage


class SwitchPage(BasePage):

    @allure.step('Кликаем на лого Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(SwitchPageLocators.YANDEX_LOGO)

    @allure.step('Кликаем на лого Самокат')
    def click_on_logo_scooter(self):
        self.click_on_element(SwitchPageLocators.SCOOTER_LOGO)

    @allure.step('Находим кнопку "Найти" на главной странице Яндекса')
    def search_find_button(self):
        self.switch_to_another_window()
        self.find_element_with_wait(SwitchPageLocators.FIND_BUTTON)
        return self.get_text_from_element(SwitchPageLocators.FIND_BUTTON)

    @allure.step('Находим текст согласия на использование куки на домашней странице Самоката')
    def check_home_page(self):
        self.find_element_with_wait(SwitchPageLocators.COOKIE_HOME_PAGE)
        return self.get_text_from_element(SwitchPageLocators.COOKIE_HOME_PAGE)

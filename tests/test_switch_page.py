import allure
import data


class TestSwitchPage:

    @allure.step('Проверяем открытие в новом окне домашней страницы Яндекса, при нажатии на лого Яндекса')
    def test_click_on_yandex_logo_and_open_dzen(self, switch_page,):
        switch_page.get_url(data.MAIN_URL)
        switch_page.click_on_logo_yandex()
        result = switch_page.search_find_button()
        assert result == data.find_button_text

    @allure.step('Проверяем возвращение на главную страницу Самоката, при нажатии на лого Самоката')
    def test_click_on_scooter_logo_and_open_home_page(self, switch_page):
        switch_page.get_url(data.ORDER_URL)
        switch_page.click_on_logo_scooter()
        result = switch_page.check_home_page()
        assert result == data.cookie_text

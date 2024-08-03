import allure
import pytest
from locators.main_page_locators import MainPageLocators


class TestOrderPage:
    @allure.step('Тестируем позитивный сценарий заказа самоката. Две даты.')
    @pytest.mark.parametrize('button, date',
                             [
                                 [MainPageLocators.ORDER_BUTTON_HEADER, '10.08.2024'],
                                 [MainPageLocators.ORDER_BUTTON_FOOTER, '11.09.2024']
                             ]
                             )
    def test_order_scooter(self, main_page, order_page, button, date):
        main_page.click_on_cookie()
        main_page.click_on_order_button(button)
        order_page.set_personal_data_for_order()
        order_page.click_further_button()
        order_page.set_order_info(date)
        order_page.click_on_order_and_confirm_button()
        assert order_page.check_order_is_done()

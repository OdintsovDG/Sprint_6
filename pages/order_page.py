import allure
import helpers
from data import DataForOrder
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим имя')
    def set_name(self):
        name = helpers.generate_name()
        self.set_text_to_element(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Вводим фамилию')
    def set_surname(self):
        surname = helpers.generate_surname()
        self.set_text_to_element(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step('Вводим адрес доставки')
    def set_address(self):
        address = helpers.generate_address()
        self.set_text_to_element(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self):
        metro_station = helpers.generate_station()
        self.click_on_element(OrderPageLocators.INPUT_METRO_STATION)
        locator = self.extraction_locator(OrderPageLocators.STATION, metro_station)
        self.click_on_element(locator)

    @allure.step('Вводим номер телефона')
    def set_phone(self):
        phone = helpers.generate_phone()
        self.set_text_to_element(OrderPageLocators.INPUT_PHONE, phone)

    @allure.step('Вводим персональные данные для заказа')
    def set_personal_data_for_order(self):
        self.set_name()
        self.set_surname()
        self.set_address()
        self.select_metro_station()
        self.set_phone()

    @allure.step('Нажимаем кнопку "Далее"')
    def click_further_button(self):
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    @allure.step('Выбираем дату доставки самоката')
    def set_date(self, date):
        self.set_text_to_element(OrderPageLocators.INPUT_DATE, date)
        self.click_on_element(OrderPageLocators.TITLE)

    @allure.step('Выбираем срок аренды самоката')
    def select_rental_period(self):
        rental_period = helpers.generate_rental_period()
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_POPUP)
        locator = self.extraction_locator(OrderPageLocators.RENTAL_PERIOD_SELECT, rental_period)
        self.click_on_element(locator)

    @allure.step('Выбираем цвет самоката')
    def select_color(self):
        color = helpers.generate_color()
        locator = self.extraction_locator(OrderPageLocators.INPUT_COLOR, color)
        self.click_on_element(locator)

    @allure.step('Вводим комментарий')
    def set_comment(self):
        comment = helpers.generate_comment()
        self.set_text_to_element(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step('Вводим информацию о заказе')
    def set_order_info(self, date):
        self.set_date(date)
        self.select_rental_period()
        self.select_color()
        self.set_comment()

    @allure.step('Нажимаем кнопку "Заказать" и  подтверждаем заказ')
    def click_on_order_and_confirm_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверяем факт оформления заказа')
    def check_order_is_done(self):
        result = self.get_text_from_element(OrderPageLocators.ORDER_STATUS_BUTTON)
        return result == DataForOrder.result_order_is_done

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:

    @allure.step('Подгружаем драйвер в конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Ищем элемент на странице с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Вводим текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Прокручиваем страницу')
    def scroll_page(self, locator):
        question = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question)

    @allure.step('Извлекаем части локатора и преобразовываем')
    def extraction_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return method, locator

    @allure.step('Находим новое окно браузера')
    def switch_to_another_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

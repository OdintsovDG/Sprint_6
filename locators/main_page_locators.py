from selenium.webdriver.common.by import By


class MainPageLocators:
    # Вопрос
    QUESTION = By.XPATH, '//div[@id = "accordion__heading-{}"]'
    # Последний вопрос
    QUESTION_LAST = By.XPATH, '//div[@id = "accordion__heading-7"]'
    # Ответ
    ANSWER = By.XPATH, '//div[@id = "accordion__panel-{}"]'
    # Кнопка принять куки
    COOKIE = By.XPATH, '//button[text() = "да все привыкли"]'
    # Кнопка "Заказать" в шапке страницы
    ORDER_BUTTON_HEADER = By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'
    # Кнопка "Заказать" в футере страницы
    ORDER_BUTTON_FOOTER = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'

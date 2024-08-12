from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поле "Имя"
    INPUT_NAME = By.XPATH, '//*[@placeholder="* Имя"]'
    # Поле "Фамилия"
    INPUT_SURNAME = By.XPATH, '//*[@placeholder="* Фамилия"]'
    # Поле "Адрес"
    INPUT_ADDRESS = By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]'
    # Поле "Станция метро"
    INPUT_METRO_STATION = By.XPATH, '//*[@placeholder="* Станция метро"]'
    # Выпадающий список станций
    STATION = By.XPATH, '//*[text()="{}"]'
    # Поле "Телефон"
    INPUT_PHONE = By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]'
    # Кнопка "Далее"
    FURTHER_BUTTON = By.XPATH, '//button[text()="Далее"]'
    # Поле "Дата"
    INPUT_DATE = By.XPATH, '//*[@placeholder="* Когда привезти самокат"]'
    # Поле "Срок аренды"
    RENTAL_PERIOD_POPUP = By.XPATH, '//div[@class="Dropdown-control"]'
    # Выпадающий список "Срок аренды"
    RENTAL_PERIOD_SELECT = By.XPATH, '//*[text()="{}"]'
    # Поле "Выбор цвета"
    INPUT_COLOR = By.XPATH, '//*[@id="{}"]'
    # Поле "Комментарий"
    INPUT_COMMENT = By.XPATH, '//*[@placeholder="Комментарий для курьера"]'
    # Кнопка "Заказать"
    ORDER_BUTTON_MIDDLE = By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Заказать"]'
    # Кнопка подтверждения заказа
    CONFIRM_BUTTON = By.XPATH, '//button[text()="Да"]'
    # Кнопка перехода к просмотру статуса заказа
    ORDER_STATUS_BUTTON = By.XPATH, '//button[text()="Посмотреть статус"]'
    # Локатор заголовка
    TITLE = By.XPATH, '//*[text()="Про аренду"]'

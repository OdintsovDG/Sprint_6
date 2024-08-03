from selenium.webdriver.common.by import By


class SwitchPageLocators:

    YANDEX_LOGO = By.XPATH, '//*[@href = "//yandex.ru"]'
    FIND_BUTTON = By.XPATH, '//*[text() = "Найти"]'
    SCOOTER_LOGO = By.XPATH, '//*[contains(@class, "Header_LogoScooter")]'
    COOKIE_HOME_PAGE = By.XPATH, '//*[text()="И здесь куки! В общем, мы их используем."]'

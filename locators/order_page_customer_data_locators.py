from selenium.webdriver.common.by import By


class CustomerDataFormLocators:
    HEADER_FOR_WHOM_SCOOTER = (By.CLASS_NAME, 'Order_Header__BZXOb')
    NAME_INPUT_CONTAINER = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT_CONTAINER = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT_CONTAINER = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    SUBWAY_STATION_SELECT_SEARCH = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    BOULVAR_ROKOSSOVSKOGO_MENU_ITEM = (By.XPATH, '//li[@data-value="1"]')
    PHONE_INPUT_CONTAINER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    FURTHER_BUTTON = (By.XPATH, '//button[text()="Далее"]')

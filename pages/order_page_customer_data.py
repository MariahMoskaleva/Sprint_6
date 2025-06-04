from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_customer_data_locators import CustomerDataFormLocators


class OrderPageCustomerData:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page_customer_data(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(CustomerDataFormLocators.HEADER_FOR_WHOM_SCOOTER))

    def set_name(self, name):
        self.driver.find_element(*CustomerDataFormLocators.NAME_INPUT_CONTAINER).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*CustomerDataFormLocators.SURNAME_INPUT_CONTAINER).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*CustomerDataFormLocators.ADDRESS_INPUT_CONTAINER).send_keys(address)

    def select_subway_station(self):
        self.driver.find_element(*CustomerDataFormLocators.SUBWAY_STATION_SELECT_SEARCH).click()
        self.driver.find_element(*CustomerDataFormLocators.BOULVAR_ROKOSSOVSKOGO_MENU_ITEM).click()

        # Явное ожидание, пока кнопка "Далее" станет доступна (вместо invisibility_of_element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(CustomerDataFormLocators.FURTHER_BUTTON)
        )

    def set_phone_number(self, phone):
        self.driver.find_element(*CustomerDataFormLocators.PHONE_INPUT_CONTAINER).send_keys(phone)

    def go_further(self):
        self.driver.find_element(*CustomerDataFormLocators.FURTHER_BUTTON).click()

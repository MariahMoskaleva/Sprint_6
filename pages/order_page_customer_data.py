import allure
from locators.order_page_customer_data_locators import CustomerDataFormLocators
from pages.base_page import BasePage


class OrderPageCustomerData(BasePage):

    @allure.step("Ожидание загрузки страницы ввода данных клиента")
    def wait_for_load(self):
        self.wait_for_element_visibility(CustomerDataFormLocators.HEADER_FOR_WHOM_SCOOTER)

    @allure.step("Ввод имени: {name}")
    def set_name(self, name):
        self.send_keys(CustomerDataFormLocators.NAME_INPUT_CONTAINER, name)

    @allure.step("Ввод фамилии: {surname}")
    def set_surname(self, surname):
        self.send_keys(CustomerDataFormLocators.SURNAME_INPUT_CONTAINER, surname)

    @allure.step("Ввод адреса: {address}")
    def set_address(self, address):
        self.send_keys(CustomerDataFormLocators.ADDRESS_INPUT_CONTAINER, address)

    @allure.step("Выбор станции метро")
    def select_subway_station(self, station_locator):
        self.click(CustomerDataFormLocators.SUBWAY_STATION_SELECT_SEARCH)
        self.click(station_locator)

    @allure.step("Ввод номера телефона: {phone}")
    def set_phone_number(self, phone):
        self.send_keys(CustomerDataFormLocators.PHONE_INPUT_CONTAINER, phone)

    @allure.step("Переход к следующему шагу оформления заказа")
    def go_further(self):
        self.click(CustomerDataFormLocators.FURTHER_BUTTON)

import allure
from selenium.common import ElementClickInterceptedException
from pages.base_page import BasePage
from locators.order_page_rent_data_locators import (
    RentDataFormLocators,
    SubmitOrderWindowLocators,
    OrderPlacedLocators,
)


class OrderPageRentData(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание загрузки страницы аренды самоката")
    def wait_for_load_order_page_rent_data(self):
        self.wait_for_element_visibility(RentDataFormLocators.HEADER_ABOUT_RENT)

    @allure.step("Установка даты аренды")
    def set_date(self):
        self.click(RentDataFormLocators.RENT_DATE_DATE_PICKER)
        self.click(RentDataFormLocators.DATE_PICKER_DAY)

    @allure.step("Выбор срока аренды")
    def set_rent_time(self):
        self.click(RentDataFormLocators.RENT_TIME_DROPDOWN)
        self.click(RentDataFormLocators.RENT_TIME_SELECTED)

    @allure.step("Выбор цвета самоката")
    def set_scooter_color(self):
        self.click(RentDataFormLocators.SCOOTER_COLOR_PLACEHOLDER_BLACK)

    @allure.step("Ввод комментария для курьера: {comment}")
    def set_comment(self, comment):
        self.send_keys(RentDataFormLocators.COMMENT_INPUT, comment)

    @allure.step("Оформление заказа")
    def place_order(self):
        self.scroll_into_view(RentDataFormLocators.ORDER_BUTTON)
        try:
            self.click(RentDataFormLocators.ORDER_BUTTON)
        except ElementClickInterceptedException:
            self.js_click(RentDataFormLocators.ORDER_BUTTON)

        self.click(SubmitOrderWindowLocators.YES_BUTTON)

        self.wait_for_element_visibility(OrderPlacedLocators.ORDER_PLACED_TEXT)
        self.click(OrderPlacedLocators.CHECK_STATUS_BUTTON)

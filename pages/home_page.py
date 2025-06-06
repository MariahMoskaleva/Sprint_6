import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HeaderLocators, FAQDropDownLocators, LogoYandexLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_home_page(self):
        self.wait_for_element_visibility(HeaderLocators.HOME_HEADER)

    @allure.step("Открытие выпадающего списка по локатору: {locator}")
    def open_dropdown(self, locator):
        self.scroll_into_view(locator)
        try:
            self.wait_for_element_invisibility(BasePageLocators.SCOOTER_IMG)
        except TimeoutException:
            print("Overlay image still visible, proceeding with click")

        try:
            self.click(locator)
        except ElementClickInterceptedException:
            self.js_click(locator)

    @allure.step("Получение текста из выпадающего списка по локатору: {dropdown_locator}")
    def get_dropdown_text(self, dropdown_locator):
        return self.get_text(dropdown_locator)

    @allure.step("Открытие страницы оформления заказа по кнопке: {order_button_locator}")
    def open_order_page(self, order_button_locator):
        self.click(order_button_locator)

    @allure.step("Переход на домашнюю страницу Яндекса по клику на логотип")
    def redirect_to_zen_home_page(self):
        self.click(LogoYandexLocators.YANDEX_LOGO)

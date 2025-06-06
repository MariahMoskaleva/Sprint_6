import allure
from pages.base_page import BasePage
from locators.status_page_locators import StatusLocators, LogoLocators


class StatusPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание загрузки страницы статуса заказа")
    def wait_for_load_status_page(self):
        self.wait_for_element_visibility(StatusLocators.CHECK_STATUS_BUTTON)

    @allure.step("Переход на главную страницу по логотипу Самокат")
    def redirect_to_home_page(self):
        self.click(LogoLocators.SAMOKAT_LOGO)

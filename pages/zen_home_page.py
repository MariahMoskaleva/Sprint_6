import allure
from locators.zen_home_page_locators import ZenHomePageLocators
from pages.base_page import BasePage


class ZenHomePage(BasePage):
    @allure.step("Ожидание загрузки главной страницы Дзена")
    def wait_for_load(self, timeout=30):
        self.wait_for_element_visibility(ZenHomePageLocators.ZEN_UNIQUE_LOCATOR, timeout)

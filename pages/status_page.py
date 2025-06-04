from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.status_page_locators import StatusLocators, LogoLocators


class StatusPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_status_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(StatusLocators.CHECK_STATUS_BUTTON))

    def redirect_to_home_page(self):
        self.driver.find_element(*LogoLocators.SAMOKAT_LOGO).click()
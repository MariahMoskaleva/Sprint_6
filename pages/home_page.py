from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HeaderLocators, FAQDropDownLocators, LogoYandexLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HeaderLocators.HOME_HEADER))

    def scroll_to_faq(self):
        element = self.driver.find_element(*FAQDropDownLocators.RENT_TIME_QUESTION_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_dropdown(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(
                (By.CSS_SELECTOR, "img[src='/assets/scooter.png']")))
        except TimeoutException:
            print("Overlay image still visible, proceeding with click")

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def get_dropdown_text(self, dropdown_locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(dropdown_locator)
        )
        return element.text

    def open_order_page(self, order_button_locator):
        dropdown = self.driver.find_element(*order_button_locator)
        dropdown.click()

    def redirect_to_zen_home_page(self):
        logo = self.driver.find_element(*LogoYandexLocators.YANDEX_LOGO)
        logo.click()



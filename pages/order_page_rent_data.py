from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_rent_data_locators import RentDataFormLocators, SubmitOrderWindowLocators, OrderPlacedLocators


class OrderPageRentData:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page_rent_data(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(RentDataFormLocators.HEADER_ABOUT_RENT))

    def set_date(self):
        self.driver.find_element(*RentDataFormLocators.RENT_DATE_DATE_PICKER).click()
        self.driver.find_element(*RentDataFormLocators.DATE_PICKER_DAY).click()

    def set_rent_time(self):
        self.driver.find_element(*RentDataFormLocators.RENT_TIME_DROPDOWN).click()
        self.driver.find_element(*RentDataFormLocators.RENT_TIME_SELECTED).click()

    def set_scooter_color(self):
        self.driver.find_element(*RentDataFormLocators.SCOOTER_COLOR_PLACEHOLDER_BLACK).click()

    def set_comment(self, comment):
        self.driver.find_element(*RentDataFormLocators.COMMENT_INPUT).send_keys(comment)

    def place_order(self):
        order_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(RentDataFormLocators.ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        try:
            order_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", order_button)

        yes_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(SubmitOrderWindowLocators.YES_BUTTON)
        )
        yes_button.click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPlacedLocators.ORDER_PLACED_TEXT)
        )
        check_status_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(OrderPlacedLocators.CHECK_STATUS_BUTTON)
        )
        check_status_button.click()
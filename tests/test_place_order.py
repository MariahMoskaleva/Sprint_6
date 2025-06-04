import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import OrderButtonsLocators
from locators.zen_home_page_locators import ZenHomePageLocators
from pages.order_page_customer_data import OrderPageCustomerData
from pages.order_page_rent_data import OrderPageRentData
from pages.status_page import StatusPage


@pytest.mark.usefixtures("driver")
class TestPlaceOrder:

    @pytest.mark.parametrize(
        "name, surname, address, phone, comment",
        [
            ("тест тестович", "тестов", "тестовый адрес", "78985642489", "ыыыыыыыы"),
            ("тест имя", "тестфамилия", "тест адрес", "78985642488", "комментарий тест")
        ]
    )
    def test_place_order(self, home_page, driver, name, surname, address, phone, comment):
        home_page.open_order_page(OrderButtonsLocators.ORDER_BUTTON_HEADER)

        order_page_customer_data = OrderPageCustomerData(driver)
        order_page_customer_data.wait_for_load_order_page_customer_data()

        order_page_customer_data.set_name(name=name)
        order_page_customer_data.set_surname(surname=surname)
        order_page_customer_data.set_address(address=address)
        order_page_customer_data.select_subway_station()
        order_page_customer_data.set_phone_number(phone=phone)
        order_page_customer_data.go_further()

        order_page_rent_data = OrderPageRentData(driver)
        order_page_rent_data.wait_for_load_order_page_rent_data()

        order_page_rent_data.set_date()
        order_page_rent_data.set_rent_time()
        order_page_rent_data.set_scooter_color()
        order_page_rent_data.set_comment(comment=comment)
        order_page_rent_data.place_order()

        status_page = StatusPage(driver)
        status_page.wait_for_load_status_page()

        status_page.redirect_to_home_page()

        home_page.wait_for_load_home_page()

        home_page.redirect_to_zen_home_page()

        old_windows = driver.window_handles
        home_page.redirect_to_zen_home_page()

        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > len(old_windows)
        )

        new_windows = driver.window_handles
        new_window = [w for w in new_windows if w not in old_windows][0]
        driver.switch_to.window(new_window)

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(ZenHomePageLocators.ZEN_UNIQUE_LOCATOR)
        )
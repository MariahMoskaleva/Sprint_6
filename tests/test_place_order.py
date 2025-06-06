import pytest
import allure

from locators.home_page_locators import OrderButtonsLocators
from locators.order_page_customer_data_locators import CustomerDataFormLocators
from locators.zen_home_page_locators import ZenHomePageLocators
from pages.order_page_customer_data import OrderPageCustomerData
from pages.order_page_rent_data import OrderPageRentData
from pages.status_page import StatusPage
from pages.home_page import HomePage
from pages.zen_home_page import ZenHomePage


@pytest.mark.usefixtures("driver", "home_page")
class TestPlaceOrder:

    @pytest.mark.parametrize(
        "name, surname, address, phone, comment",
        [
            ("тест тестович", "тестов", "тестовый адрес", "78985642489", "ыыыыыыыы"),
            ("тест имя", "тестфамилия", "тест адрес", "78985642488", "комментарий тест")
        ]
    )
    @allure.title("Оформление заказа: {name} {surname}")
    def test_place_order(self, driver, name, surname, address, phone, comment):
        home_page = HomePage(driver)
        home_page.wait_for_load_home_page()
        home_page.open_order_page(OrderButtonsLocators.ORDER_BUTTON_HEADER)

        order_page_customer_data = OrderPageCustomerData(driver)
        order_page_customer_data.wait_for_load()
        order_page_customer_data.set_name(name)
        order_page_customer_data.set_surname(surname)
        order_page_customer_data.set_address(address)
        order_page_customer_data.select_subway_station(CustomerDataFormLocators.BOULVAR_ROKOSSOVSKOGO_MENU_ITEM)
        order_page_customer_data.set_phone_number(phone)
        order_page_customer_data.go_further()

        order_page_rent_data = OrderPageRentData(driver)
        order_page_rent_data.wait_for_load_order_page_rent_data()
        order_page_rent_data.set_date()
        order_page_rent_data.set_rent_time()
        order_page_rent_data.set_scooter_color()
        order_page_rent_data.set_comment(comment)
        order_page_rent_data.place_order()

        status_page = StatusPage(driver)
        status_page.wait_for_load_status_page()
        status_page.redirect_to_home_page()

        home_page.wait_for_load_home_page()

        old_windows = driver.window_handles
        home_page.redirect_to_zen_home_page()
        home_page.switch_to_new_window(old_windows)

        zen_home_page = ZenHomePage(driver)
        zen_home_page.wait_for_load()

        assert zen_home_page.driver.find_element(*ZenHomePageLocators.ZEN_UNIQUE_LOCATOR).is_displayed()

import pytest
from selenium import webdriver
from config import HOME_PAGE_URL
from pages.home_page import HomePage
from pages.order_page_customer_data import OrderPageCustomerData


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    driver.get(HOME_PAGE_URL)
    page = HomePage(driver)
    page.wait_for_load_home_page()
    return page


@pytest.fixture
def order_page_customer_data(driver):
    page = OrderPageCustomerData(driver)
    page.wait_for_load_order_page_customer_data()
    return page

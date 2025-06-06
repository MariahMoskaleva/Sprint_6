from selenium.webdriver.common.by import By


class BasePageLocators:
    SCOOTER_IMG = (By.CSS_SELECTOR, "img[src='/assets/scooter.png']")
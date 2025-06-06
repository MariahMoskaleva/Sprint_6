from selenium.webdriver.common.by import By


class RentDataFormLocators:
    HEADER_ABOUT_RENT = (By.CLASS_NAME, 'Order_Header__BZXOb')
    RENT_DATE_DATE_PICKER = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DATE_PICKER_DAY = (By.XPATH, '//div[@aria-label="Choose пятница, 13-е июня 2025 г."]')
    RENT_TIME_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENT_TIME_SELECTED = (By.XPATH, '//div[text()="двое суток"]')
    SCOOTER_COLOR_PLACEHOLDER_BLACK = (By.XPATH, '//label[@for="black"]')
    SCOOTER_COLOR_PLACEHOLDER_GREY = (By.XPATH, '//label[@for="grey"]')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button.Button_Button__ra12g.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)')


class SubmitOrderWindowLocators:
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')


class OrderPlacedLocators:
    ORDER_PLACED_TEXT = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    CHECK_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

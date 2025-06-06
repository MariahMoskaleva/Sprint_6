from selenium.webdriver.common.by import By


class HeaderLocators:
    HOME_HEADER = (By.CLASS_NAME, 'Home_Header__iJKdX')


class FAQDropDownLocators:
    PRICING_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), "оплатить")]')
    PRICING_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-0"]//p')
    SEVERAL_SCOOTERS_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), '
                                                  '"несколько самокатов!")]')
    SEVERAL_SCOOTERS_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-1"]//p')
    RENT_TIME_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), "время '
                                           'аренды")]')
    RENT_TIME_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-2"]//p')
    ORDER_TODAY_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), '
                                             '"прямо на сегодня")]')
    ORDER_TODAY_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-3"]//p')
    CHANGE_RENT_TERMS_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), '
                                                   '"продлить заказ")]')
    CHANGE_RENT_TERMS_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-4"]//p')
    SCOOTER_CHARGER_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), '
                                                 '"зарядку")]')
    SCOOTER_CHARGER_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-5"]//p')
    CANCEL_ORDER_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), '
                                              '"отменить")]')
    CANCEL_ORDER_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-6"]//p')
    REGIONS_ORDER_QUESTION_BUTTON = (By.XPATH, '//div[contains(@class, "accordion__button") and contains(text(), '
                                              '"МКАДом")]')
    REGIONS_ORDER_ANSWER_TEXT = (By.XPATH, '//div[@aria-labelledby="accordion__heading-7"]//p')


class OrderButtonsLocators:
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')


class LogoYandexLocators:
    YANDEX_LOGO = (By.XPATH, '//img[@alt="Yandex"]')

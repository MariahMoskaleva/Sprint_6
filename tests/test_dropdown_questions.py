import pytest
import allure

from locators.home_page_locators import FAQDropDownLocators
from data.FAQ_data import (
    PRICING_ANSWER,
    SEVERAL_SCOOTERS_ANSWER,
    RENT_TIME_ANSWER,
    ORDER_TODAY_ANSWER,
    CHANGE_RENT_TERMS_ANSWER,
    SCOOTER_CHARGER_ANSWER,
    CANCEL_ORDER_ANSWER,
    REGIONS_ORDER_ANSWER,
)

FAQ_CASES = [
    (FAQDropDownLocators.PRICING_QUESTION_BUTTON,
     FAQDropDownLocators.PRICING_ANSWER_TEXT,
     PRICING_ANSWER),

    (FAQDropDownLocators.SEVERAL_SCOOTERS_QUESTION_BUTTON,
     FAQDropDownLocators.SEVERAL_SCOOTERS_ANSWER_TEXT,
     SEVERAL_SCOOTERS_ANSWER),

    (FAQDropDownLocators.RENT_TIME_QUESTION_BUTTON,
     FAQDropDownLocators.RENT_TIME_ANSWER_TEXT,
     RENT_TIME_ANSWER),

    (FAQDropDownLocators.ORDER_TODAY_QUESTION_BUTTON,
     FAQDropDownLocators.ORDER_TODAY_ANSWER_TEXT,
     ORDER_TODAY_ANSWER),

    (FAQDropDownLocators.CHANGE_RENT_TERMS_QUESTION_BUTTON,
     FAQDropDownLocators.CHANGE_RENT_TERMS_ANSWER_TEXT,
     CHANGE_RENT_TERMS_ANSWER),

    (FAQDropDownLocators.SCOOTER_CHARGER_QUESTION_BUTTON,
     FAQDropDownLocators.SCOOTER_CHARGER_ANSWER_TEXT,
     SCOOTER_CHARGER_ANSWER),

    (FAQDropDownLocators.CANCEL_ORDER_QUESTION_BUTTON,
     FAQDropDownLocators.CANCEL_ORDER_ANSWER_TEXT,
     CANCEL_ORDER_ANSWER),

    (FAQDropDownLocators.REGIONS_ORDER_QUESTION_BUTTON,
     FAQDropDownLocators.REGIONS_ORDER_ANSWER_TEXT,
     REGIONS_ORDER_ANSWER),
]


@pytest.mark.usefixtures("driver")
class TestDropdownQuestions:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", FAQ_CASES)
    @allure.title("Проверка FAQ: {expected_text[:30]}...")  # Можно упростить или добавить другое название
    def test_faq_dropdown(self, home_page, question_locator, answer_locator, expected_text):
        home_page.open_dropdown(question_locator)
        actual_text = home_page.get_dropdown_text(answer_locator)
        assert actual_text == expected_text

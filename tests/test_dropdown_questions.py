import pytest
from locators.home_page_locators import FAQDropDownLocators


@pytest.mark.usefixtures("driver")
class TestDropdownQuestions:

    def test_pricing_question(self, home_page):
        home_page.open_dropdown(FAQDropDownLocators.PRICING_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.PRICING_ANSWER_TEXT)
        assert answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_several_scooters_question(self, home_page):
        home_page.open_dropdown(FAQDropDownLocators.SEVERAL_SCOOTERS_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.SEVERAL_SCOOTERS_ANSWER_TEXT)
        assert answer == ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                          'можете просто сделать несколько заказов — один за другим.')

    def test_rent_time_question(self, home_page):
        home_page.open_dropdown(FAQDropDownLocators.RENT_TIME_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.RENT_TIME_ANSWER_TEXT)
        assert answer == ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                          'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                          'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    def test_order_today_question(self, home_page):
        home_page.open_dropdown(FAQDropDownLocators.ORDER_TODAY_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.ORDER_TODAY_ANSWER_TEXT)
        assert answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_change_rent_terms_question(self, home_page):
        home_page.scroll_to_faq()
        home_page.open_dropdown(FAQDropDownLocators.CHANGE_RENT_TERMS_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.CHANGE_RENT_TERMS_ANSWER_TEXT)
        assert answer == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                          'номеру 1010.')

    def test_scooter_charger_question(self, home_page):
        home_page.open_dropdown(FAQDropDownLocators.SCOOTER_CHARGER_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.SCOOTER_CHARGER_ANSWER_TEXT)
        assert answer == ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если '
                          'будете кататься без передышек и во сне. Зарядка не понадобится.')

    def test_cancel_order_question(self, home_page):
        home_page.open_dropdown(FAQDropDownLocators.CANCEL_ORDER_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.CANCEL_ORDER_ANSWER_TEXT)
        assert answer == ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все '
                          'же свои.')

    def test_regions_order_question(self, home_page):
        home_page.open_dropdown(FAQDropDownLocators.REGIONS_ORDER_QUESTION_BUTTON)
        answer = home_page.get_dropdown_text(FAQDropDownLocators.REGIONS_ORDER_ANSWER_TEXT)
        assert answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

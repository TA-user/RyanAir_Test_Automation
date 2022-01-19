from .base_page import BasePage
from tests.pages.payment_page_locators import PaymentPageLocators


class PaymentPage(BasePage):
    car_hire_datetime_format = "%d %b %Y - %H:%M"

    def go_to_passenger_info(self):
        self.element_interactions.click_element(PaymentPageLocators.PASSENGER_INFO_DROPDOWN)

    def go_to_main_page(self):
        self.element_interactions.click_element(PaymentPageLocators.LOGO_BUTTON)

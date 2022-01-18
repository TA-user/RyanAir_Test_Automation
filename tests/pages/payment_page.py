from .base_page import BasePage
from tests.pages.payment_page_locators import PaymentPageLocators

class PaymentPage(BasePage):
    def go_to_passenger_info(self):
        self.element_interactions.click_element(PaymentPageLocators.PASSENGER_INFO_DROPDOWN)
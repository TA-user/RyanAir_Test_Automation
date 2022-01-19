import allure

from .base_page import BasePage
from tests.pages.payment_page_locators import PaymentPageLocators


class PaymentPage(BasePage):
    car_hire_datetime_format = "%d %b %Y - %H:%M"
    
    @allure.step('Go to passenger name dropdown"')
    def go_to_passenger_info(self):
        self.element_interactions.click_element(PaymentPageLocators.PASSENGER_INFO_DROPDOWN)
    
    @allure.step('Go to main page by clicking logo"')
    def go_to_main_page(self):
        self.element_interactions.click_element(PaymentPageLocators.LOGO_BUTTON)

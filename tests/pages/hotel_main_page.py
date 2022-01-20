from .base_page import BasePage
from .hotel_main_page_locators import HotelMainPageHeaderLocators, HotelMainPageLocators


class HotelMainPage(BasePage):
    def log_out(self):
        self.element_interactions.click_element(HotelMainPageHeaderLocators.USER_MENU)
        self.element_interactions.click_element(HotelMainPageHeaderLocators.LOG_OUT_BUTTON)

    def accept_cookies(self):
        if self.element_interactions.is_element_visible(HotelMainPageLocators.ACCEPT_COOKIES_BUTTON):
            self.element_interactions.click_element(HotelMainPageLocators.ACCEPT_COOKIES_BUTTON)

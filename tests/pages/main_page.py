from .base_page import BasePage
from .main_page_locators import LogInPopupLocators, MainPageLocators


class MainPage(BasePage):
    def click_accept_cookie_popup_button(self):
        self.element_interactions.click_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)

    def open_search_cars_tab(self):
        self.element_interactions.click_element(MainPageLocators.SEARCH_FLIGHTS_TAB)


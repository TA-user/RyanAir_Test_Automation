import allure
from .base_page import BasePage
from .main_page_locators import MainPageLocators, SearchCarsTabLocators, CalendarWidgetLocators, \
    MainPageHeaderLocators, LogInPopupLocators, SearchFlightsTabLocators, SearchHotelsTabLocators
from utils.text_formatter import TextFormatter


class MainPage(BasePage):
    @allure.step('Accept cookies by clicking button')
    def accept_cookies(self):
        if self.element_interactions.is_element_visible(MainPageLocators.ACCEPT_COOKIES_BUTTON):
            self.element_interactions.click_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)

    def log_in(self, username, password):
        with allure.step('Log in through header button with given values'):
            self.element_interactions.click_element(MainPageHeaderLocators.LOG_IN_BUTTON)
            self.element_interactions.send_text_in_field(LogInPopupLocators.EMAIL_FIELD, username)
            self.element_interactions.send_text_in_field(LogInPopupLocators.PASSWORD_FIELD, password)
            self.element_interactions.click_element(LogInPopupLocators.CONFIRMATION_LOG_IN_BUTTON)

    @allure.step('Log out through header user menu button')
    def log_out(self):
        self.element_interactions.click_element(MainPageHeaderLocators.USER_MENU)
        self.element_interactions.click_element(MainPageHeaderLocators.LOG_OUT_BUTTON)

    @allure.step('Open car hire tab')
    def open_car_hire_tab(self):
        self.element_interactions.click_element(MainPageLocators.CAR_HIRE_TAB)

    @allure.step('Open flight search tab')
    def open_search_flights_tab(self):
        self.element_interactions.click_element(MainPageLocators.SEARCH_FLIGHTS_TAB)

    def open_search_hotel_tab(self):
        self.element_interactions.click_element(MainPageLocators.SEARCH_HOTELS_TAB)

    @allure.step('Select given date "{1}" at calendar widget')
    def choose_date(self, date: str):
        date_nt = TextFormatter.format_date(date)
        pick_up_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(date_nt.month_name)
        self.element_interactions.click_element(pick_up_date_month_locator)
        pick_up_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(date)
        self.element_interactions.click_element(pick_up_date_day_locator)


class MainPageSearchFlightsTab(MainPage):
    @allure.step('Perform complex action of flights search')
    def perform_flights_search(self, depart_location, destination_location, depart_date, return_date):
        self.choose_depart_location(depart_location)
        self.choose_destination_location(destination_location)
        self.choose_depart_date(depart_date)
        self.choose_return_date(return_date)
        self.element_interactions.click_element(SearchFlightsTabLocators.SEARCH_FLIGHT_BUTTON)

    @allure.step('Type and select depart location - "{1}" in form and confirm')
    def choose_depart_location(self, depart_location):
        self.element_interactions.send_text_in_field(SearchFlightsTabLocators.DEPART_LOCATION, depart_location)
        self.element_interactions.click_element(SearchFlightsTabLocators.LAST_ITEM_DROPDOWN_AIRPORT)

    @allure.step('Type and select destination location - "{1}" in form and confirm')
    def choose_destination_location(self, destination_location):
        self.element_interactions.send_text_in_field(SearchFlightsTabLocators.DESTINATION_LOCATION,
                                                     destination_location)
        self.element_interactions.click_element(SearchFlightsTabLocators.LAST_ITEM_DROPDOWN_AIRPORT)

    @allure.step('Select depart date in widget')
    def choose_depart_date(self, date: str):
        self.choose_date(date)

    @allure.step('Select return date in widget')
    def choose_return_date(self, date: str):
        self.choose_date(date)


class MainPageSearchHotelsTab(MainPage):
    def perform_hotels_search(self, destination, check_in_date, check_out_date):
        self.choose_destination_location(destination)
        self.choose_check_in_date(check_in_date)
        self.choose_check_out_date(check_out_date)
        self.element_interactions.click_element(SearchHotelsTabLocators.SEARCH_HOTEL_BUTTON)

    def choose_destination_location(self, destination):
        self.element_interactions.send_text_in_field(SearchHotelsTabLocators.DESTINATION_HOTEL_FORM, destination)
        self.element_interactions.click_element(SearchHotelsTabLocators.FIRST_ITEM_HOTEL_DROPDOWN)

    def choose_check_in_date(self, check_in_date: str):
        self.element_interactions.click_element(SearchHotelsTabLocators.CHECK_IN_FORM)
        self.choose_date(check_in_date)

    def choose_check_out_date(self, check_out_date: str):
        self.element_interactions.click_element(SearchHotelsTabLocators.CHECK_OUT_FORM)
        self.choose_date(check_out_date)


class MainPageCarHireTab(MainPage):
    @allure.step('Perform complex action of search car for hire')
    def perform_car_sharing(self, pick_up_location: str, airport_code: str, pick_up_year_month_day: str,
                            pick_up_time: str, drop_off_year_month_day: str, drop_off_time: str):
        self.choose_pick_up_location(pick_up_location, airport_code)
        self.choose_pick_up_date(pick_up_year_month_day)
        self.choose_drop_off_date(drop_off_year_month_day)
        self.choose_pick_up_time(pick_up_time)
        self.choose_drop_off_time(drop_off_time)
        self.click_submit_button()

    @allure.step('Type and select pick up location "{1}" with location code - "{2}"')
    def choose_pick_up_location(self, pick_up_location, airport_code):
        self.element_interactions.send_text_in_field(SearchCarsTabLocators.CAR_LOCATION, pick_up_location)
        airport_item_in_ddm_locator = SearchCarsTabLocators.get_airport_item_in_dropdown(airport_code)
        self.element_interactions.click_element(airport_item_in_ddm_locator)

    @allure.step('Select time - "{1}" in dropdown widget')
    def choose_time(self, time_):
        element_in_time_ddm_locator = CalendarWidgetLocators.get_time_in_ddm_locator(time_)
        self.element_interactions.click_element(element_in_time_ddm_locator)

    @allure.step('Select pick up date in widget')
    def choose_pick_up_date(self, date: str):
        self.element_interactions.click_element(SearchCarsTabLocators.PICK_UP_FORM)
        self.choose_date(date)

    @allure.step('Select drop off date in widget')
    def choose_drop_off_date(self, date: str):
        self.element_interactions.click_element(SearchCarsTabLocators.DROP_OFF_FORM)
        self.choose_date(date)

    @allure.step('Select pick up time in widget')
    def choose_pick_up_time(self, time_: str):
        self.element_interactions.click_element(SearchCarsTabLocators.PICK_UP_TIME_FORM)
        self.choose_time(time_)

    @allure.step('Select drop off time in widget')
    def choose_drop_off_time(self, time_: str):
        self.element_interactions.click_element(SearchCarsTabLocators.DROP_OFF_TIME_FORM)
        self.choose_time(time_)

    @allure.step('Confirm car search to proceed')
    def click_submit_button(self):
        self.element_interactions.click_element(SearchCarsTabLocators.SEARCH_CARS_BUTTON)

from .base_page import BasePage

from tests.pages.trip_viewer_page_locators import FlightsTabLocators
from tests.pages.trip_viewer_page_locators import SeatsTabLocators
from tests.pages.trip_viewer_page_locators import BagsTabLocators
from tests.pages.trip_viewer_page_locators import ExtrasTabLocators
from tests.pages.trip_viewer_page_locators import HeaderLocators
from tests.pages.trip_viewer_page_locators import OverviewTabLocators
from .trip_viewer_page_locators import CarHireTabLocators


class TripViewerPage(BasePage):
    def open_cart(self):
        self.element_interactions.click_element(HeaderLocators.BASKET_ICON)

    def close_flight_confirmation_popup(self):
        if self.element_interactions.is_element_visible(HeaderLocators.FLIGHT_CONFIRMATION_POPUP):
            self.element_interactions.click_element(HeaderLocators.CLOSE_CONFIRMATION_POPUP_BUTTON)

    def go_checkout(self):
        self.element_interactions.click_element(OverviewTabLocators.CHECKOUT_BUTTON)

    def go_to_main(self):
        self.element_interactions.click_element(HeaderLocators.MAIN_LOGO)


class TripViewerPageFlightsTab(BasePage):
    def choose_cheapest_depart_flight(self):
        flight_elements = self.element_interactions.find_visible_elements(FlightsTabLocators.FLIGHT_DEPART_PRICES)
        elements_values = []
        for element in flight_elements:
            value = float(element.text[1:])
            elements_values.append(value)
        element_dict = ({element: value for element in flight_elements for value in elements_values})
        minimum_price_flight_card = min(element_dict, key=element_dict.get)
        minimum_price_flight_card.click()

    def choose_cheapest_return_flight(self):
        flight_elements = self.element_interactions.find_visible_elements(FlightsTabLocators.FLIGHT_RETURN_PRICES)
        elements_values = []
        for element in flight_elements:
            value = float(element.text[1:])
            elements_values.append(value)
        element_dict = ({element: value for element in flight_elements for value in elements_values})
        minimum_price_flight_card = min(element_dict, key=element_dict.get)
        minimum_price_flight_card.click()

    def choose_light_fare_type(self):
        self.element_interactions.click_element(FlightsTabLocators.LIGHT_TYPE_CONTINUE_BUTTON)
        self.element_interactions.click_element(FlightsTabLocators.CONFIRMATION_VALUE_FARE)

    def input_passengers_data(self, first_name, last_name):
        self.element_interactions.click_element(FlightsTabLocators.PASSENGER_TITLE)
        self.element_interactions.click_element(FlightsTabLocators.MR_PASSENGER_TITLE)
        self.element_interactions.send_text_in_field(FlightsTabLocators.FIRST_NAME_PASSENGER_INPUT, first_name)
        self.element_interactions.send_text_in_field(FlightsTabLocators.LAST_NAME_PASSENGER_INPUT, last_name)
        self.element_interactions.click_element(FlightsTabLocators.PASSENGERS_CONTINUATION_BUTTON)


class TripViewerPageSeatsTab(BasePage):
    def choose_later_selection_option(self):
        self.element_interactions.click_element(SeatsTabLocators.SEATS_LATER_OPTION_BUTTON)
        self.element_interactions.click_element(SeatsTabLocators.WITHOUT_SEATS_CONTINUATION_BUTTON)


class TripViewerPageBagsTab(BasePage):
    def choose_one_small_bag(self):
        self.element_interactions.click_element(BagsTabLocators.ONE_SMALL_BAG_RADIOBUTTON)
        self.element_interactions.click_element(BagsTabLocators.BAGS_CONTINUATION_BUTTON)
        self.element_interactions.click_element(BagsTabLocators.BAG_POPUP_DECLINE_BUTTON)


class TripViewerPageExtrasTab(BasePage):
    def continue_order_without_extras(self):
        self.element_interactions.click_element(ExtrasTabLocators.EXTRAS_TRIP_CONTINUATION_BUTTON)
        if self.element_interactions.is_element_visible(ExtrasTabLocators.TRANSPORT_INFO_CARD):
            self.element_interactions.click_at_left_top_element_corner(
                ExtrasTabLocators.EXTRAS_TRANSPORT_CONTINUATION_BUTTON)


class TripViewerPageOverviewTab(BasePage):
    flight_search_date_format = "%a, %d %b"
    car_hire_date_format = "%a, %d %b"


class TripViewerPageCarHireTab(BasePage):
    search_summary_datetime_format = "%a, %d %b %Y, %H:%M"

    def switch_to_getting_around_iframe(self):
        getting_around_iframe = self.element_interactions.find_element(CarHireTabLocators.GETTING_AROUND_IFRAME)
        self.browser.switch_to.frame(getting_around_iframe)


class TripViewerPageHeader(BasePage):
    car_hire_datetime_format = "%d %b %Y - %H:%M"

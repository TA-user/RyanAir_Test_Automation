import time

from .base_page import BasePage
from selenium import webdriver

from tests.pages.trip_viewer_page_locators import FlightsTabLocators
from tests.pages.trip_viewer_page_locators import SeatsTabLocators
from tests.pages.trip_viewer_page_locators import BagsTabLocators
from tests.pages.trip_viewer_page_locators import ExtrasTabLocators
from tests.pages.trip_viewer_page_locators import TripPlannerLocators


class TripViewerPageFlightsTab(BasePage):
    def choose_cheapest_depart_flight(self):
        minimum_price_flight_card = self.element_interactions.choose_element_with_minimum_price(
            FlightsTabLocators.FLIGHT_DEPART_PRICES)
        minimum_price_flight_card.click()
        
    def choose_cheapest_return_flight(self):
        minimum_price_flight_card = self.element_interactions.choose_element_with_minimum_price(
            FlightsTabLocators.FLIGHT_RETURN_PRICES)
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
        self.element_interactions.click_at_coordinates_of_element(ExtrasTabLocators.EXTRAS_TRANSPORT_CONTINUATION_BUTTON, 10, 10)
        
class TripViewerPageOverviewTab(BasePage):
    pass



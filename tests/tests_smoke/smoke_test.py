import time
import pytest
from assertpy import soft_assertions
from tests.pages.main_page_locators import MainPageHeaderLocators
from tests.pages.main_page_locators import LogInPopupLocators
from tests.pages.main_page_locators import MainPageHeaderLocators
from tests.pages.main_page_locators import LogInPopupLocators
from tests.pages.trip_viewer_page_locators import FlightsTabLocators
from tests.pages.trip_viewer_page_locators import HeaderLocators
from tests.pages.trip_viewer_page_locators import TripPlannerLocators
from tests.pages.trip_viewer_page_locators import OverviewTabLocators
from utils.assertions import Assertions


@pytest.fixture(scope="function")
def setup(browser, main_page, user, password):
    main_page.open()
    main_page.accept_cookies()
    main_page.log_in(user, password)
    yield
    main_page.log_out()



def test_guest_can_log_in(setup, user, assertions):
    assertions.element_should_be_visible(MainPageHeaderLocators.USER_AVATAR)
    assertions.element_should_contain_phrase(MainPageHeaderLocators.USER_MENU, user)


@pytest.mark.parametrize("depart_airport, destination_airport, depart_date, return_date",
                         [("Berlin Brandenburg", "London Stansted", "2022-03-11", "2022-03-18")])
def test_user_can_order_flights(browser, assertions, setup, main_page, main_page_search_flights_tab, trip_viewer_page_flights_tab,
                                trip_viewer_page_seats_tab, trip_viewer_page_bags_tab, trip_viewer_page_extras_tab,
                                trip_viewer_page, depart_airport, destination_airport, depart_date,
                                return_date):
    main_page_search_flights_tab.perform_flights_search(depart_airport, destination_airport, depart_date, return_date)
    assertions.element_should_be_visible(FlightsTabLocators.FLIGHT_CARDS)
    assertions.visible_element_should_contain_phrase(FlightsTabLocators.ACTUAL_DEPART_LOCATION, depart_airport)
    assertions.visible_element_should_contain_phrase(FlightsTabLocators.ACTUAL_DESTINATION_LOCATION, destination_airport)
    # TODO : implement verfication of dates at page description
    trip_viewer_page_flights_tab.choose_cheapest_depart_flight()
    trip_viewer_page_flights_tab.choose_cheapest_return_flight()
    trip_viewer_page_flights_tab.choose_light_fare_type()
    trip_viewer_page_flights_tab.input_passengers_data('User', 'Tester')
    trip_viewer_page_seats_tab.choose_later_selection_option()
    trip_viewer_page_bags_tab.choose_one_small_bag()
    trip_viewer_page_extras_tab.continue_order_without_extras()
    trip_viewer_page.close_popup()
    assertions.element_should_be_visible(HeaderLocators.BASKET_ICON)
    assertions.element_should_be_visible(HeaderLocators.BASKET_TOTAL_PRICE)
    assertions.element_should_be_visible(TripPlannerLocators.TRIP_PLANER_SIDEBAR)
    assertions.element_should_contain_phrase(TripPlannerLocators.DEPART_LOCATION_FIRST_FLIGHT, depart_airport)
    assertions.element_should_contain_phrase(TripPlannerLocators.DESTINATION_LOCATION_FIRST_FLIGHT, destination_airport)
    assertions.element_should_contain_phrase(TripPlannerLocators.DEPART_LOCATION_SECOND_FLIGHT, depart_airport)
    assertions.element_should_contain_phrase(TripPlannerLocators.DESTINATION_LOCATION_SECOND_FLIGHT, destination_airport)
    assertions.element_text_should_be_in_date(TripPlannerLocators.DEPART_DATE, depart_date)
    assertions.element_text_should_be_in_date(TripPlannerLocators.RETURN_DATE, return_date)
    assertions.element_should_be_clickable(OverviewTabLocators.CHECKOUT_BUTTON)
    trip_viewer_page.open_cart()
    assertions.element_should_contain_date(HeaderLocators.BASKET_FIRST_FLIGHT_DATE, depart_date)
    assertions.element_should_contain_date(HeaderLocators.BASKET_SECOND_FLIGHT_DATE, return_date)
    assertions.visible_element_should_contain_phrase(HeaderLocators.BASKET_DEPART_LOCATION_FIRST_FLIGHT, depart_airport)
    assertions.visible_element_should_contain_phrase(HeaderLocators.BASKET_DESTINATION_LOCATION_FIRST_FLIGHT, destination_airport)
    assertions.visible_element_should_contain_phrase(HeaderLocators.BASKET_DEPART_LOCATION_SECOND_FLIGHT, destination_airport)
    assertions.visible_element_should_contain_phrase(HeaderLocators.BASKET_DESTINATION_LOCATION_SECOND_FLIGHT, depart_airport)
    trip_viewer_page.go_to_main()
    
    
import allure
import pytest
from config import Urls
from tests.data.flights_search_data import Data
from tests.pages.payment_page_locators import PaymentPageLocators
from tests.pages.trip_viewer_page_locators import FlightsTabLocators
from tests.pages.trip_viewer_page_locators import HeaderLocators
from tests.pages.trip_viewer_page_locators import OverviewTabLocators
from tests.pages.trip_viewer_page_locators import TripPlannerLocators


@pytest.fixture(scope="function")
def setup(browser, main_page, username, password):
    main_page.open(Urls.MAIN_PAGE_URL)
    main_page.accept_cookies()
    main_page.log_in(username, password)
    yield
    main_page.log_out()


class TestFlightsOrder:
    @allure.feature("Flights order")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.flights_order
    @pytest.mark.parametrize("depart_airport, destination_airport, depart_date, return_date, first_name, last_name",
                             Data.flights_search_data)
    def test_user_can_order_flights(browser, assertions, setup, main_page, main_page_search_flights_tab,
                                    trip_viewer_page_flights_tab,
                                    trip_viewer_page_seats_tab, trip_viewer_page_bags_tab, trip_viewer_page_extras_tab,
                                    trip_viewer_page, payment_page, depart_airport, destination_airport, depart_date,
                                    return_date, first_name, last_name):
        main_page_search_flights_tab.perform_flights_search(depart_airport, destination_airport, depart_date,
                                                            return_date)
        
        assertions.element_should_be_visible(FlightsTabLocators.FLIGHT_CARDS)
        assertions.element_should_contain_value(FlightsTabLocators.ACTUAL_DEPART_LOCATION, depart_airport)
        assertions.element_should_contain_value(FlightsTabLocators.ACTUAL_DESTINATION_LOCATION,
                                                destination_airport)
        assertions.element_should_contain_date(FlightsTabLocators.ACTUAL_DATES_DESCRIPTION, depart_date)
        assertions.element_should_contain_date(FlightsTabLocators.ACTUAL_DATES_DESCRIPTION, return_date)
        
        trip_viewer_page_flights_tab.choose_cheapest_depart_flight()
        trip_viewer_page_flights_tab.choose_cheapest_return_flight()
        trip_viewer_page_flights_tab.choose_light_fare_type()
        trip_viewer_page_flights_tab.input_passengers_data(first_name, last_name)
        trip_viewer_page_seats_tab.choose_later_selection_option()
        trip_viewer_page_bags_tab.choose_one_small_bag()
        trip_viewer_page_extras_tab.continue_order_without_extras()
        trip_viewer_page.close_flight_confirmation_popup()
        trip_viewer_page.open_cart()
        
        assertions.element_should_be_visible(HeaderLocators.BASKET_ICON)
        assertions.element_should_be_visible(HeaderLocators.BASKET_TOTAL_PRICE)
        assertions.element_should_be_visible(TripPlannerLocators.TRIP_PLANER_SIDEBAR)
        assertions.element_should_contain_value(TripPlannerLocators.DEPART_LOCATION_FIRST_FLIGHT, depart_airport)
        assertions.element_should_contain_value(TripPlannerLocators.DESTINATION_LOCATION_FIRST_FLIGHT,
                                                destination_airport)
        assertions.element_should_contain_value(TripPlannerLocators.DEPART_LOCATION_SECOND_FLIGHT, depart_airport)
        assertions.element_should_contain_value(TripPlannerLocators.DESTINATION_LOCATION_SECOND_FLIGHT,
                                                destination_airport)
        assertions.date_should_contain_element(TripPlannerLocators.DEPART_DATE, depart_date)
        assertions.date_should_contain_element(TripPlannerLocators.RETURN_DATE, return_date)
        assertions.element_should_be_clickable(OverviewTabLocators.CHECKOUT_BUTTON)
        assertions.element_should_contain_date(HeaderLocators.BASKET_FIRST_FLIGHT_DATE, depart_date)
        assertions.element_should_contain_date(HeaderLocators.BASKET_SECOND_FLIGHT_DATE, return_date)
        assertions.element_should_contain_value(HeaderLocators.BASKET_DEPART_LOCATION_FIRST_FLIGHT,
                                                depart_airport)
        assertions.element_should_contain_value(HeaderLocators.BASKET_DESTINATION_LOCATION_FIRST_FLIGHT,
                                                destination_airport)
        assertions.element_should_contain_value(HeaderLocators.BASKET_DEPART_LOCATION_SECOND_FLIGHT,
                                                destination_airport)
        assertions.element_should_contain_value(HeaderLocators.BASKET_DESTINATION_LOCATION_SECOND_FLIGHT,
                                                depart_airport)
        
        trip_viewer_page.go_checkout()
        payment_page.go_to_passenger_info()
        
        assertions.element_should_be_visible(PaymentPageLocators.CARD_DETAIL_FORM)
        assertions.element_should_be_visible(PaymentPageLocators.BILLING_ADDRESS_FORM)
        assertions.element_should_be_visible(PaymentPageLocators.PAY_BUTTON)
        assertions.element_should_contain_value(PaymentPageLocators.DEPART_LOCATION_FIRST_FLIGHT, depart_airport)
        assertions.element_should_contain_value(PaymentPageLocators.DESTINATION_LOCATION_FIRST_FLIGHT,
                                                destination_airport)
        assertions.element_should_contain_value(PaymentPageLocators.DEPART_LOCATION_SECOND_FLIGHT, destination_airport)
        assertions.element_should_contain_value(PaymentPageLocators.DESTINATION_LOCATION_SECOND_FLIGHT, depart_airport)
        assertions.element_should_contain_date(PaymentPageLocators.DEPART_DATE, depart_date)
        assertions.element_should_contain_date(PaymentPageLocators.RETURN_DATE, return_date)
        assertions.element_should_contain_value(PaymentPageLocators.PASSENGER_NAME, first_name)
        assertions.element_should_contain_value(PaymentPageLocators.PASSENGER_NAME, last_name)
        
        trip_viewer_page.go_to_main()

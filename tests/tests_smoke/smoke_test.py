import time
import pytest
from tests.pages.main_page_locators import MainPageHeaderLocators
from tests.pages.main_page_locators import LogInPopupLocators
from tests.pages.trip_viewer_page_locators import FlightsTabLocators
from tests.pages.main_page_locators import MainPageHeaderLocators
from tests.pages.main_page_locators import LogInPopupLocators



@pytest.fixture(scope="function")
def setup(browser, main_page, user, password):
    main_page.open()
    main_page.accept_cookies()
    main_page.log_in(user, password)


def test_guest_can_log_in(setup, user, assertions):
    assertions.element_should_be_visible(MainPageHeaderLocators.USER_AVATAR)
    assertions.element_should_contain_phrase(MainPageHeaderLocators.USER_MENU, user)



def test_user_can_order_flights(browser, main_page, main_page_search_flights_tab, trip_viewer_page_flights_tab,
                                trip_viewer_page_seats_tab, trip_viewer_page_bags_tab, trip_viewer_page_extras_tab):
    main_page.open()
    main_page.accept_cookie()
    main_page.element_interactions.click_element(MainPageHeaderLocators.LOG_IN_BUTTON)
    main_page.element_interactions.send_text_in_field(LogInPopupLocators.EMAIL_FORM, 'testuserintern@mail.ru')
    main_page.element_interactions.send_text_in_field(LogInPopupLocators.PASSWORD_FORM, 'ui89WFdd')
    main_page.element_interactions.click_element(LogInPopupLocators.CONFIRMATION_LOG_IN_BUTTON)
    main_page_search_flights_tab.perform_flights_search('Berlin Brandenburg', 'London Stansted', '2022-03-11', '2022-03-18')
    trip_viewer_page_flights_tab.assertions.element_should_be_visible(FlightsTabLocators.FLIGHT_CARDS)
    trip_viewer_page_flights_tab.assertions.visible_element_should_contain_phrase(FlightsTabLocators.ACTUAL_DEPART_LOCATION, 'Berlin Brandenburg')
    trip_viewer_page_flights_tab.assertions.visible_element_should_contain_phrase(FlightsTabLocators.ACTUAL_DESTINATION_LOCATION, 'London Stansted')
    # TODO : implement verfication of dates at page description
    trip_viewer_page_flights_tab.choose_cheapest_depart_flight()
    trip_viewer_page_flights_tab.choose_cheapest_return_flight()
    trip_viewer_page_flights_tab.choose_light_fare_type()
    trip_viewer_page_flights_tab.input_passengers_data('user', 'Tester')
    trip_viewer_page_seats_tab.choose_later_selection_option()
    trip_viewer_page_bags_tab.choose_one_small_bag()
    trip_viewer_page_extras_tab.continue_order_without_extras()
    
    
    time.sleep(3)

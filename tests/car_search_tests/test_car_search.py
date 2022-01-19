import pytest
from tests.pages.trip_viewer_page_locators import CarHireTabLocators, OverviewTabLocators, HeaderLocators
from tests.pages.payment_page_locators import PaymentPageLocators
from tests.data.car_hire_data import Data
from config import Urls


class TestCarHire:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, main_page, username, password):
        main_page.open(Urls.MAIN_PAGE_URL)
        main_page.accept_cookies()
        main_page.log_in(username, password)
        yield
        main_page.log_out()

    @pytest.mark.smoke
    @pytest.mark.car_hire
    @pytest.mark.parametrize("airport, airport_code, pick_up_date, pick_up_time, drop_off_date, drop_off_time",
                             Data.car_hire_data)
    def test_user_can_hire_car(self, assertions, main_page, main_page_car_hire_tab, trip_viewer_page_car_hire_tab,
                               trip_viewer_page_overview_tab, trip_viewer_page_header, payment_page,
                               airport, airport_code, pick_up_date, pick_up_time, drop_off_date, drop_off_time):
        main_page.open_car_hire_tab()
        main_page_car_hire_tab.perform_car_sharing(airport, airport_code, pick_up_date, pick_up_time,
                                                   drop_off_date, drop_off_time)
        # Move to the trip_viewer_page_car_hire_tab
        assertions.element_should_contain_value(CarHireTabLocators.HEADER_TITLE,
                                                Data.trip_viewer_page_car_hire_tab_header)
        trip_viewer_page_car_hire_tab.switch_to_getting_around_iframe()
        assertions.element_should_be_visible(CarHireTabLocators.FIRST_CAR_IMAGE)  # check the visibility of car image
        trip_viewer_page_car_hire_tab.element_interactions.click_element(CarHireTabLocators.FIRST_CAR_VIEW_DEAL_BUTTON)
        assertions.element_should_contain_value(CarHireTabLocators.PICK_UP_LOCATION, airport)
        assertions.element_should_contain_value(CarHireTabLocators.PICK_UP_LOCATION, airport_code)
        # Verify pick_up and drop_off dates and time on trip viewer page
        assertions.element_text_should_contain_formatted_date(
            CarHireTabLocators.PICK_UP_DATE_TIME, trip_viewer_page_car_hire_tab.search_summary_datetime_format,
            pick_up_date, pick_up_time)
        assertions.element_text_should_contain_formatted_date(
            CarHireTabLocators.DROP_OFF_DATE_TIME, trip_viewer_page_car_hire_tab.search_summary_datetime_format,
            drop_off_date, drop_off_time)
        assertions.element_should_be_visible(CarHireTabLocators.TOTAL_PRICE)
        trip_viewer_page_car_hire_tab.element_interactions.click_element(CarHireTabLocators.ADD_TO_TRIP_BUTTON)
        # Move to the trip_viewer_page_overview_tab
        trip_viewer_page_overview_tab.element_interactions.click_element(
            OverviewTabLocators.TRIP_PLANNER_SIDEBAR_ITENERARY_BUTTON)
        # Verify the airport name to be correct
        assertions.element_should_contain_value(OverviewTabLocators.TRIP_PLANNER_SIDEBAR_PICK_UP_LOCATION, airport)
        # Verify pick_up and drop_off dates and time on overview tab of trip viewer page
        assertions.element_text_should_contain_formatted_date(
            OverviewTabLocators.TRIP_PLANNER_SIDEBAR_PICK_UP_DATE, trip_viewer_page_overview_tab.car_hire_date_format,
            pick_up_date, pick_up_time)
        assertions.element_text_should_contain_formatted_date(
            OverviewTabLocators.TRIP_PLANNER_SIDEBAR_DROP_OFF_DATE, trip_viewer_page_overview_tab.car_hire_date_format,
            drop_off_date, drop_off_time)
        assertions.element_should_contain_value(OverviewTabLocators.TRIP_PLANNER_SIDEBAR_PICK_UP_TIME,
                                                pick_up_time)
        # Verify the basket popup content
        trip_viewer_page_header.element_interactions.click_element(HeaderLocators.BASKET_ICON)
        trip_viewer_page_header.element_interactions.click_element(HeaderLocators.BASKET_POPUP_VIEW_DETAIL_BUTTON)
        # Verify the pickup location on basket popup
        assertions.element_should_contain_value(HeaderLocators.BASKET_POPUP_CAR_HIRE_PICK_UP_LOCATION,
                                                airport)
        # Verify the pickup and dropdown datetime on basket popup

        assertions.element_text_should_contain_formatted_date(
            HeaderLocators.BASKET_CAR_PICK_UP_DATETIME, trip_viewer_page_header.car_hire_datetime_format,
            pick_up_date, pick_up_time)
        assertions.element_text_should_contain_formatted_date(
            HeaderLocators.BASKET_CAR_DROP_OFF_DATETIME, trip_viewer_page_header.car_hire_datetime_format,
            drop_off_date, drop_off_time)
        assertions.element_should_be_visible(HeaderLocators.BASKET_POPUP_CAR_HIRE_PRICE)
        trip_viewer_page_header.element_interactions.click_element(HeaderLocators.BASKET_CHECKOUT_BUTTON)
        # Move to payment page
        # Verify the presence driver details input fields
        assertions.element_should_be_visible(PaymentPageLocators.DRIVER_DETAILS_TITLE_INPUT)
        assertions.element_should_be_visible(PaymentPageLocators.DRIVER_DETAILS_FIRST_INPUT)
        assertions.element_should_be_visible(PaymentPageLocators.DRIVER_DETAILS_LAST_INPUT)
        payment_page.element_interactions.click_element(PaymentPageLocators.CAR_VIEW_DETAILS_BUTTON)
        # Verify the pickup location
        assertions.element_should_contain_value(PaymentPageLocators.CAR_PICK_UP_LOCATION, airport)
        # Verify the pickup and dropdown datetime
        assertions.element_text_should_contain_formatted_date(
            PaymentPageLocators.CAR_PICK_UP_DATETIME, payment_page.car_hire_datetime_format,
            pick_up_date, pick_up_time)
        assertions.element_text_should_contain_formatted_date(
            PaymentPageLocators.CAR_DROP_OFF_DATETIME, payment_page.car_hire_datetime_format,
            drop_off_date, drop_off_time)
        payment_page.go_to_main_page()

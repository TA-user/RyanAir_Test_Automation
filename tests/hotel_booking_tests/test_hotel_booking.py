import pytest
from config import Urls
from tests.data.hotel_booking_data import Data
from tests.pages.hotel_page_locators import HotelPageLocators
from tests.pages.hotels_list_page_locators import HotelsListPageLocators
from tests.pages.room_booking_page_locators import RoomBookingPageLocators


@pytest.fixture(scope="function")
def setup(browser, main_page, hotel_main_page, username, password):
    main_page.open(Urls.MAIN_PAGE_URL)
    main_page.accept_cookies()
    main_page.log_in(username, password)
    yield
    hotel_main_page.log_out()


class TestHotelBooking:
    @pytest.mark.smoke
    @pytest.mark.hotel_booking
    @pytest.mark.parametrize("destination, check_in_date, check_out_date", Data.hotel_booking_data)
    def test_user_can_book_hotel(self, destination, check_in_date, check_out_date, assertions, setup, main_page,
                                 main_page_search_hotels_tab, hotels_list_page, hotel_page):
        main_page.open_search_hotel_tab()
        main_page_search_hotels_tab.perform_hotels_search(destination, check_in_date, check_out_date)
        hotels_list_page.accept_cookies()
        assertions.element_should_contain_value(HotelsListPageLocators.ACTUAL_DESTINATION, destination)
        assertions.element_should_contain_date(HotelsListPageLocators.ACTUAL_DATES, check_in_date)
        assertions.element_should_contain_date(HotelsListPageLocators.ACTUAL_DATES, check_out_date)
        hotels_list_page.choose_most_popular_hotel()
        assertions.element_should_contain_value(HotelPageLocators.ACTUAL_DESTINATION, destination)
        assertions.element_should_contain_date(HotelPageLocators.ACTUAL_DATES, check_in_date)
        assertions.element_should_contain_date(HotelPageLocators.ACTUAL_DATES, check_out_date)
        hotel_page.choose_cheapest_room()
        assertions.element_should_contain_date(RoomBookingPageLocators.ACTUAL_CHECK_IN_DATE, check_in_date)
        assertions.element_should_contain_date(RoomBookingPageLocators.ACTUAL_CHECK_OUT_DATE, check_out_date)

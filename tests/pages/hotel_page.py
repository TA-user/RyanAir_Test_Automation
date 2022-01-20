from tests.pages.hotel_main_page import HotelMainPage
from tests.pages.hotel_page_locators import HotelPageLocators


class HotelPage(HotelMainPage):
    def choose_cheapest_room(self):
        self.element_interactions.switch_to_new_tab()
        self.element_interactions.click_element(HotelPageLocators.BOOK_FIRST_ROOM_BUTTON)

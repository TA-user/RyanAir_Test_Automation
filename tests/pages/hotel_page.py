import allure
from tests.pages.hotel_main_page import HotelMainPage
from tests.pages.hotel_page_locators import HotelPageLocators
from utils.browser_helper import Tabs


class HotelPage(HotelMainPage):
    hotels_search_date_format = "%#d %b %Y"

    @allure.step('Choose cheapest room on hotel page')
    def choose_cheapest_room(self):
        self.element_interactions.switch_to_tab(Tabs.NEW)
        self.element_interactions.click_element(HotelPageLocators.BOOK_FIRST_ROOM_BUTTON)

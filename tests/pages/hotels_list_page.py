import allure
from tests.pages.hotel_main_page import HotelMainPage
from tests.pages.hotels_list_page_locators import HotelsListPageLocators


class HotelsListPage(HotelMainPage):
    hotels_search_date_format = "%#d %b %Y"

    @allure.step('Choose most popular hotel on hotels list page')
    def choose_most_popular_hotel(self):
        self.element_interactions.refresh_until_visible(HotelsListPageLocators.OPEN_FIRST_HOTEL_BUTTON)
        self.element_interactions.click_element(HotelsListPageLocators.OPEN_FIRST_HOTEL_BUTTON)

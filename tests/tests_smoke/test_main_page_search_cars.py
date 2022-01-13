from tests.pages.main_page import MainPage
from config import Urls


def test_user_can_hire_car(browser):
    main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
    main_page.open()
    main_page.click_accept_cookie_popup_button()
    main_page.open_search_cars_tab()


# def perform_car_sharing(main_page_car_hire_tab: MainPageCarHireTab, pick_up_location: str,
#                         pick_up_year_month_day: str, pick_up_time: str,
#                         drop_off_year_month_day: str, drop_off_time: str, button: str):
#     logger.info(f"pick_up_location: {pick_up_location}")
#     logger.info(f"pick_up_year_month_day: {pick_up_year_month_day}")
#     logger.info(f"pick_up_time: {pick_up_time}")
#     logger.info(f"drop_off_year_month_day: {drop_off_year_month_day}")
#     logger.info(f"drop_off_time: {drop_off_time}")
#
#     main_page_car_hire_tab.perform_car_sharing(pick_up_location, pick_up_year_month_day, pick_up_time,
#                                                drop_off_year_month_day, drop_off_time)
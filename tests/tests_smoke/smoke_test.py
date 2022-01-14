import time

from tests.pages.main_page_locators import MainPageHeaderLocators
from tests.pages.main_page_locators import LogInPopupLocators

def test_user_can_order_flights(browser, main_page, main_page_search_flights_tab):
    main_page.open()
    main_page.accept_cookie()
    main_page.element_interactions.click_element(MainPageHeaderLocators.LOG_IN_BUTTON)
    main_page.element_interactions.send_text_in_field(LogInPopupLocators.EMAIL_FORM, 'testuserintern@mail.ru')
    main_page.element_interactions.send_text_in_field(LogInPopupLocators.PASSWORD_FORM, 'ui89WFdd')
    main_page.element_interactions.click_element(LogInPopupLocators.CONFIRMATION_LOG_IN_BUTTON)
    main_page_search_flights_tab.perform_flights_search('Berlin Brandenburg', 'London Stansted', '2022-03-11', '2022-03-18')
    time.sleep(3)
    
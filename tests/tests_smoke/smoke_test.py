import time
import pytest
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


def test_user_can_order_flights(browser, main_page, main_page_search_flights_tab):
    main_page.open()
    main_page.accept_cookie()
    main_page.element_interactions.click_element(MainPageHeaderLocators.LOG_IN_BUTTON)
    main_page.element_interactions.send_text_in_field(LogInPopupLocators.EMAIL_FORM, 'testuserintern@mail.ru')
    main_page.element_interactions.send_text_in_field(LogInPopupLocators.PASSWORD_FORM, 'ui89WFdd')
    main_page.element_interactions.click_element(LogInPopupLocators.CONFIRMATION_LOG_IN_BUTTON)
    main_page_search_flights_tab.perform_flights_search('Berlin Brandenburg', 'London Stansted', '2022-03-11', '2022-03-18')
    time.sleep(3)

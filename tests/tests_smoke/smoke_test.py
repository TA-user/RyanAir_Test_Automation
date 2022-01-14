import pytest
from tests.pages.main_page_locators import MainPageHeaderLocators


@pytest.fixture(scope="function")
def setup(browser, main_page, user, password):
    main_page.open()
    main_page.accept_cookies()
    main_page.log_in(user, password)


def test_guest_can_log_in(setup, user, assertions):
    assertions.element_should_be_visible(MainPageHeaderLocators.USER_AVATAR)
    assertions.element_should_contain_phrase(MainPageHeaderLocators.USER_MENU, user)

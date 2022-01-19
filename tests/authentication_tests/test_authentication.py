import allure
import pytest
from config import Urls
from tests.pages.main_page_locators import MainPageHeaderLocators


@pytest.fixture(scope="function")
def setup(browser, main_page, username, password):
    main_page.open(Urls.MAIN_PAGE_URL)
    main_page.accept_cookies()
    main_page.log_in(username, password)
    yield
    main_page.log_out()


@allure.feature("Authorization")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.authorization
def test_guest_can_log_in(setup, username, assertions):
    assertions.element_should_be_visible(MainPageHeaderLocators.USER_AVATAR)
    assertions.element_should_contain_value(MainPageHeaderLocators.USER_MENU, username)

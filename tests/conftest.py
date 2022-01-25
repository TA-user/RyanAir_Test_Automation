import allure
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from utils.assertions import Assertions
from config import Capabilities
from config import DefaultCreds
from tests.pages.hotel_main_page import HotelMainPage
from tests.pages.hotel_page import HotelPage
from tests.pages.hotels_list_page import HotelsListPage
from tests.pages.main_page import MainPage, MainPageCarHireTab, MainPageSearchHotelsTab, MainPageSearchFlightsTab
from tests.pages.payment_page import PaymentPage
from tests.pages.room_booking_page import RoomBookingPage
from tests.pages.trip_viewer_page import TripViewerPageFlightsTab, TripViewerPageSeatsTab, TripViewerPageBagsTab, \
    TripViewerPageExtrasTab, TripViewerPage, TripViewerPageCarHireTab, TripViewerPageOverviewTab, TripViewerPageHeader


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser:chrome,firefox,opera or all. Options 'all' - only for selenoid launch mode")
    parser.addoption("--launch_mode", action="store", default="selenoid",
                     help="To run tests on local machine type local. Default - selenoid launch mode")
    parser.addoption('--username',
                     action='store',
                     default='None',
                     help="Set a username",
                     )
    parser.addoption('--password',
                     action='store',
                     default='None',
                     help="Set a password",
                     )



@pytest.fixture(scope="package", params=[Capabilities.chrome_97, Capabilities.firefox_96, Capabilities.opera_82])
def browser(request):
    browser_name = request.config.getoption("browser_name")
    launch_mode = request.config.getoption("launch_mode")

    if launch_mode == 'selenoid':
        if browser_name == "chrome":
            browser = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub", desired_capabilities=Capabilities.chrome_97)
        elif browser_name == "firefox":
            browser = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub", desired_capabilities=Capabilities.firefox_96)
        elif browser_name == "opera":
            browser = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub", desired_capabilities=Capabilities.opera_82)
            browser.set_window_position(2, 2)
        elif browser_name == 'all':
            browser = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub", desired_capabilities=request.param)
        browser.set_window_size(1920, 1080)

    elif launch_mode == 'local':
        if browser_name == "chrome":
            browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser_name == "firefox":
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "opera":
            browser = webdriver.Opera(executable_path=OperaDriverManager().install())
        browser.maximize_window()

    else:
        raise pytest.UsageError("--browser name should be chrome or firefox or opera")

    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture(scope="module")
def assertions(browser):
    return Assertions(browser=browser)


@pytest.fixture()
def username(request):
    commandline_username = request.config.getoption("username")
    if commandline_username == "None":
        commandline_username = DefaultCreds.USERNAME
    return commandline_username


@pytest.fixture()
def password(request):
    commandline_password = request.config.getoption("password")
    if commandline_password == "None":
        commandline_password = DefaultCreds.PASSWORD
    return commandline_password


@pytest.fixture(scope="module")
def main_page(browser):
    return MainPage(browser=browser)


@pytest.fixture(scope="module")
def main_page_search_flights_tab(browser):
    return MainPageSearchFlightsTab(browser=browser)


@pytest.fixture(scope="module")
def main_page_car_hire_tab(browser):
    return MainPageCarHireTab(browser=browser)


@pytest.fixture(scope="module")
def main_page_search_hotels_tab(browser):
    return MainPageSearchHotelsTab(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page_flights_tab(browser):
    return TripViewerPageFlightsTab(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page_seats_tab(browser):
    return TripViewerPageSeatsTab(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page_bags_tab(browser):
    return TripViewerPageBagsTab(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page_extras_tab(browser):
    return TripViewerPageExtrasTab(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page(browser):
    return TripViewerPage(browser=browser)


@pytest.fixture(scope="module")
def payment_page(browser):
    return PaymentPage(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page_car_hire_tab(browser):
    return TripViewerPageCarHireTab(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page_overview_tab(browser):
    return TripViewerPageOverviewTab(browser=browser)


@pytest.fixture(scope="module")
def trip_viewer_page_header(browser):
    return TripViewerPageHeader(browser=browser)


@pytest.fixture(scope="module")
def hotels_list_page(browser):
    return HotelsListPage(browser=browser)


@pytest.fixture(scope="module")
def hotel_page(browser):
    return HotelPage(browser=browser)


@pytest.fixture(scope="module")
def hotel_main_page(browser):
    return HotelMainPage(browser=browser)


@pytest.fixture(scope="module")
def room_booking_page(browser):
    return RoomBookingPage(browser=browser)

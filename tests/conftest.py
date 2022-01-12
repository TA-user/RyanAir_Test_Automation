import allure
import os
import pytest
from selenium import webdriver

from msedge.selenium_tools import Edge
from selene.support.shared import browser as selene_browser
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function', autouse=True)
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--window-size=1920,1080")
        chrome_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        selene_browser.config.driver = chrome_driver

    elif browser_name == "firefox":

        firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        firefox_driver.set_window_size(1920, 1080)

        selene_browser.config.driver = firefox_driver

    elif browser_name == "edge":
        desired_cap = {}
        edge_driver = Edge(EdgeChromiumDriverManager().install(), capabilities=desired_cap)
        edge_driver.set_window_size(1920, 1080)

        selene_browser.config.driver = edge_driver

    else:
        raise pytest.UsageError("--browser name should be chrome or firefox")
    yield selene_browser
    selene_browser.quit()


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

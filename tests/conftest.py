import allure
import os
import pytest
from msedge.selenium_tools import Edge
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox or edge")


@pytest.fixture(scope="package")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp,
                                    options=firefox_options)
    elif browser_name == "edge":
        desired_cap = {}
        browser = Edge(executable_path=EdgeChromiumDriverManager().install(),
                       desired_capabilities=desired_cap)
        browser.set_window_size(1920, 1080)

    else:
        raise pytest.UsageError("--browser name should be chrome or firefox or edge")
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

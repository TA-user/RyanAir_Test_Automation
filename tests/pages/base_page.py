import allure

from utils.browser_helper import ElementInteractions


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.element_interactions = ElementInteractions(self.browser)
    
    @allure.step('Driver get url - "{1}"')
    def open(self, url):
        self.browser.get(url)

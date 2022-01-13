from utils.browser_helper import ElementInteractions
from utils.assertions import Assertions


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.element_interactions = ElementInteractions(self.browser)
        self.assertions = Assertions()

    def open(self):
        self.browser.get(self.url)


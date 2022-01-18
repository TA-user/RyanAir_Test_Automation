from utils.browser_helper import ElementInteractions


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.element_interactions = ElementInteractions(self.browser)

    def open(self, url):
        self.browser.get(url)


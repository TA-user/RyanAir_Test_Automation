from utils.browser_helper import ElementInteractions


class BasePage:
    def __init__(self, browser, url, timeout=7):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.element_interactions = ElementInteractions(self.browser)

    def open(self):
        self.browser.get(self.url)

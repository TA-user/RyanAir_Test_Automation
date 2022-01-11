from loguru import logger
from selene import be
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotInteractableException, TimeoutException


class ElementInteractions:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, selector):
        logger.debug(f'Trying to find visible element "{selector}"...')
        try:
            element = self.browser.element(selector).should(be.visible)
        except NoSuchElementException or ElementNotVisibleException or ElementNotInteractableException \
                or TimeoutException:
            logger.error(f'Cannot find visible element "{selector}"!')
            raise
        logger.debug(f'Element "{selector}" was found...')
        return element

    def click_element(self, selector):
        element = self.browser.element(selector).should(be.clickable)
        logger.debug(f'Trying to click an element "{selector}"...')
        try:
            element.click()
        except NoSuchElementException or ElementNotVisibleException or ElementNotInteractableException \
                or TimeoutException:
            logger.error(f'Cannot click an element "{selector}"...')
            raise
        logger.debug(f'Element "{selector}" clicked...')

    def send_text_in_field(self, selector, text):
        element = self.browser.element(selector).should(be.blank)
        element.clear()
        logger.debug(f'Trying to send "{text}" in element "{selector}"...')
        try:
            element.type(text)
        except NoSuchElementException or ElementNotVisibleException or ElementNotInteractableException \
                or TimeoutException:
            logger.error(f'Cannot send {text} in element "{selector}"...')
            raise
        logger.debug(f'{text} is sent in element "{selector}"...')

    def clear_field(self, selector):
        element = self.browser.element(selector).should(be.clickable)
        try:
            element.clear()
        except NoSuchElementException or ElementNotVisibleException or ElementNotInteractableException \
                or TimeoutException:
            logger.error(f'Cannot clear element "{selector}"...')
            raise
        logger.debug(f'Field, located "{selector}" cleared...')

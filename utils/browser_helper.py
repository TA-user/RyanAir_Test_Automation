from loguru import logger
from selene import be
from selene.core.exceptions import TimeoutException
from utils.logging import Logger


class ElementInteractions:
    Logger.set_logger()

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, selector):
        try:
            element = self.browser.element(selector).should(be.visible)
        except TimeoutException:
            logger.error(f'Cannot find element "{selector}"!')
            raise
        logger.debug(f'Element "{selector}" was found...')
        return element

    def click_element(self, selector):
        element = self.find_element(selector)
        try:
            element.should(be.clickable).click()
        except TimeoutException:
            logger.error(f'Cannot click an element "{selector}"...')
            raise
        logger.debug(f'Element "{selector}" clicked...')

    def send_text_in_field(self, selector, text):
        element = self.find_element(selector)
        try:
            element.should(be.blank).type(text)
        except TimeoutException:
            logger.error(f'Cannot send {text} in element "{selector}"...')
            raise
        logger.debug(f'{text} is sent in element "{selector}"...')

    def clear_field(self, selector):
        element = self.find_element(selector)
        try:
            element.should(be.blank).clear()
        except TimeoutException:
            logger.error(f'Cannot clear element "{selector}"...')
            raise
        logger.debug(f'Field, located "{selector}" cleared...')

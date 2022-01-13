from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from utils.logging import Logger
from config import wait_time_s


class ElementInteractions:
    Logger.set_logger(Logger())

    def __init__(self, browser):
        self.browser = browser

    def find_visible_element(self, selector):
        try:
            element = WebDriverWait(self.browser, wait_time_s).until(EC.visibility_of_element_located(selector))
        except WebDriverException:
            logger.error(f'Cannot find visible element "{selector}"!')
            raise
        logger.debug(f'Element "{selector}" was found...')
        return element

    def find_clickable_element(self, selector):
        try:
            element = WebDriverWait(self.browser, wait_time_s).until(EC.element_to_be_clickable(selector))
        except WebDriverException:
            logger.error(f'Cannot find clickable element "{selector}"!')
            raise
        logger.debug(f'Element "{selector}" was found...')
        return element

    def click_element(self, selector):
        element = self.find_clickable_element(selector)
        try:
            element.click()
        except WebDriverException:
            logger.error(f'Cannot click an element "{selector}"...')
            raise
        logger.debug(f'Element "{selector}" clicked...')

    def send_text_in_field(self, selector, text):
        element = self.find_clickable_element(selector)
        element.clear()
        try:
            element.send_keys(text)
        except WebDriverException:
            logger.error(f'Cannot send {text} in element "{selector}"...')
            raise
        logger.debug(f'{text} is sent in element "{selector}"...')

    def clear_field(self, selector):
        element = self.find_clickable_element(selector)
        try:
            element.clear()
        except WebDriverException:
            logger.error(f'Cannot clear field, located "{selector}"...')
            raise
        logger.debug(f'Field, located "{selector}" cleared...')

    def find_element(self, selector):
        try:
            element = WebDriverWait(self.browser, wait_time_s).until(EC.presence_of_element_located(selector))
        except WebDriverException:
            logger.error(f'Cannot find element "{selector}" in DOM!')
            raise
        logger.debug(f'Element "{selector}" was found in DOM ...')
        return element

    def is_element_visible(self, selector):
        try:
            self.find_visible_element(selector)
        except WebDriverException:
            logger.error(f'Element "{selector}" is not visible!')
            return False
        logger.debug(f'Element "{selector}" is visible')
        return True

    def is_element_clickable(self, selector):
        try:
            self.find_clickable_element(selector)
        except WebDriverException:
            logger.error(f'Element "{selector}" is not clickable')
            return False
        logger.debug(f'Element "{selector}" is clickable')
        return True

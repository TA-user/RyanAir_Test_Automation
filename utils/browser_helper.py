from loguru import logger
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from utils.logging import Logger
from config import BrowserHelperSettings
from enum import Enum, IntEnum


class Tabs(Enum):
    NEW = -1
    MAIN = 0


class ElementInteractions:
    WAIT_TIME_SECS = BrowserHelperSettings.WAIT_TIME_SECS
    Logger.set_logger(Logger())

    def __init__(self, browser):
        self.browser = browser

    def find_visible_element(self, selector):
        try:
            element = WebDriverWait(self.browser, self.WAIT_TIME_SECS).until(EC.visibility_of_element_located(selector))
        except WebDriverException:
            logger.error(f'Cannot find visible element "{selector}"!')
            raise
        logger.debug(f'Element "{selector}" was found...')
        return element

    def find_visible_elements(self, selector):
        try:
            elements = WebDriverWait(self.browser, self.WAIT_TIME_SECS).until(
                EC.visibility_of_all_elements_located(selector))
        except WebDriverException:
            logger.error(f'Not all elements "{selector}" are visible')
            raise
        logger.debug(f'Visible elements "{selector}" was found')
        return elements

    def find_clickable_element(self, selector):
        try:
            element = WebDriverWait(self.browser, self.WAIT_TIME_SECS).until(EC.element_to_be_clickable(selector))
        except WebDriverException:
            logger.error(f'Cannot find clickable element "{selector}"!')
            raise
        logger.debug(f'Element "{selector}" was found...')
        return element

    def find_element_by_text(self, text):
        locator = (By.XPATH, f"//*[text()='{text}']")
        try:
            element = WebDriverWait(self.browser, self.WAIT_TIME_SECS).until(EC.presence_of_element_located(locator))
        except WebDriverException:
            logger.error(f'Cannot find element "{locator}" in DOM!')
            raise
        logger.debug(f'Element "{locator}" was found in DOM ...')
        return element

    def find_element_by_partial_text_match(self, text):
        locator = (By.XPATH, f"//*[contains(text(),'{text}')]")
        try:
            element = WebDriverWait(self.browser, self.WAIT_TIME_SECS).until(EC.presence_of_element_located(locator))
        except WebDriverException:
            logger.error(f'Cannot find element "{locator}" in DOM!')
            raise
        logger.debug(f'Element "{locator}" was found in DOM ...')
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
            element.click()
            element.clear()
        except WebDriverException:
            logger.error(f'Cannot clear field, located "{selector}"...')
            raise
        logger.debug(f'Field, located "{selector}" cleared...')

    def find_element(self, selector):
        try:
            element = WebDriverWait(self.browser, self.WAIT_TIME_SECS).until(EC.presence_of_element_located(selector))
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

    def click_at_left_top_element_corner(self, selector):
        try:
            element = self.find_clickable_element(selector)
            webdriver.ActionChains(self.browser).move_to_element_with_offset(element, xoffset=10,
                                                                             yoffset=10).click().perform()
        except WebDriverException:
            logger.error(f'Cannot click at left top corner of element "{selector}"')
            raise
        logger.debug(f'Element "{selector}" clicked at at left top corner')

    def refresh_page(self):
        self.browser.refresh()
        logger.debug(f'Page refreshed...')

    def switch_to_tab(self, tab):
        self.browser.switch_to.window(self.browser.window_handles[tab])
        logger.debug(f'Switched to "{tab}" tab...')

    def refresh_until_visible(self, selector):
        class TestFailed(Exception):
            def __init__(self, m):
                self.message = m

            def __str__(self):
                return self.message

        i = 1
        while not self.is_element_visible(selector):
            self.refresh_page()
            i += 1
            if i == 5:
                logger.error(f'Element is still invisible after several refreshes!')
                raise TestFailed("Element is still invisible after several refreshes!")

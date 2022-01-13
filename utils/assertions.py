import allure
from assertpy import assert_that
from loguru import logger
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logging import Logger


class Assertions:
    """
    Example usage from test layer
    Assertions.element_should_be_clickable(browser, MainPageLocators.ADD_ITEM)
    Assertions.element_should_be_visible(browser, MainPageHeaderLocators.USER_MENU)
    Assertions.element_should_contain_text(browser, MainPageHeaderLocators.USER_MENU, 'user')
    Assertions.phrase_should_contain_element_text(browser, MainPageHeaderLocators.USER_MENU, 'user')
    """

    Logger.set_logger(Logger())

    @allure.step('Verification visibility "{1}" element')
    def element_should_be_visible(browser, locator):
        logger.info(f'Verification visibility "{locator}" element')
        try:
            required_element = WebDriverWait(browser, timeout=5).until(EC.visibility_of_element_located(locator))
        except WebDriverException:
            required_element = None
            logger.error(f'Element "{locator}" is not visible at page')
        assert_that(required_element, description=f'Required element {locator} is not present').is_not_none()

    @allure.step('Verification clickability "{1}" element')
    def element_should_be_clickable(browser, locator):
        logger.info(f'Verification clickability "{locator}" element')
        try:
            required_element = WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable(locator))
        except WebDriverException:
            required_element = None
            logger.error(f'Element "{locator}" is not clickable')
        assert_that(required_element, description=f'Element {locator} is not clickable').is_not_none().is_true()

    @allure.step('Verification that element "{1}" contain text - "{2}"')
    def element_should_contain_text(browser, locator, phrase):
        required_element = WebDriverWait(browser, timeout=5).until(EC.visibility_of_element_located(locator))
        logger.info(f'Verification that element "{locator}" contain text - "{phrase}"')
        assert_that(required_element.text, description="Element don't contain required phrase").contains(phrase)

    @allure.step('Verification that given phrase "{2}" contain text from element - "{1}"')
    def phrase_should_contain_element_text(browser, locator, phrase):
        required_element = WebDriverWait(browser, timeout=5).until(EC.visibility_of_element_located(locator))
        logger.info(f'Verification that given phrase "{phrase}" contain text from element - "{locator}"')
        assert_that(phrase, description="Element don't contain required phrase").contains(required_element.text)

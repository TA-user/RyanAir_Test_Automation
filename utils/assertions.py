import allure
from selene import be, have
from loguru import logger
from utils.logging import Logger


class Assertions:
    Logger.set_logger()
    
    @allure.step('Verification visibility "{1}" element')
    def element_should_be_visible(browser, *locator):
        required_element = browser.element(locator)
        # logger.info(f'Verification visibility "{locator}" element')
        required_element.should(be.visible)
        
        
    @allure.step('Verification that element "{1}" contain text - "{2}"')
    def element_should_contain_text(browser, *locator, phrase=str):
        required_element = browser.element(locator)
        # logger.info(f'Verification that element "{locator}" contain text - "{phrase}"')
        required_element.should(have.text(f'{phrase}'))


    @allure.step('Verification clickability of "{1}" element')
    def element_should_be_clickable(browser, *locator):
        required_element = browser.element(locator)
        # logger.info(f'Verification clickability of "{locator}" element')
        required_element.should(be.clickable)

        
    
    
    
    # def phrase_should_contain_text(browser, *locator, phrase=str):
    #     required_element = BrowserHelper.find_visible_element(browser, *locator)
    #     actual_text = required_element.text
    #     assert actual_text in f"{phrase}", "Actual text of element isn't part of given phrase"
    
    # def elements_should_not_contain_phrase(browser, *locator, phrase=str):
    #     required_elements = BrowserHelper.find_visible_elements(browser, *locator)
    #     for element in required_elements:
    #         assert phrase not in element.text, "Element contain phrase but should not"
    
    # @allure.step("Verification of correct URL of page")
    # def should_be_correct_url(browser, url_identifier=str):
    #     assert f"{url_identifier}" in browser.current_url, "Url of that page don't contains url phrase"

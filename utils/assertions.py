import allure
from assertpy import assert_that
from utils.browser_helper import ElementInteractions
from utils.text_formatter import TextFormatter


class Assertions(ElementInteractions):
    """
    Object instance of Assertions class should initialize in BasePage class. And it would be used by perforce.
    Example usage:
    assertions.element_should_be_clickable(MainPageLocators.ADD_ITEM)
    assertions.element_should_contain_text(MainPageHeaderLocators.USER_MENU, 'username')
    """

    @allure.step('Verification of visibility "{1}" element')
    def element_should_be_visible(self, locator):
        element_visibility = self.is_element_visible(locator)
        assert_that(element_visibility, description=f'Required element {locator} is not visible').is_true()

    @allure.step('Verification clickability "{1}" element')
    def element_should_be_clickable(self, locator):
        element_clickability = self.is_element_clickable(locator)
        assert_that(element_clickability, description=f'Required element {locator} is not clickable').is_true()

    @allure.step('Verification that text of visible element "{1}" contain phrase - "{2}"')
    def element_should_contain_value(self, locator, phrase):
        required_element = self.find_visible_element(locator)
        assert_that(required_element.text, description="Visible element don't contain required phrase").contains(phrase)
        
    @allure.step('Verification that text of element "{1}" is in formatted date "{2}"')
    def date_should_contain_element(self, locator, date):
        date_object = TextFormatter.date_formatter(date)
        required_date = (date_object.day + date_object.month_name + date_object.month_number + date_object.year)
        required_element = self.find_visible_element(locator)
        element_text = required_element.text.replace(' ', '')
        assert_that(required_date, description="Formatted date doesn't contain text of element").contains(element_text)

    @allure.step('Verification that element contain "{1}" formatted date "{2}"')
    def element_should_contain_date(self, locator, date):
        date_object = TextFormatter.date_formatter(date)
        required_date = (date_object.day + date_object.month_name)
        required_element = self.find_visible_element(locator)
        element_text = required_element.text.replace(' ', '')
        assert_that(element_text, description="Text of element doesn't contain given date").contains(required_date)


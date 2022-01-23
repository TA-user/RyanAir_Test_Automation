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

    @allure.step('Verification of element "{1}" visibility')
    def element_should_be_visible(self, locator):
        element_visibility = self.is_element_visible(locator)
        assert_that(element_visibility, description=f'Required element {locator} is not visible').is_true()

    @allure.step('Verification of element "{1}" clickability')
    def element_should_be_clickable(self, locator):
        element_clickability = self.is_element_clickable(locator)
        assert_that(element_clickability, description=f'Required element {locator} is not clickable').is_true()

    @allure.step('Verification that text of visible element "{1}" contain value - "{2}"')
    def element_should_contain_value(self, locator, value):
        required_element = self.find_visible_element(locator)
        assert_that(required_element.text, description="Visible element don't contain required phrase").contains(value)

    @allure.step('Verification that text of element contain "{1}" formatted date "{2}"')
    def element_should_contain_date(self, locator, date):
        date_object = TextFormatter.format_date(date)
        required_date = (date_object.day + date_object.month_name)
        required_element = self.find_visible_element(locator)
        element_text = required_element.text.replace(' ', '')
        assert_that(element_text, description="Text of element doesn't contain given date").contains(required_date)

    @allure.step('Verification that text of element "{1}" contain date "{3}" in format "{2}"')
    def element_text_should_contain_formatted_date(self, locator, date_format: str, date: str):
        formatted_date = TextFormatter.format_date(date_format, date)
        required_element = self.find_visible_element(locator)
        assert_that(required_element.text,
                    description="Text of element doesn't contain expected formatted date").contains(formatted_date)

    @allure.step('Verification that text of element "{1}" contain date "{3}" and time {4} in format "{2}"')
    def element_text_should_contain_formatted_datetime(self, locator, datetime_format: str, date: str, time: str):
        formatted_datetime = TextFormatter.format_date_time(datetime_format, date, time)
        required_element = self.find_visible_element(locator)
        assert_that(required_element.text,
                    description="Text of element doesn't contain expected formatted datetime").contains(
            formatted_datetime)

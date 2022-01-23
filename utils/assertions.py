import allure
from assertpy import assert_that

from utils.browser_helper import ElementInteractions
from utils.text_formatter import TextFormatter


class Assertions(ElementInteractions):
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
        assert_that(required_element.text,
                    description=f"Visible element {locator} doesn't contain required value - {value}").contains(value)

    @allure.step('Verification that text of element "{1}" contain date "{3}" in format "{2}"')
    def element_text_should_contain_formatted_date(self, locator, date_format: str, date: str):
        formatted_date = TextFormatter.format_date(date_format, date)
        required_element = self.find_visible_element(locator)
        assert_that(required_element.text,
                    description=f"Text of element {locator} doesn't contain expected formatted date {date}").contains(
            formatted_date)

    @allure.step('Verification that text of element "{1}" contain date "{3}" and time {4} in format "{2}"')
    def element_text_should_contain_formatted_datetime(self, locator, datetime_format: str, date: str, time: str):
        formatted_datetime = TextFormatter.format_date_time(datetime_format, date, time)
        required_element = self.find_visible_element(locator)
        assert_that(required_element.text,
                    description=f"Text of element {locator} doesn't contain expected formatted date {date} or time {time}").contains(
            formatted_datetime)

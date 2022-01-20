from selenium.webdriver.common.by import By


class HotelsListPageLocators:
    OPEN_FIRST_HOTEL_BUTTON = (By.XPATH, "(//*[contains(@class, 'accommodation-card-body__choose')])[1]")
    ACTUAL_DESTINATION = (By.CSS_SELECTOR, "span.search-summary__destination")
    ACTUAL_DATES = (By.CSS_SELECTOR, "span.search-summary__dates")

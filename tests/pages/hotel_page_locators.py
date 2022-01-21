from selenium.webdriver.common.by import By


class HotelPageLocators:
    BOOK_FIRST_ROOM_BUTTON = (By.XPATH, "//*[contains(@class, 'room-card__book')]")
    ACTUAL_DESTINATION = (By.CSS_SELECTOR, "span.search-summary__destination")
    ACTUAL_DATES = (By.CSS_SELECTOR, "span.search-summary__dates")

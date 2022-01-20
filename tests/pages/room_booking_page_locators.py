from selenium.webdriver.common.by import By


class RoomBookingPageLocators:
    ACTUAL_CHECK_IN_DATE = (By.XPATH, "//span[contains(text(),'Check in')]/following-sibling::h5")
    ACTUAL_CHECK_OUT_DATE = (By.XPATH, "//span[contains(text(),'Check out')]/following-sibling::h5")


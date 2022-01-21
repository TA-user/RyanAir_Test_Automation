from selenium.webdriver.common.by import By


class HotelMainPageHeaderLocators:
    LOG_OUT_BUTTON = (By.XPATH, "//div/a[contains(text(),'Log out')]")
    USER_MENU = (By.CSS_SELECTOR, "button.user-controls__user-btn")


class HotelMainPageLocators:
    ACCEPT_COOKIES_BUTTON = (
        By.XPATH, "//div[@id='cookie-popup-with-overlay']//button[@class='cookie-popup-with-overlay__button']")

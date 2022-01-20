from selenium.webdriver.common.by import By


class HotelMainPageHeaderLocators:
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, "div.user-controls__menu > a:nth-child(3)")
    USER_MENU = (By.CSS_SELECTOR, "button.user-controls__user-btn")


class HotelMainPageLocators:
    ACCEPT_COOKIES_BUTTON = (
        By.XPATH, "//div[@id='cookie-popup-with-overlay']//button[@class='cookie-popup-with-overlay__button']")

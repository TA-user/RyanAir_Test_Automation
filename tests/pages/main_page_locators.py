from selenium.webdriver.common.by import By


class LogInPopupLocators:
    CONFIRMATION_LOG_IN_BUTTON = (By.XPATH, "//form[@data-ref='login_modal']//button[@type='submit']")
    EMAIL_FORM = (By.XPATH, "//input[@placeholder='email@email.com']")
    PASSWORD_FORM = (By.XPATH, "//input[@placeholder='Password']")


class MainPageLocators:

    ACCEPT_COOKIES_BUTTON = (By.XPATH, """//div[@id='cookie-popup-with-overlay']//button
        [@class='cookie-popup-with-overlay__button']""")
    FRAME_DATEPICKER = (By.XPATH, "//iframe[@id='_hjRemoteVarsFrame']")
    SEARCH_CARS_TAB = (By.XPATH, "//hp-search-widget-tab[@iconid='glyphs/cars']")
    SEARCH_FLIGHTS_TAB = (By.XPATH, "//hp-search-widget-tab[@iconid='glyphs/plane']")
    SEARCH_HOTELS_TAB = (By.XPATH, "//hp-search-widget-tab[@iconid='glyphs/hotels']")


class MainPageHeaderLocators:
    LOG_IN_BUTTON = (By.XPATH, "//button[@aria-label='Log in']")
    LOG_OUT_BUTTON = (By.XPATH, "//a[@data-ref='header-dropdown-user__logout']")
    USER_MENU = (By.XPATH, "//button[@data-ref='header-menu-item__toggle-button']/hp-header-menu-user")


class SearchCarsTabLocators:
    CAR_LOCATION = (By.XPATH, "//*[@id='input-button__pick-up-location']")
    DROP_OFF_FORM = (By.XPATH, "//hp-input-button[@uniqueid='drop-off-date']")
    DROP_OFF_TIME_FORM = (By.XPATH, "//hp-input-button[@uniqueid='drop-off-time']")
    FIRST_ITEM_LOCATION_DROPDOWN = (By.XPATH, "//hp-car-hire-location/div[1]")
    PICK_UP_FORM = (By.XPATH, "//hp-input-button[@uniqueid='pick-up-date']")
    PICK_UP_TIME_FORM = (By.XPATH, "//hp-input-button[@uniqueid='pick-up-time']")
    SEARCH_CARS_BUTTON = (By.XPATH, "//button[@data-ref='car-hire-widget__cta']")


class SearchFlightsTabLocators:
    DEPART_LOCATION = (By.XPATH, "//*[@id='input-button__departure']")
    DESTINATION_LOCATION = (By.XPATH, "//input[@id='input-button__destination']")
    LAST_ITEM_DROPDOWN_AIRPORT = (By.XPATH, "(//span[@data-ref='airport-item__name'])[last()]")
    DEPART_FORM = (By.CSS_SELECTOR, "fsw-input-button[uniqueid='dates-from'] div.input-button__input")
    RETURN_FORM = (By.XPATH, "//fsw-input-button[@uniqueid='dates-to']")
    SEARCH_FLIGHT_BUTTON = (By.XPATH, "//button[@data-ref='flight-search-widget__cta']")


class SearchHotelsTabLocators:
    CHECK_IN_FORM = (By.XPATH, "//hp-input-button[@uniqueid='check-in']")
    CHECK_OUT_FORM = (By.XPATH, "//hp-input-button[@uniqueid='check-out']")
    FIRST_ITEM_HOTEL_DROPDOWN = (By.XPATH, "//icon[@iconid='glyphs/destination-pin']")
    DESTINATION_HOTEL_FORM = (By.XPATH, "//*[@id='input-button__locations-or-properties']")
    SEARCH_HOTEL_BUTTON = (By.XPATH, "//button[@data-ref='rooms-search-widget__cta']")


class CarHirePageLocators:
    PICK_UP_DAY = (By.CSS_SELECTOR, "td.ab-SearchSummary_PickUp-day")
    PICK_UP_CITY = (By.CSS_SELECTOR, "div.ab-SearchSummary_PickUp_City")
    PICK_UP_HOUR = (By.CSS_SELECTOR, "td.ab-SearchSummary_PickUp-hour")
    PICK_UP_MINUTE = (By.CSS_SELECTOR, "div.ab-SearchSummary_PickUp-minute")
    DROP_OFF_DAY = (By.CSS_SELECTOR, "td.ab-SearchSummary_DropOff-day")
    DROP_OFF_CITY = (By.CSS_SELECTOR, "div.ab-SearchSummary_DropOff_City")
    DROP_OFF_HOUR = (By.CSS_SELECTOR, "td.ab-SearchSummary_DropOff-hour")
    DROP_OFF_MINUTE = (By.CSS_SELECTOR, "div.ab-SearchSummary_DropOff-minute")
    CHEAPEST_CARS_BUTTON = (By.CSS_SELECTOR, "tbody .price-from > a")
    FIRST_CAR_VIEW_DEAL_BUTTON = (By.CSS_SELECTOR, "div:nth-child(8) > table td.carResultRow_OfferInfo-toolbar > a")


class CalendarWidgetLocators:
    CHOOSE_MONTH_BUTTON_LOCATOR_PATTERN = "//div[text()=' {month} ']"  # Jan
    CHOOSE_DAY_OF_MONTH_LOCATOR_PATTERN = "[data-id='{date}']"  # date yyyy-mm-dd
    TIME_DDM_ELEMENT_PATTERN = "//ry-tooltip[@role='tooltip']//*[text()='{time}']"

    @classmethod
    def get_calendar_month_button_locator(cls, month: str) -> tuple:
        return By.XPATH, cls.CHOOSE_MONTH_BUTTON_LOCATOR_PATTERN.format(month=month.title())

    @classmethod
    def get_calendar_day_button_locator(cls, date: str) -> tuple:
        return By.CSS_SELECTOR, cls.CHOOSE_DAY_OF_MONTH_LOCATOR_PATTERN.format(date=date)

    @classmethod
    def get_time_in_ddm_locator(cls, time_="00:00") -> tuple:
        return By.XPATH, cls.TIME_DDM_ELEMENT_PATTERN.format(time=time_)

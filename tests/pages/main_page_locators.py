from selene import by


class LogInPopupLocators:
    CONFIRMATION_LOG_IN_BUTTON = (by.xpath("//form[@data-ref='login_modal']//button[@type='submit']"))
    EMAIL_FORM = (by.xpath("//input[@placeholder='email@email.com']"))
    PASSWORD_FORM = (by.xpath("//input[@placeholder='Password']"))


class MainPageLocators:
    ACCEPT_COOKIES_BUTTON = (by.xpath("""//div[@id='cookie-popup-with-overlay']//button
        [@class='cookie-popup-with-overlay__button']"""))
    FRAME_DATEPICKER = (by.xpath("//iframe[@id='_hjRemoteVarsFrame']"))
    SEARCH_CARS_TAB = (by.xpath("//hp-search-widget-tab[@iconid='glyphs/cars']"))
    SEARCH_FLIGHTS_TAB = (by.xpath("//hp-search-widget-tab[@iconid='glyphs/plane']"))
    SEARCH_HOTELS_TAB = (by.xpath("//hp-search-widget-tab[@iconid='glyphs/hotels']"))


class MainPageHeaderLocators:
    LOG_IN_BUTTON = (by.xpath("//button[@aria-label='Log in']"))
    LOG_OUT_BUTTON = (by.xpath("//a[@data-ref='header-dropdown-user__logout']"))
    USER_MENU = (by.xpath("//button[@data-ref='header-menu-item__toggle-button']/hp-header-menu-user"))


class SearchCarsTabLocators:
    CAR_LOCATION = (by.xpath("//*[@id='input-button__pick-up-location']"))
    DROP_OFF_FORM = (by.xpath("//hp-input-button[@uniqueid='drop-off-date']"))
    DROP_OFF_TIME_FORM = (by.xpath("//hp-input-button[@uniqueid='drop-off-time']"))
    FIRST_ITEM_LOCATION_DROPDOWN = (by.xpath("//hp-car-hire-location/div[1]"))
    PICK_UP_FORM = (by.xpath("//hp-input-button[@uniqueid='pick-up-date']"))
    PICK_UP_TIME_FORM = (by.xpath("//hp-input-button[@uniqueid='pick-up-time']"))
    SEARCH_CARS_BUTTON = (by.xpath("//button[@data-ref='car-hire-widget__cta']"))


class SearchFlightsTabLocators:
    INPUT_DEPARTURE_FORM = (by.xpath("//*[@id='input-button__departure']"))
    INPUT_DESTINATION_FORM = (by.xpath("//input[@id='input-button__destination']"))
    LAST_ITEM_DROPDOWN_AIRPORT = (by.xpath("(//span[@data-ref='airport-item__name'])[last()]"))
    RETURN_FORM = (by.xpath("//fsw-input-button[@uniqueid='dates-to']"))
    SEARCH_FLIGHT_BUTTON = (by.xpath("//button[@data-ref='flight-search-widget__cta']"))


class SearchHotelsTabLocators:
    CHECK_IN_FORM = (by.xpath("//hp-input-button[@uniqueid='check-in']"))
    CHECK_OUT_FORM = (by.xpath("//hp-input-button[@uniqueid='check-out']"))
    FIRST_ITEM_HOTEL_DROPDOWN = (by.xpath("//icon[@iconid='glyphs/destination-pin']"))
    DESTINATION_HOTEL_FORM = (by.xpath("//*[@id='input-button__locations-or-properties']"))
    SEARCH_HOTEL_BUTTON = (by.xpath("//button[@data-ref='rooms-search-widget__cta']"))

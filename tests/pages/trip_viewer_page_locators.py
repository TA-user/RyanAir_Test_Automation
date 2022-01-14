from selenium.webdriver.common.by import By


class FlightsTabLocators:
    FLIGHT_CARDS = (By.XPATH, "//flight-card")
    FLIGHT_HEADER_SUMMARY = (By.XPATH, "//flights-trip-details/div")
    ACTUAL_DEPART_LOCATION = (By.XPATH, "(//flights-trip-details/div//h4)[1]")
    ACTUAL_DESTINATION_LOCATION = (By.XPATH, "(//flights-trip-details/div//h4)[last()]")
    FLIGHT_DEPART_PRICES = (By.CSS_SELECTOR, "journey-container[data-ref='outbound'] span[data-e2e='flight-card-price']")
    FLIGHT_RETURN_PRICES = (By.CSS_SELECTOR, "journey-container[data-ref='inbound'] span[data-e2e='flight-card-price']")
    LIGHT_TYPE_CONTINUE_BUTTON = (By.CSS_SELECTOR, "div.fare-card--primary button.fare-card__button")
    CONFIRMATION_VALUE_FARE = (By.CSS_SELECTOR, "button[data-e2e='value']")
    PASSENGER_TITLE = (By.CSS_SELECTOR, "button[type='button']")
    MR_PASSENGER_TITLE = (By.CSS_SELECTOR, "ry-dropdown-item[data-ref='title-item-0'] button.dropdown-item__link")
    FIRST_NAME_PASSENGER_INPUT = (By.CSS_SELECTOR, "input[name='form.passengers.ADT-0.name']")
    LAST_NAME_PASSENGER_INPUT = (By.CSS_SELECTOR, "input[name='form.passengers.ADT-0.surname']")
    PASSENGERS_CONTINUATION_BUTTON = (By.CSS_SELECTOR, "button.continue-flow__button")

class HeaderLocators:
    BASKET_ICON = (By.CSS_SELECTOR, "div.basket-total")
    USER_MENU_DROPDOWN = (By.XPATH, "//logged-in")
    LOG_OUT_BUTTON = (By.XPATH, "//ry-log-out-button//button")
    MAIN_LOGO = (By.XPATH, "//icon[@class='ry-header__logo']")
    FLIGHT_CONFIRMATION_POPUP = (By.CSS_SELECTOR, "ry-tooltip-1")
    CLOSE_CONFIRMATION_POPUP_BUTTON = (By.CSS_SELECTOR, "icon[data-ref='tooltip-close-icon']")


class BagsTabLocators:
    ONE_SMALL_BAG_RADIOBUTTON = (By.CSS_SELECTOR, "bags-small-bag-pax-control ry-radio-circle-button")
    BAGS_CONTINUATION_BUTTON = (By.CSS_SELECTOR, "bags-continue-flow button")
    BAG_POPUP_DECLINE_BUTTON = (By.CSS_SELECTOR, "button.enhanced-takeover__product-dismiss-cta")


class ExtrasTabLocators:
    EXTRAS_TRIP_CONTINUATION_BUTTON = (By.CSS_SELECTOR, "airport-and-flight-container + button")
    EXTRAS_TRANSPORT_CONTINUATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")


class SeatsTabLocators:
    SEATS_LATER_OPTION_BUTTON = (By.CSS_SELECTOR, "button.seats-v2-navigation__button.h4")
    WITHOUT_SEATS_CONTINUATION_BUTTON = (By.CSS_SELECTOR, "button.ry-button--gradient-yellow")


class TripPlannerLocators:
    TRIP_PLANER_SIDEBAR = (By.CSS_SELECTOR, "div.trip-planner-container__content")
    DEPART_DATE = (By.CSS_SELECTOR, "span[data-ref='details-header-start-date']")
    RETURN_DATE = (By.CSS_SELECTOR, "span[data-ref='details-header-end-date']")
    DEPART_FLIGHT_LOCATIONS = (By.CSS_SELECTOR, "div.pillar-tab-details__extra-info-title:first-of-type")
    RETURN_FLIGHT_LOCATIONS = (By.CSS_SELECTOR, "div.pillar-tab-details__extra-info-title:nth-of-type(3)")
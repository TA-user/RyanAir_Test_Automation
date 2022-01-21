from selenium.webdriver.common.by import By


class FlightsTabLocators:
    FLIGHT_CARDS = (By.XPATH, "//flight-card")
    FLIGHT_HEADER_SUMMARY = (By.XPATH, "//flights-trip-details/div")
    ACTUAL_DEPART_LOCATION = (By.XPATH, "(//flights-trip-details/div//h4)[1]")
    ACTUAL_DESTINATION_LOCATION = (By.XPATH, "(//flights-trip-details/div//h4)[last()]")
    ACTUAL_DATES_DESCRIPTION = (By.CSS_SELECTOR, "div.details__bottom-bar")
    FLIGHT_DEPART_PRICES = (
        By.CSS_SELECTOR, "journey-container[data-ref='outbound'] span[data-e2e='flight-card-price']")
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
    MAIN_LOGO = (By.CSS_SELECTOR, "icon.ry-header__logo span svg")
    FLIGHT_CONFIRMATION_POPUP = (By.CSS_SELECTOR, "trip-basket-tooltip")
    CLOSE_CONFIRMATION_POPUP_BUTTON = (By.CSS_SELECTOR, "icon[data-ref='tooltip-close-icon']")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "span.basket-total-price")

    BASKET_POPUP_VIEW_DETAIL_BUTTON = (By.CSS_SELECTOR, ".exp-panel__title-tabindex-wrapper [role=button]")
    BASKET_POPUP_CAR_HIRE_PICK_UP_LOCATION = (By.CSS_SELECTOR, "[data-ref$=location-pickUp]")
    BASKET_CAR_PICK_UP_DATETIME = (By.CSS_SELECTOR, "[data-ref$='date-pickUp']")
    BASKET_CAR_DROP_OFF_DATETIME = (By.CSS_SELECTOR, "[data-ref$='date-dropOff']")
    BASKET_POPUP_CAR_HIRE_PRICE = (By.CSS_SELECTOR, "h4>*>.price__integers")
    BASKET_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-ref=basket-continue-flow__check-out]")

    BASKET_DEPART_LOCATION_FIRST_FLIGHT = (
        By.CSS_SELECTOR, "div[data-ref='outbound'] div.flight-details span:nth-child(1)")
    BASKET_DESTINATION_LOCATION_FIRST_FLIGHT = (
        By.CSS_SELECTOR, "div[data-ref='outbound'] div.flight-details span:nth-child(3)")
    BASKET_DEPART_LOCATION_SECOND_FLIGHT = (
        By.CSS_SELECTOR, "div[data-ref='inbound'] div.flight-details span:nth-child(1)")
    BASKET_DESTINATION_LOCATION_SECOND_FLIGHT = (
        By.CSS_SELECTOR, "div[data-ref='inbound'] div.flight-details span:nth-child(3)")
    BASKET_FIRST_FLIGHT_DATE = (
        By.CSS_SELECTOR, "div[data-ref='outbound'] div.flight-segment-details span:nth-child(1)")
    BASKET_SECOND_FLIGHT_DATE = (
        By.CSS_SELECTOR, "div[data-ref='inbound'] div.flight-segment-details span:nth-child(1)")


class BagsTabLocators:
    ONE_SMALL_BAG_RADIOBUTTON = (By.CSS_SELECTOR, "bags-small-bag-pax-control ry-radio-circle-button")
    BAGS_CONTINUATION_BUTTON = (By.CSS_SELECTOR, "bags-continue-flow button")
    BAG_POPUP_DECLINE_BUTTON = (By.CSS_SELECTOR, "button.enhanced-takeover__product-dismiss-cta")


class ExtrasTabLocators:
    EXTRAS_TRIP_CONTINUATION_BUTTON = (By.CSS_SELECTOR, "airport-and-flight-container + button")
    EXTRAS_TRANSPORT_CONTINUATION_BUTTON = (By.CSS_SELECTOR,
                                            "parking-container + div + button.app-container__cta.ry-button--gradient-yellow.ry-button--large")
    TRANSPORT_INFO_CARD = (By.CSS_SELECTOR, "transfer-card transport-info-card")
    DECLINE_POPUP_EXTRAS_BUTTON = (By.CSS_SELECTOR, 
                                   "div[data-ref='enhanced-takeover-desktop__INFLIGHT_ENHANCED_TAKEOVER'] button[color='anchor-blue']")


class SeatsTabLocators:
    SEATS_LATER_OPTION_BUTTON = (By.CSS_SELECTOR, "button.seats-v2-navigation__button.h4")
    WITHOUT_SEATS_CONTINUATION_BUTTON = (By.CSS_SELECTOR, "button.ry-button--gradient-yellow")


class TripPlannerLocators:
    TRIP_PLANER_SIDEBAR = (By.CSS_SELECTOR, "div.trip-planner-container__content")
    DEPART_DATE = (By.CSS_SELECTOR, "span[data-ref='details-header-start-date']")
    RETURN_DATE = (By.CSS_SELECTOR, "span[data-ref='details-header-end-date']")
    DEPART_LOCATION_FIRST_FLIGHT = (
        By.CSS_SELECTOR, "span[data-ref='pillar-tab-details-getting-there-outbound-origin']")
    DESTINATION_LOCATION_FIRST_FLIGHT = (
        By.CSS_SELECTOR, "span[data-ref='pillar-tab-details-getting-there-outbound-destination']")
    DEPART_LOCATION_SECOND_FLIGHT = (
        By.CSS_SELECTOR, "span[data-ref='pillar-tab-details-getting-there-outbound-origin']")
    DESTINATION_LOCATION_SECOND_FLIGHT = (
        By.CSS_SELECTOR, "span[data-ref='pillar-tab-details-getting-there-outbound-destination']")


class OverviewTabLocators:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-ref='trip-overview-container-checkout-button']")
    TRIP_PLANNER_SIDEBAR_ITENERARY_BUTTON = (
        By.CSS_SELECTOR, "div .trip-planner-sidebar__tab--itinerary")
    TRIP_PLANNER_SIDEBAR_PICK_UP_LOCATION = (By.CSS_SELECTOR, "[data-ref$=car-hire-pick-up-location]")
    TRIP_PLANNER_SIDEBAR_PICK_UP_DATE = (By.CSS_SELECTOR, "[data-ref$=car-hire-pick-up-date]")
    TRIP_PLANNER_SIDEBAR_PICK_UP_TIME = (By.CSS_SELECTOR, "[data-ref$=car-hire-pick-up-time]")
    TRIP_PLANNER_SIDEBAR_DROP_OFF_DATE = (By.CSS_SELECTOR, "[data-ref$=car-hire-drop-off-date]")


class CarHireTabLocators:
    PICK_UP_LOCATION = (By.CSS_SELECTOR, "[class=bui-f-font-strong_1][data-testid=pick-up-location]")
    PICK_UP_DATE_TIME = (By.CSS_SELECTOR, "[data-testid=pick-up-date]")
    DROP_OFF_DATE_TIME = (By.CSS_SELECTOR, "[data-testid=drop-off-date]")
    HEADER_TITLE = (By.CSS_SELECTOR, "h3.header__title")
    GETTING_AROUND_IFRAME = (By.CSS_SELECTOR, "#getting-around-iframe")
    FIRST_CAR_IMAGE = (By.XPATH, '//*[@id="in-path-container"]//section//picture/img')
    FIRST_CAR_VIEW_DEAL_BUTTON = (
        By.CSS_SELECTOR, "div[data-testid=car-card-list]>div>div:nth-child(1) button[data-testid*=vcc]")
    TOTAL_PRICE = (By.CSS_SELECTOR, "[data-testid=total-price]")
    ADD_TO_TRIP_BUTTON = (By.CSS_SELECTOR, "button[data-testid=packagePageCta]")

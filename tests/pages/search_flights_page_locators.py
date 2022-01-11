from selene import by


class FlightsTabLocators:
    FLIGHT_CARDS = (by.xpath("//flight-card"))
    FLIGHT_HEADER_SUMMARY = (by.xpath("//flights-trip-details/div"))
    FLIGHTS_PRICES = (by.css("span[data-e2e='flight-card-price']"))
    LIGHT_TYPE_CONTINUE_BUTTON = (by.css("div.fare-card--primary button.fare-card__button"))
    CONFIRMATION_VALUE_FARE = (by.css("button[data-e2e='value']"))
    PASSENGER_TITLE = (by.css("button[type='button']"))
    MR_PASSENGER_TITLE = (by.css("ry-dropdown-item[data-ref='title-item-0'] button.dropdown-item__link"))
    FIRST_NAME_PASSENGER_INPUT = (by.css("input[name='form.passengers.ADT-0.name']"))
    LAST_NAME_PASSENGER_INPUT = (by.css("input[name='form.passengers.ADT-0.surname']"))
    PASSENGERS_CONTINUATION_BUTTON = (by.css("button.continue-flow__button"))


class FlightsPageHeaderLocators:
    BASKET_ICON = (by.css("div.basket-total"))
    USER_MENU_DROPDOWN = (by.xpath("//logged-in"))
    LOG_OUT_BUTTON = (by.xpath("//ry-log-out-button//button"))
    MAIN_LOGO = (by.xpath("//icon[@class='ry-header__logo']"))
    FLIGHT_CONFIRMATION_POPUP = (by.css("ry-tooltip-1"))
    CLOSE_CONFIRMATION_POPUP_BUTTON = (by.css("icon[data-ref='tooltip-close-icon']"))


class BagsTabLocators:
    ONE_SMALL_BAG_RADIOBUTTON = (by.css("bags-small-bag-pax-control ry-radio-circle-button"))
    BAGS_CONTINUATION_BUTTON = (by.css("bags-continue-flow button"))
    BAG_POPUP_DECLINE_BUTTON = (by.css("button.enhanced-takeover__product-dismiss-cta"))


class ExtrasTabLocators:
    EXTRAS_TRIP_CONTINUATION_BUTTON = (by.css("airport-and-flight-container + button"))
    EXTRAS_TRANSPORT_CONTINUATION_BUTTON = (by.css("airport-and-flight-container + button"))


class SeatsTabLocators:
    SEATS_LATER_OPTION_BUTTON = (by.css("button.seats-v2-navigation__button.h4"))
    WITHOUT_SEATS_CONTINUATION_BUTTON = (by.css("button.ry-button--gradient-yellow"))


class TripPlannerLocators:
    TRIP_PLANER_SIDEBAR = (by.css("div.trip-planner-container__content"))
    DEPART_DATE = (by.css("span[data-ref='details-header-start-date']"))
    RETURN_DATE = (by.css("span[data-ref='details-header-end-date']"))
    DEPART_FLIGHT_LOCATIONS = (by.css("div.pillar-tab-details__extra-info-title:first-of-type"))
    RETURN_FLIGHT_LOCATIONS = (by.css("div.pillar-tab-details__extra-info-title:nth-of-type(3)"))

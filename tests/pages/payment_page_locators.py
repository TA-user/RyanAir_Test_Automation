from selenium.webdriver.common.by import By


class PaymentPageLocators:
    DEPART_LOCATION_FIRST_FLIGHT = (By.CSS_SELECTOR,
        "div.price-breakdown-pillars__group[data-ref='outbound'] div.flight-details span:nth-child(1)")
    DESTINATION_LOCATION_FIRST_FLIGHT = (By.CSS_SELECTOR,
        "div.price-breakdown-pillars__group[data-ref='outbound'] div.flight-details span:nth-child(3)")
    DEPART_LOCATION_SECOND_FLIGHT = (By.CSS_SELECTOR,
        "div.price-breakdown-pillars__group[data-ref='inbound'] div.flight-details span:nth-child(1)")
    DESTINATION_LOCATION_SECOND_FLIGHT = (By.CSS_SELECTOR,
        "div.price-breakdown-pillars__group[data-ref='inbound'] div.flight-details span:nth-child(3)")
    DEPART_DATE = (By.CSS_SELECTOR,
        "div.price-breakdown-pillars__group[data-ref='outbound'] div.flight-segment-details span:nth-child(1)")
    RETURN_DATE = (By.CSS_SELECTOR,
        "div.price-breakdown-pillars__group[data-ref='inbound'] div.flight-segment-details span:nth-child(1)")
    
    PASSENGER_INFO_DROPDOWN = (By.CSS_SELECTOR, "div.passenger-details__toggle + icon")
    PASSENGER_NAME = (By.CSS_SELECTOR, "span.passengers__name")
    

    CARD_DETAIL_FORM = (By.CSS_SELECTOR, "card-details > form")
    BILLING_ADDRESS_FORM = (By.CSS_SELECTOR, "address-form > form")
    USER_EMAIL = (By.CSS_SELECTOR, "div.contact-details__user-info div.b2")
    PAY_BUTTON = (By.CSS_SELECTOR, "button.pay-button")
    
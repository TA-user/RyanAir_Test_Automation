class BrowserHelperSettings:
    WAIT_TIME_SECS = 10


class Urls:
    MAIN_PAGE_URL = "https://www.ryanair.com/gb/en"


class DefaultCreds:
    USERNAME = "type here"
    PASSWORD = "type here"


class Capabilities:
    chrome_97_capabilities = {
        "browserName": "chrome",
        "browserVersion": "97.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True,
            "screenResolution": "1920x1080x24"
        }
    }

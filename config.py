class BrowserHelperSettings:
    WAIT_TIME_SECS = 10


class Urls:
    MAIN_PAGE_URL = "https://www.ryanair.com/gb/en"


class DefaultCreds:
    USERNAME = ""
    PASSWORD = ""


class Capabilities:
    chrome_97 = {
        "browserName": "chrome",
        "browserVersion": "97.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True,
            "screenResolution": "1920x1080x24"
        }
    }
    firefox_96 = {
        "browserName": "firefox",
        "browserVersion": "96.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True,
            "screenResolution": "1920x1080x24"
        }
    }
    opera_82 = {
        "browserName": "opera",
        "browserVersion": "82.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True,
            "screenResolution": "1920x1080x24"
        }
    }
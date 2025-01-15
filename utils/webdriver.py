"""Set up browser options and other configurations for the webdriver.
"""

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from settings import HEADLESS_MODE


def set_chrome_options() -> ChromeOptions:
    """Sets Chrome options for Selenium.

    Chrome options for headless browser is enabled.
    """

    chrome_options = ChromeOptions()

    if HEADLESS_MODE:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    return chrome_options


def set_firefox_options() -> FirefoxOptions:
    """Sets Firefox options for Selenium."""

    firefox_options = FirefoxOptions()

    if HEADLESS_MODE:
        firefox_options.add_argument("--headless")

    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    # firefox_prefs = {}
    # firefox_options.experimental_options["prefs"] = firefox_prefs
    # firefox_prefs["profile.default_content_settings"] = {"images": 2}

    return firefox_options

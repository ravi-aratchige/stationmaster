"""Set up browser options and other configurations for the webdriver.
"""

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from settings import HEADLESS_MODE


class BrowserOptionsFactory:
    @staticmethod
    def get_browser_options(browser_name: str = "chrome"):
        """Returns options for browser, based on the browser name provided.

        Args:
            browser_name (str, optional): Name of the required browser. Defaults to "chrome".

        Raises:
            ValueError: Raised when an invalid browser name is specified.

        Returns:
            Options: Browser options for the selected browser.
        """

        if browser_name.lower() == "chrome":
            return BrowserOptionsFactory.get_chrome_options()
        elif browser_name.lower() == "firefox":
            return BrowserOptionsFactory.get_firefox_options()
        else:
            raise ValueError("Invalid browser name has been specified!")

    @staticmethod
    def get_chrome_options() -> ChromeOptions:
        """Return Chrome options for Selenium.

        Chrome options for headless browser can be enabled if required.

        Returns:
            selenium.webdriver.chrome.options: Browser options for Chrome.
        """

        options = ChromeOptions()

        # Check whether Chrome needs to be run in headless mode
        if HEADLESS_MODE:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        # NOTE
        # Window size MUST be set when running Chrome in headless mode.

        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}

        # Prevent images loading
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

        return options

    @staticmethod
    def get_firefox_options() -> FirefoxOptions:
        """Return Firefox options for Selenium.

        Firefox options for headless browser can be enabled if required.

        Returns:
            selenium.webdriver.firefox.options: Browser options for Firefox.
        """

        firefox_options = FirefoxOptions()

        # Check whether Firefox needs to be run in headless mode
        if HEADLESS_MODE:
            firefox_options.add_argument("--headless")

        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")

        # Disable images loading
        firefox_options.set_preference("permissions.default.image", 2)

        return firefox_options


# Make module safely exportable
if __name__ == "__main__":
    pass

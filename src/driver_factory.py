""" driver_factory """

import os

import dotenv
from selenium import webdriver

dotenv.load_dotenv()

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


def get_driver():
    """A fazer"""
    browser_name = os.getenv("BROWSER_NAME", "chrome").lower()
    selenium_grid = os.getenv("SELENIUM_GRID", None)

    browser_map = {
        "chrome": _chrome_options,
        "firefox": _firefox_options,
        "edge": _edge_options,
        "safari": _safari_options,
        "webkit": _webkit_options,
    }

    browser_driver = {
        "chrome": _chrome_driver,
        "firefox": _firefox_driver,
    }

    if browser_name in browser_map:
        options = browser_map[browser_name]()
        if selenium_grid:
            return webdriver.Remote(command_executor=selenium_grid, options=options)
        if browser_name in browser_driver:
            return browser_driver[browser_name](options)
    raise ValueError(f"browser {browser_name} is not supported")


def _chrome_options():
    options = webdriver.ChromeOptions()
    # Disable the default browser check, do not prompt to set it as such
    options.add_argument("--no-default-browser-check")
    # Hide scrollbars from screenshots
    options.add_argument("--hide-scrollbars")
    # Disable the 2023+ search engine choice screen
    options.add_argument("--disable-search-engine-choice-screen")
    # Disable a few things considered not appropriate for automation
    options.add_argument("--enable-automation")
    if HEADLESS:
        # New, native Headless mode
        options.add_argument("--headless=new")
        # Often used in Lambda, Cloud Functions scenarios and Docker
        options.add_argument("--disable-dev-shm-usage")
    options.enable_bidi = False
    return options


def _chrome_driver(options):
    return webdriver.Chrome(options=options)


def _firefox_options():
    options = webdriver.FirefoxOptions()
    if HEADLESS:
        options.add_argument("--headless")
    return options


def _firefox_driver(options):
    return webdriver.Firefox(options=options)


def _edge_options():
    options = webdriver.EdgeOptions()
    return options


def _safari_options():
    options = webdriver.SafariOptions()
    return options


def _webkit_options():
    options = webdriver.WebKitGTKOptions()
    return options

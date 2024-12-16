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
    if HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
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

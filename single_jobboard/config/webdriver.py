"""Configurations for webdrivers"""

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from arsenic import browsers, services


WEBDRIVER_ARGUMENTS = [
    "--headless",
    "--no-sandbox",
    "--disable-extensions",
    "start-maximized",
    "disable-infobars",
]

# The order of webdrivers to try installing and use
WEBDRIVERS = [
    {
        "driver": services.Chromedriver,
        "manager": ChromeDriverManager,
        "browser": browsers.Chrome,
        "options": ChromeOptions,
        "options_kwarg": "chromeOptions",
    },
    {
        "driver": services.Geckodriver,
        "manager": GeckoDriverManager,
        "browser": browsers.Firefox,
        "options": FirefoxOptions,
        "options_kwarg": "firefoxOptions",
    },
    {
        "driver": services.IEDriverServer,
        "manager": IEDriverManager,
        "browser": browsers.InternetExplorer,
        "options": None,
        "options_kwarg": None,
    },
]
# WEBDRIVERS = [
#     {
#         "driver": webdriver.Chrome,
#         "manager": ChromeDriverManager,
#         "options": ChromeOptions,
#         "capabilities": DesiredCapabilities().CHROME,
#     },
#     {
#         "driver": webdriver.Firefox,
#         "manager": GeckoDriverManager,
#         "options": FirefoxOptions,
#         "capabilities": {**DesiredCapabilities().FIREFOX, "marionette": False,},
#     },
#     {
#         "driver": webdriver.Edge,
#         "manager": EdgeChromiumDriverManager,
#         "options": None,
#         "capabilities": DesiredCapabilities().EDGE,
#     },
#     {
#         "driver": webdriver.Opera,
#         "manager": OperaDriverManager,
#         "options": None,
#         "capabilities": DesiredCapabilities().OPERA,
#     },
#     {
#         "driver": webdriver.Ie,
#         "manager": IEDriverManager,
#         "options": None,
#         "capabilities": DesiredCapabilities().INTERNETEXPLORER,
#     },
# ]

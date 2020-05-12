import platform
import os
import logging
import structlog
from arsenic import start_session

from .config.webdriver import WEBDRIVER_ARGUMENTS, WEBDRIVERS
from .exceptions import InstallationError


def set_arsenic_log_level(level=logging.ERROR):
    # Create logger
    logger = logging.getLogger("arsenic")

    # We need factory, to return application-wide logger
    def logger_factory():
        return logger

    structlog.configure(logger_factory=logger_factory)
    logger.setLevel(level)


async def get_webdriver():
    driver = None

    for config in WEBDRIVERS:
        _driver, _browser, _options, _manager, _options_kwarg = (
            config["driver"],
            config["browser"],
            config["options"],
            config["manager"],
            config["options_kwarg"],
        )

        options = None
        if _options:
            options = {
                "args": WEBDRIVER_ARGUMENTS,
            }

        try:
            options_args = {
                _options_kwarg: options,
            }
            binary = _manager().install()
            if platform.system() == "Windows":
                binary = binary.replace("\\", "\\\\")

            service = _driver(binary=binary, log_file=os.devnull,)
            browser = _browser(**options_args)
            driver = await start_session(service, browser)
        except Exception as exc:
            raise exc
        else:
            break

    if driver is None:
        raise InstallationError(
            "Unable to install any webdrivers, using \
            [Chrome, Firefox, Internet Explorer]"
        )

    set_arsenic_log_level()
    return driver


def get_webdriver_selenium():
    """Get whatever webdriver is availiable in the system.
    webdriver_manager and selenium are currently being used for this.
    Supported browsers:[Firefox, Chrome, Opera, Microsoft Edge, Internet Expolorer]

    Returns:
        a webdriver that can be used for scraping.
        Returns None if we don't find a supported webdriver.
    """
    driver = None

    for config in WEBDRIVERS:
        _options, _driver, _manager, _capabilities = (
            config["options"],
            config["driver"],
            config["manager"],
            config["capabilities"],
        )

        options = None
        if _options:
            options = _options()
            for _arg in WEBDRIVER_ARGUMENTS:
                options.add_argument(_arg)
            options.headless = True

        try:
            driver = _driver(
                executable_path=_manager().install(),
                options=options,
                desired_capabilities=_capabilities,
                service_log_path=None,
            )
        except Exception as exc:
            raise exc
        else:
            break

    if driver is None:
        raise InstallationError(
            "Unable to install any webdrivers, using \
            [Chrome, Firefox, Microsoft Edge, Opera, Internet Explorer]"
        )

    return driver

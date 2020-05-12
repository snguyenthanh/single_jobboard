from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from single_jobboard.clients.web_scraper import WebScraper


web_scraper = WebScraper()


async def start_services():
    global web_scraper
    await web_scraper.start()


async def stop_services():
    await web_scraper.stop()


def create_app():
    from .config.application import DEBUG
    from .views.urls import routes
    from .clients.web_scraper import WebScraper
    from .utils.exception_handler import http_exception_handler

    exception_handlers = {
        HTTPException: http_exception_handler,
        # Exception: http_exception
    }
    middleware = [
        Middleware(GZipMiddleware),
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]

    app = Starlette(
        routes=routes,
        debug=DEBUG,
        exception_handlers=exception_handlers,
        middleware=middleware,
        on_startup=[start_services],
        on_shutdown=[stop_services],
    )

    return app

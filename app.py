# from single_jobboard.webdriver import get_webdriver
#
# driver = get_webdriver()
# driver.close()

import uvicorn

from single_jobboard import create_app
from single_jobboard.config.application import UVICORN_RUN_CONFIG


app = create_app()

if __name__ == "__main__":
    uvicorn.run("app:app", **UVICORN_RUN_CONFIG)

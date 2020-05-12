from attr import attrs, attrib
from bs4 import BeautifulSoup

from single_jobboard import channels
from single_jobboard.webdriver import get_webdriver


class WebScraper:
    def __init__(self):
        self.driver = None
        self.config = None

    async def start(self):
        self.driver = await get_webdriver()

    async def stop(self):
        await self.driver.stop_session()

    def parse_into_bs(self, page_source: str):
        return BeautifulSoup(page_source, "lxml")

    async def get_jobs(self, configs: list) -> list:
        channel = getattr(channels, "glassdoor")
        config = {
            "query": "software",
            "job_type": "fulltime",
            "remote": 0,
        }
        search_url = channel.get_search_url(config)
        # await self.driver.get(search_url)
        # source = await self.driver.get_page_source()
        # soup = self.parse_into_bs(source)

        jobs = await channel.get_jobs(search_url, self.driver)
        # print(f'url: {search_url}')

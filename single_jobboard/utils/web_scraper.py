from bs4 import BeautifulSoup


def parse_into_bs(page_source: str):
    return BeautifulSoup(page_source, "lxml")

from arsenic import keys, actions
from asyncio import sleep

from single_jobboard.models import JobSummary
from single_jobboard.utils.web_scraper import parse_into_bs
from single_jobboard.utils.url import add_params_to_url


def get_search_url(config):
    """gets the glassdoor search url"""
    job_types = {
        "fulltime": "fulltime",
        "parttime": "parttime",
        "contract": "contract",
        "internship": "internship",
        "temporary": "temporary",
    }

    map_query_params = {
        "query": "sc.keyword",
        "job_type": "jobType",
        "remote": "remoteWorkType",  # 0 or 1
        "date_posted": "fromAge",  # int
    }

    query_params = {
        map_query_params[key]: val
        for key, val in config.items()
        if key in map_query_params
    }

    # search_url = "https://www.glassdoor.com/Job/jobs.htm?clickSource=searchBtn&sc.keyword={query}&jobType={job_type}&remoteWorkType={remote}"
    search_url = "https://www.glassdoor.com/Job/jobs.htm?clickSource=searchBtn&countryRedirect=true"
    return add_params_to_url(search_url, query_params)


async def get_jobs(url, driver) -> list:
    await driver.get(url)

    # await driver.wait_for_element(3, ".sqLogo img[src]:last-of-type")
    sleep(0.2)
    source = await driver.get_page_source()
    soup = parse_into_bs(source)

    menu_element = "#MainCol"
    menu_height = await driver.execute_script(
        "return document.querySelector(arguments[0]).scrollHeight;", menu_element
    )
    row_height = await driver.execute_script(
        "return document.querySelector(arguments[0]).scrollHeight;",
        ".react-job-listing:nth-of-type(1)",
    )
    cur_height = 0

    listings = soup.findAll("li", {"class": "react-job-listing"})
    jobs = []
    found_job_ids = set()

    for job in listings:
        if job["data-id"] in found_job_ids:
            continue

        found_job_ids.add(job["data-id"])

        employer = job.find("div", {"class": ["jobInfoItem", "jobEmpolyerName"]}).text
        position = job.find("a", {"class": ["jobInfoItem", "jobTitle"]}).text
        city = job.find("span", {"class": "subtle loc"}).text
        # date_posted = job.find("span", {"class": "jobLabel nowrap"}).find("span", {"class": "minor"})
        date_posted = job.find("span", {"class": "jobLabel nowrap"}).text
        logo = job.find("span", {"class": "sqLogo"})
        rating = job.find("span", {"class": "compactStars"}).text
        jobs.append({"employer": employer, "position": position})

    while cur_height <= menu_height:
        # element = '#ResultsFooter'
        # element = '.css-j26eul'
        # element = 'li:nth-of-type(1)'
        element = "#MainColSummary"
        # element = "article[id='MainColSummary'][class='gdGrid']"
        # cool = await driver.get_element(element)
        # await cool.click()
        # await actions.Mouse.move_to(cool, 150)
        # await actions.Mouse.down()
        # await actions.Mouse.up()

        # await cool.send_keys(keys.END)
        # height = await driver.execute_script("return document.querySelector(arguments[0]).scrollHeight;", element)
        # print('yay')
        # print(height)
        # Action scroll down
        # await driver.execute_script('''document.querySelector(arguments[0]).scrollTo(0, document.querySelector(arguments[0]).scrollHeight);''', element)
        # await driver.execute_script('''document.querySelector(arguments[0]).scrollIntoView();''', element)

        cur_height += row_height * (len(listings) - 1)  # The height of each row
        await driver.execute_script(
            f"""document.querySelector(arguments[0]).scrollTo(0, {cur_height});""",
            menu_element,
        )
        sleep(0.2)
        # sleep(1)
        # await driver.wait_for_element(3, "span[class='sqLogo'] img[src]:not([src='']):last-of-type")
        # await driver.wait_for_element(3, ".sqLogo img[src]:last-of-type")

        source = await driver.get_page_source()
        soup = parse_into_bs(source)

        listings = soup.findAll("li", {"class": "react-job-listing"})
        for job in listings:
            if job["data-id"] in found_job_ids:
                continue

            found_job_ids.add(job["data-id"])

            employer = job.find(
                "div", {"class": ["jobInfoItem", "jobEmpolyerName"]}
            ).text
            position = job.find("a", {"class": ["jobInfoItem", "jobTitle"]}).text
            city = job.find("span", {"class": "subtle loc"}).text
            # date_posted = job.find("span", {"class": "jobLabel nowrap"}).find("span", {"class": "minor"})
            date_posted = job.find("span", {"class": "jobLabel nowrap"}).text
            logo_element = job.find("span", {"class": "sqLogo"})
            logo = logo_element.img.get("src", None) if logo_element.img else None
            rating_element = job.find("span", {"class": "compactStars"})
            rating = rating_element.text if rating_element else None

            # print(f'Index: {index + 1}')
            print(employer)
            print(position)
            print(city)
            print(date_posted)
            print(logo)
            # print(logo["src"])
            print(rating)
            print()
            jobs.append({"employer": employer, "position": position})

    print(f"length: {len(jobs)}")

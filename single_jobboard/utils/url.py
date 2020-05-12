import urllib.parse as urlparse


def add_params_to_url(url: str, params: dict) -> str:
    url_parse = urlparse.urlparse(url)
    query = url_parse.query
    url_dict = dict(urlparse.parse_qsl(query))
    url_dict.update(params)
    url_new_query = urlparse.urlencode(url_dict)
    url_parse = url_parse._replace(query=url_new_query)
    return urlparse.urlunparse(url_parse)

from urllib.parse import urlparse


def name_from_url(url: str):
    return urlparse(url).path.split("/")[-1]

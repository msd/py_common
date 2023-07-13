FF_USERAGENT = "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0"

FF_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Dnt": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": FF_USERAGENT,
}

FF_HEADERS_SEC_FETCH_NONE = {
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}
FF_HEADERS_SEC_FETCH_SAME = {
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}


FF_HEADERS_SEC_FETCH_CROSS = {
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
}

try:
    import requests

    __REQUESTS_INSTALLED = True
except ImportError:
    __REQUESTS_INSTALLED = False

if __REQUESTS_INSTALLED:

    def ff_session():
        session = requests.session()
        session.headers.update(FF_HEADERS)
        return session

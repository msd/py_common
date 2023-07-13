from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from requests import Session
import requests


@dataclass
class Webpage:
    url: str | None = field(default=None)
    _html: str | None = field(default=None)
    _soup: BeautifulSoup | None = field(default=None)
    session: Session | None = field(default=None)

    def _html__get_from_others(self):
        if self._soup is not None:
            return self._soup.text
        if self.url is not None:
            response = (self.session or requests).get(self.url)
            response.raise_for_status()
            return response.text
        raise RuntimeError("Both URL and Soup are null")

    @property
    def html(self):
        if self._html is None:
            self._html = self._html__get_from_others()
        return self._html

    @property
    def soup(self):
        if self._soup is None:
            if self._html is not None or self.url is not None:
                self._soup = BeautifulSoup(self.html, "lxml")
            else:
                raise RuntimeError("Both HTML and URL are null")
        return self._soup

    @staticmethod
    def from_url(url: str, session: Session | None = None):
        return Webpage(url=url, session=session)

    @staticmethod
    def from_html(html: str, session: Session | None = None):
        return Webpage(_html=html, session=session)

    @staticmethod
    def from_soup(soup: BeautifulSoup, session: Session | None = None):
        return Webpage(_soup=soup, session=session)

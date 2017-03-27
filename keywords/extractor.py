import re

from bs4 import BeautifulSoup


class ContentExtractor:
    """Tool to read informations from web page

    Uses BeautifulSoup module to parse web page content"""

    def __init__(self, page):
        self._content = None
        self._page = b''
        if isinstance(page, bytes):
            self._page = page
        self.init_parser()
        # TODO
        # set page by property ?

    def init_parser(self):
        self._content = BeautifulSoup(self._page, 'html.parser')
        # TODO
        # try/except ?
        # suppressing wornings from bs ?

    def get_keywords(self):
        keywords = None
        if self._content:
            if self._content.head:
                # find meta with name = keywords/KEYWORDS/Keywords/etc.
                meta = self._content.head.find_all('meta',
                                                    attrs={'name': re.compile('^keywords', re.I),
                                                           'content': True})
                if len(meta) > 0:
                    meta = meta[0]  # first occurrence of keywords meta - should by only one
                    keywords = meta['content']

        return keywords

    def get_text(self):
        body_text = None
        if self._content:
            if self._content.body:
                body_text = self._content.body.get_text()
        return body_text

import re

from bs4 import BeautifulSoup


class ContentExtractor:
    """Tool to read informations from web page

    Uses BeautifulSoup module to parse web page content"""

    def __init__(self, page):
        self._content = None
        self._page = b''

        self.page = page
        self.init_parser()

    def init_parser(self):
        self._content = BeautifulSoup(self._page, 'html.parser')

    def get_keywords(self):
        keywords = None
        if self._content is not None:
            if self._content.head is not None:
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
        if self._content is not None:
            if self._content.body is not None:
                body_text = self._content.body.get_text()
        return body_text

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        """Set the page to parse"""
        if isinstance(page, bytes):
            self._page = page
        else:
            self._page = b''

from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import urlopen


class URLLoader:
    """Simple class for opening a web page selected by given url."""

    def __init__(self, url):
        self._error_info = None
        self._url = None

        self.url = ''
        self.url = url

    def parse_url(self):
        """Very simple test if url is valid."""
        if len(self.url) == 0:
            self._error_info = 'URLLoader: URL is empty'
            return False

        url_parsed = urlparse(self.url)
        if url_parsed.scheme != 'http' and url_parsed.scheme != 'https':
            self._error_info = 'URLLoader: HTTP/HTTPS URL expected'
            return False
        if len(url_parsed.netloc) == 0:
            self._error_info = 'URLLoader: URL is not valid'
            return False
        # TODO
        # More tests?
        # add http if scheme is empty ?

        return True

    def open(self):
        """Open specified url

        Return the content read from page"""
        self._error_info = None
        page = None

        if not self.parse_url():
            return None

        try:
            with urlopen(self.url) as my_response:
                page = my_response.read()
        except URLError as e:
            self._error_info = str.format('URLLoader: Error opening URL: {0}', e.reason)
            return None
        except Exception as e:
            self._error_info = str.format('URLLoader: Error opening URL: {0}', e)
            return None
        finally:
            return page

    @property
    def error_info(self):
        """Return error description if something goes wrong"""
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        pass

    @property
    def url(self):
        """Return the URL of the page to open"""
        return self._url

    @url.setter
    def url(self, url):
        """Set the URL of the page to open"""
        if isinstance(url, str):
            self._url = url
        else:
            self._url = ''

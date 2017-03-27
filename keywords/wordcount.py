class WordCounter:
    """Class for counting occurrences of specified keywords in given text"""

    def __init__(self, text=None, keywords=None):
        """Construct a word counter

        text - text to analyse (defaults to '')
        keywords - words to search and count inside text, separated by commas (defaults to '')
        """
        self._text = ''
        self._keywords = ''

        self.text = text
        self.keywords = keywords

    def count(self):
        """Count keywords in specified text

        Return dictionary of keywords with counted occurrences"""
        statistics = {}

        if len(self._text) > 0 and len(self._keywords) > 0:
            statistics = dict((kw.strip(), 0) for kw in self._keywords.split(','))
            for s in statistics:
                statistics[s] = self._text.lower().count(s.lower())

        # TODO:
        # full words ?

        return statistics

    @property
    def text(self):
        """Return the text intended to analyse"""
        return self._text

    @text.setter
    def text(self, text):
        """Set the text to analyse"""
        if isinstance(text, str):
            self._text = text
        else:
            self._text = ''

    @property
    def keywords(self):
        """Return the keywords intended to search inside the text"""
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Set the keywords to search inside the text"""
        if isinstance(keywords, str):
            self._keywords = keywords
        else:
            self._keywords = ''

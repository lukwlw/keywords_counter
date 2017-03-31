import tkinter as tk

from keywords.tools.loader import URLLoader
from keywords.tools.extractor import ContentExtractor
from keywords.tools.wordcount import WordCounter


class KeywordsMainForm:
    """The project main dialog window

    To count keywords occurrences on the page, type the URL into URL text box,
    and push Count button"""
    def __init__(self, parent):
        self._parent = parent
        self._create_widgets()
        self._parent.wm_title('To count keywords on page')

    def _create_widgets(self):
        """Prepare dialog widgets"""
        self.content = tk.Frame(self._parent)

        # URL input
        self.lbl_url = tk.Label(self.content, text='URL:')
        self.entry_url = tk.Entry(self.content)

        # Results - text area and controls around
        self.lbl_result = tk.Label(self.content, text='Counted words:')
        self.txt_result = tk.Text(self.content, width=50, height=8)

        self.scroll_result = tk.Scrollbar(self.content,
                                          orient=tk.VERTICAL,
                                          command=self.txt_result.yview)
        self.txt_result.config(yscrollcommand=self.scroll_result.set)

        # Problems info - text area and controls around
        self.lbl_error = tk.Label(self.content, text='Problems:')
        self.txt_error = tk.Text(self.content, width=50, height=4)

        self.scroll_error = tk.Scrollbar(self.content,
                                         orient=tk.VERTICAL,
                                         command=self.txt_error.yview)
        self.txt_error.config(yscrollcommand=self.scroll_error.set)

        # Buttons
        self.btn_count = tk.Button(self.content,
                                   text='Count',
                                   width='10',
                                   command=self._click_count)
        self.btn_clear = tk.Button(self.content,
                                   text='Clear',
                                   width='10',
                                   command=self._click_clear)
        self.btn_close = tk.Button(self.content,
                                   text='Close',
                                   width='10',
                                   command=self._parent.quit)

        self._set_positions_on_grid()

    def _set_positions_on_grid(self):
        """Set widgets on grid"""
        self.content.grid(column=0,
                          row=0,
                          sticky=(tk.N, tk.S, tk.E, tk.W),
                          pady=5,
                          padx=5)

        self.lbl_url.grid(column=0, row=0, sticky=tk.W)
        self.entry_url.grid(column=1,
                            row=0,
                            columnspan=3,
                            sticky=(tk.N, tk.E, tk.W),
                            pady=5)

        self.lbl_result.grid(column=0, row=1, sticky=tk.W, pady=(10, 2))
        self.txt_result.grid(column=0,
                             row=2,
                             columnspan=3,
                             sticky=(tk.N, tk.S, tk.E, tk.W))
        self.scroll_result.grid(column=3, row=2, sticky=(tk.N, tk.S, tk.W))

        self.lbl_error.grid(column=0, row=3, sticky=tk.W, pady=(10, 2))
        self.txt_error.grid(column=0,
                            row=4,
                            columnspan=3,
                            sticky=(tk.N, tk.S, tk.E, tk.W))
        self.scroll_error.grid(column=3, row=4, sticky=(tk.N, tk.S, tk.W))

        self.btn_count.grid(column=0, row=5, sticky=tk.W, pady=(10, 0))
        self.btn_clear.grid(column=1, row=5, sticky=tk.E, pady=(10, 0), padx=5)
        self.btn_close.grid(column=2, row=5, columnspan=2, pady=(10, 0))

        self._parent.columnconfigure(0, weight=1)
        self._parent.rowconfigure(0, weight=1)

        self.content.columnconfigure(1, weight=3)
        self.content.rowconfigure(2, weight=1)

    def _click_count(self):
        """'on click' command for Count button

        Clear current results and try to count keywords on page"""
        self.clear()
        self.count()

    def _click_clear(self):
        self.clear()

    def print_problem_info(self, error_info):
        """Print info in problems text field"""
        self.txt_error.insert(tk.INSERT, '{0}\n'.format(error_info))

    def print_result(self, result_info):
        """Print info in results text field"""
        self.txt_result.insert(tk.INSERT, '{0}\n'.format(result_info))

    def clear(self):
        """Clear fields"""
        self.txt_result.delete(1.0, tk.END)
        self.txt_error.delete(1.0, tk.END)

    def count(self):
        """Open the page given by URL, get keywords and text, and count keywords.
        Display results."""

        # load the page given by url
        url_to_test = self.entry_url.get()
        url_loader = URLLoader(url_to_test)
        web_page = url_loader.open()

        if web_page is None:
            self.print_problem_info(url_loader.error_info)
            return

        # get keywords and body text from the page
        extractor = ContentExtractor(web_page)
        page_text = extractor.get_text()
        page_keywords = extractor.get_keywords()
        if page_keywords is None:
            self.print_problem_info("Keywords tag not found or is empty")
            return
        if page_text is None:
            self.print_problem_info("Body text not found or is empty")
            return

        # count words
        word_counter = WordCounter(page_text, page_keywords)
        stat = word_counter.count()
        if len(stat) > 0:
            for s in stat:
                self.print_result('{0}: {1}'.format(s, stat[s]))
        else:
            self.print_result('No keywords found')

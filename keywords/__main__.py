import tkinter as tk

from keywords.forms.mainform import KeywordsMainForm


root = tk.Tk()
win = KeywordsMainForm(root)
root.mainloop()

# Future works
# Add more checks in loader to test URLs. Consider adding http if not exists in url
# Add logging - logging.xxxxx(), warnings.warn(), etc. to make app more verbose
# Add additional button in main form to clear the current results

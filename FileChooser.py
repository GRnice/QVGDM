from tkinter import filedialog
from tkinter import *

class FileChooser:
    def __init__(self):
        pass

    def get_filename(self):
        root = Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(initialdir="./", title="Select file")
        root.destroy()
        return filename

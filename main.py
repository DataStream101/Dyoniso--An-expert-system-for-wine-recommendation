from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from pyswip import *
import re
import unicodedata

import warnings
warnings.filterwarnings("ignore")

from MenuPage import MenuPage


def main():
    root = Tk()
    app = MenuPage(root)

    root.mainloop()

if __name__ == '__main__':
    main()

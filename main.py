import platform
from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.window()
        self.root.mainloop()

    def window(self):
        self.root.geometry('500x500')

Application()
import platform
from tkinter import *
from tkinter import ttk


root = Tk()

class Application():
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.frames()
        self.labels()
        root.mainloop()

    def window(self):
        self.root.geometry('500x500')
        self.root.resizable(width = FALSE, height = FALSE)
        self.root.title('System Information')

    def frames(self):
        self.fr_title = Frame(self.root, width=500, height=65, bg='white')
        self.fr_title.grid(row=0, column=0)

        self.fr_dados = Frame(self.root, width=400, height=400, bg='black')
        self.fr_dados.grid(row=1, column=0, columnspan=3, sticky=N, pady=30, padx=15)

    def labels(self):
        self.lb_title = Label(self.fr_title, text='System Information', fg='black', font='arial 18', width=35)
        self.lb_title.grid(row=0, column=0)

        self.lb_system = Label(self.fr_dados, text='System: ', width=13, height=1,
                                    pady=7, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 12 bold', bg="#DCDCDC", fg="#000000")
        self.lb_system.grid(row=0, column=0, pady=1, padx=0)
        self.et_system = Entry(self.fr_dados, width=30, font='Arial 10 bold')
        self.et_system.grid(row=0, column=1, padx=0, pady=1)


Application()
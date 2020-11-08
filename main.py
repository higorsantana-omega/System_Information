import platform
from tkinter import *


root = Tk()

class Application():
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.frames()
        self.labels()
        self.dados()
        root.mainloop()

    def window(self):
        self.root.geometry('500x300')
        self.root.resizable(width = FALSE, height = FALSE)
        self.root.title('System Information')
        self.root.configure(bg='#DCDCDC')

    def frames(self):
        self.fr_title = Frame(self.root, width=500, height=65, bg='#DCDCDC')
        self.fr_title.grid(row=0, column=0)

        self.fr_dados = Frame(self.root, width=400, height=400, bg='#DCDCDC')
        self.fr_dados.grid(row=1, column=0, columnspan=3, sticky=N, pady=30, padx=15)

    def labels(self):
        self.lb_title = Label(self.fr_title, text='System Information', bg='#DCDCDC', fg='black', font='arial 18', width=35)
        self.lb_title.grid(row=0, column=0)

        self.lb_system = Label(self.fr_dados, text='System: ', width=13, height=1,
                                    pady=7, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 12 bold', bg="#DCDCDC", fg="#000000")
        self.lb_system.grid(row=0, column=0, pady=1, padx=0)

        self.lb_platform = Label(self.fr_dados, text='Platform: ', width=13, height=1,
                                    pady=7, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 12 bold', bg="#DCDCDC", fg="#000000")
        self.lb_platform.grid(row=1, column=0, pady=1, padx=0)

        self.lb_processor = Label(self.fr_dados, text='Processor: ', width=13, height=1,
                                    pady=7, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 12 bold', bg="#DCDCDC", fg="#000000")
        self.lb_processor.grid(row=2, column=0, pady=1, padx=0)

        self.lb_architecture = Label(self.fr_dados, text='Architecture: ', width=13, height=1,
                                    pady=7, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 12 bold', bg="#DCDCDC", fg="#000000")
        self.lb_architecture.grid(row=3, column=0, pady=1, padx=0)

        self.lb_computername = Label(self.fr_dados, text='ComputerName: ', width=13, height=1,
                                    pady=7, padx=0, relief="flat", anchor=NW, 
                                    font='Helvetica 12 bold', bg="#DCDCDC", fg="#000000")
        self.lb_computername.grid(row=4, column=0, pady=1, padx=0)

    def dados(self):
        self.system_name = platform.system()
        self.plataform = platform.platform()
        self.processor = platform.processor()
        self.architecture = platform.architecture()
        self.computername = platform.node()

        self.et_system = Entry(self.fr_dados, width=30, font='Arial 10', bg='white')
        self.et_system.grid(row=0, column=1, padx=0, pady=1)
        self.et_system.insert(END, self.system_name)
        self.et_system.configure(state='disabled')

        self.et_plataform = Entry(self.fr_dados, width=30, font='Arial 10', bg='white')
        self.et_plataform.grid(row=1, column=1, padx=0, pady=1)
        self.et_plataform.insert(END, self.plataform)
        self.et_plataform.configure(state='disabled')

        self.et_processor = Entry(self.fr_dados, width=30, font='Arial 10', bg='white')
        self.et_processor.grid(row=2, column=1, padx=0, pady=1)
        self.et_processor.insert(END, self.processor)
        self.et_processor.configure(state='disabled')

        self.et_architecture = Entry(self.fr_dados, width=30, font='Arial 10', bg='white')
        self.et_architecture.grid(row=3, column=1, padx=0, pady=1)
        self.et_architecture.insert(END, self.architecture)
        self.et_architecture.configure(state='disabled')

        self.et_computername = Entry(self.fr_dados, width=30, font='Arial 10', bg='white')
        self.et_computername.grid(row=4, column=1, padx=0, pady=1)
        self.et_computername.insert(END, self.computername)
        self.et_computername.configure(state='disabled')

Application()

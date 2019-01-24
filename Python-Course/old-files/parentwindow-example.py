from tkinter import *
import tkinter as tk

from tkinter import messagebox
from tkinter.filedialog import askdirectory

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(700,500)
        self.master.title("My Program")
        self.lbl_fname = tk.Label(self.master,text='Hello User')
        self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

        self.closeButton = Button(self.master,text="Close",width=5,height=2)
        self.closeButton.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=E+W)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

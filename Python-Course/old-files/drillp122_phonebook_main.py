from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

import drillp122_phonebook_gui
import drillp122_phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(300,100) #(Height, Width)
        self.master.maxsize(300,100)
        drillp122_phonebook_func.center_window(self,300,100)
        self.master.title("The Tkinter Directory Select Demo")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: drillp122_phonebook_func.ask_quit(self))
        arg = self.master
        drillp122_phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

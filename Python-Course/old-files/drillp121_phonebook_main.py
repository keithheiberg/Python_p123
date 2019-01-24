from tkinter import *
import tkinter as tk

import drillp121_phonebook_gui
import drillp121_phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(481,203) #(Height, Width)
        self.master.maxsize(481,203)
        drillp121_phonebook_func.center_window(self,481,203)
        self.master.title("Check files")
        self.master.configure(bg="#FFFFFF")
        self.master.protocol("WM_DELETE_WINDOW", lambda: drillp121_phonebook_func.ask_quit(self))
        arg = self.master
        drillp121_phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

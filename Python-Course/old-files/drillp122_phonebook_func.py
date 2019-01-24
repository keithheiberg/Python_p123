import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

import drillp122_phonebook_main
import drillp122_phonebook_gui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def onSelect(self):
    # Calling by self.btn_add, sending to the self.txt_folder widget
	file_path = askdirectory()
	self.txt_folder.insert(0,file_path)
	

if __name__ == "__main__":
    pass


root = Tk()
root.withdraw()

current_directory = filedialog.askdirectory()
file_name = "test.txt"

file_path = os.path.join(current_directory,file_name)
print(file_path)

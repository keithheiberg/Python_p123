from tkinter import *
import tkinter as tk

import drillp121_phonebook_main
import drillp121_phonebook_func

def load_gui(self):
    self.txt_fname = tk.Entry(self.master,text='', width=50)
    self.txt_fname.grid(row=5,column=2,rowspan=1,columnspan=4,padx=(30,0),pady=(50,0),sticky=NSEW)
    self.txt_lname = tk.Entry(self.master,text='', width=50)
    self.txt_lname.grid(row=6,column=2,rowspan=1,columnspan=4,padx=(30,0),pady=(10,0),sticky=NSEW)

    self.btn_add = tk.Button(self.master,width=15,height=2,text='Browse...')
    self.btn_add.grid(row=5,column=0,padx=(10,0),pady=(50,0),sticky=SW)
    self.btn_update = tk.Button(self.master,width=15,height=2,text='Browse...')
    self.btn_update.grid(row=6,column=0,padx=(10,0),pady=(10,0),sticky=SW)
    self.btn_delete = tk.Button(self.master,width=15,height=3,text='Check for files...')
    self.btn_delete.grid(row=7,column=0,padx=(10,0),pady=(10,0),sticky=SW)
    self.btn_close = tk.Button(self.master,width=15,height=3,text='Close Program')
    self.btn_close.grid(row=7,column=5,columnspan=5,padx=(10,0),pady=(10,0),sticky=SW)

if __name__ == "__main__":
    pass

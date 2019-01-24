from tkinter import *
import tkinter as tk

import drillp122_phonebook_main
import drillp122_phonebook_func

def load_gui(self):
	self.txt_folder = tk.Entry(self.master,text='Directory goes here...', width=45)
	self.txt_folder.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(10,10),pady=(10,0),sticky=NSEW)

	self.btn_add = tk.Button(self.master,width=20,height=2,text='Choose directory',command=lambda: drillp122_phonebook_func.onSelect(self))
	self.btn_add.grid(row=8,column=0,padx=(10,0),pady=(15,10),sticky=W)
	
    
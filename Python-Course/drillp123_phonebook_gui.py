from tkinter import *
import tkinter as tk

import drillp123_phonebook_main
import drillp123_phonebook_func

def load_gui(self):
	self.lbl_sourceDir = tk.Label(self.master,text='Source Directory:')
	self.lbl_sourceDir.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky=N+W)
	self.lbl_destDir = tk.Label(self.master,text='Destination Directory:')
	self.lbl_destDir.grid(row=3,column=0,padx=(10,0),pady=(10,0),sticky=N+W)

	self.txt_sourceDir = tk.Entry(self.master,width=65)
	self.txt_sourceDir.grid(row=1,column=0,rowspan=1,columnspan=6,padx=(10,10),pady=(10,0),sticky=NSEW)
	self.txt_destDir = tk.Entry(self.master,width=65)
	self.txt_destDir.grid(row=4,column=0,rowspan=1,columnspan=6,padx=(10,10),pady=(10,0),sticky=NSEW)

	self.btn_addSource = tk.Button(self.master,width=18,height=2,text='Source Dir',command=lambda: drillp123_phonebook_func.onSelectSource(self))
	self.btn_addSource.grid(row=5,column=0,padx=(10,0),pady=(15,10),sticky=W)
	self.btn_addDest = tk.Button(self.master,width=18,height=2,text='Destination Dir',command=lambda: drillp123_phonebook_func.onSelectDest(self))
	self.btn_addDest.grid(row=5,column=2,padx=(10,0),pady=(15,10),sticky=W)
	self.btn_addText = tk.Button(self.master,width=18,height=2,text='Move Text files',command=lambda: drillp123_phonebook_func.onSelectText(self))
	self.btn_addText.grid(row=5,column=4,padx=(10,0),pady=(15,10),sticky=W)
	
	drillp123_phonebook_func.create_db(self)


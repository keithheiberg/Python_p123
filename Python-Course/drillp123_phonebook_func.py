import os, time, shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import sqlite3

import drillp123_phonebook_main
import drillp123_phonebook_gui

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

##def create_db(self):   1st change
def create_db():
	conn = sqlite3.connect('db_phonebook.db')
	with conn:
		cur = conn.cursor()
		cur.execute("CREATE TABLE if not exists tbl_phonebook( \
			ID INTEGER PRIMARY KEY AUTOINCREMENT, \
			col_fname TEXT, \
			col_dirname TEXT, \
			col_mtime TEXT \
			);")
		conn.commit()
	conn.close()
##	first_run(self) 3rd change

def first_run(self):
        # Get source directory from text field in dialog box
        src_file_path = self.txt_sourceDir.get() ##8th change
        srcName = os.listdir(src_file_path) ##8th change
        # Populate dB
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            # Add data, print to shell
            for file in srcName: ##8th change
                cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_dirname,col_mtime) VALUES (?,?,?)""", (file,src_file_path,(os.path.getmtime(file))))
                conn.commit()
                print("File, mtime: {} {}".format(file,(os.path.getmtime(file)))) ##9th change
        conn.close() ##7th change??

def onSelectSource(self):
	src_file_path = askdirectory()
	self.txt_sourceDir.insert(0,src_file_path)
	
def onSelectDest(self):
	dst_file_path = askdirectory()
	self.txt_destDir.insert(0,dst_file_path)
	
def onSelectText(self):
        # Get directories from text fields in dialog box
        src_file_path = self.txt_sourceDir.get()
        dst_file_path = self.txt_destDir.get()
        srcName = os.listdir(src_file_path)
        dstName = os.listdir(dst_file_path)
        for file in srcName:  ##6th change
            if file.endswith(".txt"): ##6th change
                first_run(self) ##6th change
	# Move text files from source to destination, print names to shell
        for file in srcName:
            if file.endswith(".txt"):
                fullpath = os.path.join(src_file_path, file)
                shutil.move(fullpath,dst_file_path)
                print("Moved text file: {}".format(file))
##	first_run(self) ##5th change	##6th change is commenting this out	
##	create_db(self) 4th change
	
if __name__ == "__main__":
    pass

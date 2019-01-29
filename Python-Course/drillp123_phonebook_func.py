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

def first_run(self):
	# Get directory paths from text fields in dialog box
	dst_file_path = self.txt_destDir.get() 
	dstName = os.listdir(dst_file_path) 
	print("Destination dir: {}".format(dstName))
	src_file_path = self.txt_sourceDir.get() 
	srcName = os.listdir(src_file_path) 
	print("Source dir: {}".format(srcName))
	# Populate dB
	conn = sqlite3.connect('db_phonebook.db')
	with conn:
		cur = conn.cursor()
		# Add data, print to shell
		for file in srcName: 
			print("In srcName: File, mtime: {} {}".format(file,(os.path.getmtime(file))))
			if file.endswith(".txt"):
				cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_dirname,col_mtime) VALUES (?,?,?)""", (file,src_file_path,(os.path.getmtime(file))))
				conn.commit()
	
	conn.close() 

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
		# Populate dB
		first_run(self) 
		# Move text files from source to destination, print names to shell
		for file in srcName:
			if file.endswith(".txt"):
				fullpath = os.path.join(src_file_path, file)
				shutil.move(fullpath,dst_file_path)
				print("File, mtime: {} {}".format(file,(os.path.getmtime(file)))) 
				print("fullpath: {}".format(fullpath))
				print("dst_file_path: {}".format(dst_file_path))
				print("Moved text file: {}".format(file))
			
		
if __name__ == "__main__":
    pass

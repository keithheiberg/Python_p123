import sqlite3, os
from os import listdir
from os.path import isfile, join
from pprint import pprint

conn = sqlite3.connect('fileNamesText.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileNamesText( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fileName TEXT)")

basepath = 'c:\\PyProjects\\'
files = [file for file in listdir(basepath) if isfile(join(basepath, file))]
filesText = []

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    filename, file_extension = os.path.splitext( path )
    if file_extension == '.txt':
        f = open(path, 'r')
        file_contents = f.read()
        filesText.append(fname)
        cur.execute("INSERT INTO tbl_fileNamesText(col_fileName) VALUES (?)", (fname,))
        pprint(file_contents)
        pprint(filesText)
        pprint(fname)
        f.close()

    conn.commit()
conn.close()

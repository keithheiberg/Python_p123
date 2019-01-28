import sqlite3, os
from os import listdir
from os.path import isfile, join

files = [file for file in listdir(path) if isfile(join(path, file))]
print(files)

basepath = 'c:\\PyProjects\\'
fname = 'Test.txt'

for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    filename, file_extension = os.path.splitext( path )
    if file_extension == '.txt':
        f = open(path, 'r')
        file_contents = f.read()
        f.close()

conn = sqlite3.connect('fileNames.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileNames( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Bob', 'Smith', 'bsmith@gmail.com'))
    conn.commit()
conn.close()

conn = sqlite3.connect('fileNames.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)

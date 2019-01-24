import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizeable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg="lightgray")

        self.varFname = StringVar()
        self.varLname = StringVar()
        
        self.lbl

        self.txtFname = Entry(self.master, text=self.varFname, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtFname.grid(row=, column=)

        self.txtLname = Entry(self.master, text=self.varLname, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtLname.grid(row=, column=)
        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

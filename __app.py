import sqlite3
from tkinter import *
from tkinter import filedialog,messagebox,simpledialog, scrolledtext
from tkinter.ttk import Notebook, Frame, Treeview
import os
from traceback import format_exc
import sys

from tkinter import *
   
# Create object

db_path = None

def load_db():
    global db_path
    db_path = filedialog.askopenfilename(filetypes=(("SQL Database","*.db")))

def secure_error(error:Exception):
    win = Tk()

    # This is the section of code which creates the main window
    win.geometry('520x230')
    win.configure(background='#FFFFFF')
    win.title('Internal Error')
    text_area = scrolledtext.ScrolledText(win, 
                                      wrap = WORD, 
                                      width = 65, 
                                      height = 10, 
                                      font = ("Arial",
                                              10))
    
    text_area.pack()
   
    # Placing cursor in the text area
    text_area.focus()
    text_area.insert(INSERT,
    f"""
    {format_exc()}
    """)
    Button(win,text="Copy to Clipboard",command=lambda:win.clipboard_append(error)).pack()
    # Making the text read only
    Button(win,text="Close",command=lambda:win.destroy()).pack()
    text_area.configure(state ='disabled')
try:    
    menu = Menu(root)
    files = Menu(menu,tearoff=0)
    files.add_command(label="New Database",command=new_db)
    files.add_command(label="Load Database",command=load_db)
    files.add_command(label="Dump Code",command=dump_db_code)
    menu.add_cascade(menu=files,label="File")

    root = Tk()
    root.title("Querify")
    root.geometry("900x600")
    root.config(menu=menu)

except Exception as error:
    secure_error(error)

mainloop()


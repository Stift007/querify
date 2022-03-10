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
db = sqlite3.connect(":memory:")


def new_db():...
def dump_db_code():...

def loadTable():

    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(f"PRAGMA table_info({c_table.get()});")
    cursor.execute(f"PRAGMA table_info({c_table.get()});")
    columns = cursor.fetchall()
    tree = ttk.Treeview(root, columns=columns, show='headings')
    truecolumns = []
    for c in columns:
        truecolumns.append(c[1])
    tree['columns'] = tuple(truecolumns)
    Button(text='Load',command=loadTable).place(x=40,y=10)
    tree.column("#0",width=50,minwidth=25)
    tree.heading("#0",text='ID')
    for c in truecolumns:
        tree.column(c,anchor=W,width=50)
        tree.heading(c,text=c)
    t = c_table.get()
    data = f'SELECT * FROM {t};'
    print(data)
    cursor.execute(data)
    print(c_table.get())
    all_ = cursor.fetchall()
    print(all_)
    for data in all_:
        tree.insert('','end', iid=all_.index(data),text=all_.index(data),values=tuple(data))
        
    tree.place(x=5,y=50)

def create_widgets():
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    c_table.set(tables[0][0])
    w = OptionMenu(root, c_table, tables[0][0], *tables)
    w.place(x=5,y=10)
    print(f"PRAGMA table_info({c_table.get()});")
    cursor.execute(f"PRAGMA table_info({c_table.get()});")
    columns = cursor.fetchall()
    tree = ttk.Treeview(root, columns=columns, show='headings')
    truecolumns = []
    for c in columns:
        truecolumns.append(c[1])
    tree['columns'] = tuple(truecolumns)
    Button(text='Load',command=loadTable).place(x=500,y=10)
    tree.column("#0",width=50,minwidth=25)
    tree.heading("#0",text='ID')
    for c in truecolumns:
        tree.column(c,anchor=W,width=50)
        tree.heading(c,text=c)
    t = c_table.get()
    data = f'SELECT * FROM {t};'
    print(data)
    cursor.execute(data)
    print(c_table.get())
    all_ = cursor.fetchall()
    print(all_)
    for data in all_:
        tree.insert('','end', iid=all_.index(data),text=all_.index(data),values=tuple(data))
        
    tree.place(x=5,y=50)

def load_db():
  try:
    global db_path,db
    db_path = filedialog.askopenfilename(filetypes=(("SQL Database",".db"),))
    db = sqlite3.connect(db_path)
    create_widgets()
  except Exception as error:
      secure_error(error)


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
    root = Tk()
    menu = Menu(root)
    files = Menu(menu,tearoff=0)
    files.add_command(label="New Database",command=new_db)
    files.add_command(label="Load Database",command=load_db)
    files.add_command(label="Dump Code",command=dump_db_code)
    menu.add_cascade(menu=files,label="File")

    root.title("Querify")
    root.geometry("900x600")
    root.config(menu=menu)
    c_table = StringVar(root)   

except Exception as error:
    secure_error(error)

mainloop()


# We create tabbed widgets using notebook
import tkinter as tk
from tkinter import ttk
from tkinter.constants import TRUE
win=tk.Tk()
win.title('Tabbed Widgets')
nb=ttk.Notebook(win) # by this we can create multiple tabs which contains widgets
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='ONE') 
nb.add(page2,text='TWO')
nb.pack(expand=True,fill='both') # this will expand the size box of widgets both horizontally and vertically
label1=ttk.Label(page1,text='This is entry for first page: ')
label1.grid()
label2=ttk.Label(page2,text='This is entry for second page: ')
label2.grid()
entry1=ttk.Entry(page1,width=26)
entry1.grid(row=0,column=1)
entry2=ttk.Entry(page2,width=26)
entry2.grid(row=0,column=1)
win.mainloop()
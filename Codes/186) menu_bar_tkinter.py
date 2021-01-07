# It's a request to the learner plz first comment out the Advanced Menubar section then run it and afterwards comment out the 
# Simple MenuBar section the run it
import tkinter as tk
from tkinter import Label, ttk

def func():
    print("func was called!!")

win=tk.Tk()
win.title("MenuBar")

#************Simple MenuBar******************
# menubar=tk.Menu(win)
# menubar.add_command(label='Save',command=func)
# menubar.add_command(label='Save As',command=func)
# menubar.add_command(label='Copy',command=func)
# menubar.add_command(label='Paste',command=func)
# win.config(menu=menubar) # instead of using grid or pack we use this line of code!!

#***********Advanced Menubar*****************
new_menu=tk.Menu(win)

file_menu=tk.Menu(new_menu,tearoff=0) # this will remove the dotted lines which appears above the dropdown list
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator() # this will add a line between 'New Window' option and 'Open File' option
file_menu.add_command(label='Open File',command=func)

edit_menu=tk.Menu(new_menu,tearoff=0)
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)

new_menu.add_cascade(label='Edit',menu=edit_menu)
new_menu.add_cascade(label='File',menu=file_menu) # this will cascade all the 'file_menu' commands to the 'File' like drop down list

win.config(menu=new_menu,padx=40)

win.mainloop()

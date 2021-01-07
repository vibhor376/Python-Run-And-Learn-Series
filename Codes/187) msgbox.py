import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()
win.title('MessageBox')

# label frames
l1=ttk.Labelframe(win,text='Contact info')
l1.grid(row=0,column=0,padx=40,pady=0)

# labels
lab1=tk.Label(l1,text="Enter your Name",font=('Comic Sans MS',12)) # this how you can add your font
lab1.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
lab2=tk.Label(l1,text='Enter your age',font=('Comic Sans MS',12))
lab2.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)

# Entry boxes
v1=tk.StringVar()
ent1=ttk.Entry(l1,width=30,textvariable=v1)
ent1.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)

v2=tk.StringVar()
ent2=ttk.Entry(l1,width=30,textvariable=v2)
ent2.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

# buttons
def func():
    name=v1.get()
    age=v2.get()
    if age=='' or name=='':
        m_box.showinfo('Error','Please enter in both the fields!!')
    else:
        try:
            age=int(age)
            print(f'Name: {name}')
            print(f'Age: {age}')
        except ValueError:
            m_box.showerror('Error!','Please enter age in digits only!!')

        
btn=ttk.Button(text='Submit',command=func)
btn.grid()

win.mainloop()
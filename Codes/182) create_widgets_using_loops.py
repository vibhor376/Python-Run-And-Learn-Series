# for loop
import tkinter as tk
from tkinter import Entry, Label, ttk
win=tk.Tk()
win.title('LOOP')

l=['What is your name: ','What is your age: ','What is your gender: ','Country: ','State: ','City: ']

# labels using loops
for i in range(len(l)):
    cur_label='label'+str(i)
    cur_label=ttk.Label(win,text=l[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

# entry boxes using loops
user_info={   # this is to store the information given by the user
    'Name': tk.StringVar(),
    'Age': tk.StringVar(),
    'Gender': tk.StringVar(),
    'Country': tk.StringVar(),
    'State': tk.StringVar(),
    'City': tk.StringVar()
}
counter=0
for i in user_info:
    curr_entry='entry'+i
    curr_entry=ttk.Entry(win,width=25,textvariable=user_info[i])
    curr_entry.grid(row=counter,column=1,sticky=tk.W)
    counter+=1

def submit():
    print(user_info['Name'].get())
    print(user_info['Age'].get())
    print(user_info['Gender'].get())
    print(user_info['Country'].get())
    print(user_info['State'].get())
    print(user_info['City'].get())

submit_btn=ttk.Button(win,text="SUBMIT",command=submit)
submit_btn.grid(row=counter,column=0,sticky=tk.W)
win.mainloop()
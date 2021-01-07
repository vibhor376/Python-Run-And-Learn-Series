import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("LabelFrame")
label_frame=tk.LabelFrame(win,text='Enter your text below')
label_frame.grid(row=0,column=0,padx=10)

l=['What is your name: ','What is your age: ','What is your gender: ','Country: ','State: ','City: ']
for i in range(len(l)):
    cur_label='label'+str(i)
    cur_label=ttk.Label(label_frame,text=l[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

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
    curr_entry=ttk.Entry(label_frame,width=25,textvariable=user_info[i])
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
submit_btn.grid(row=1,column=0)

for i in label_frame.winfo_children(): # this will add padding to all the elements in the label frame
    i.grid_configure(padx=4,pady=4)

win.mainloop()
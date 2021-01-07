# starter code (these three lines are must for any gui application creation using tkinter)
# import tkinter
# win=tkinter.Tk()
# win.mainloop() # if you do not write this line then when you run the code our application will terminate as soon as it starts
import tkinter as tk # or from tkinter import * --> by this you can write tkinter.Tk() as Tk()
from tkinter import StringVar, ttk
import os
win=tk.Tk()
win.title('Learning Tkinter!') # this will give the title to your application

# Creating Labels
# widgets --> labels, buttons, radio buttons -- these are available in both tk and ttk module but ttk module has better display style

name_label=ttk.Label(win,text='Enter your Name: ') 
name_label.grid(sticky=tk.W) # by default it will place it in top left corner
# another method to do this is using ttk.Label(win,text='Enter your Name: ').pack() , this will place it at top center 

age_label=ttk.Label(win,text="Enter your Age: ")
age_label.grid(row=1,column=0,sticky=tk.W) # sticky=tk.W will stick the text towards West('W')(or remove spaces on the left side)   

email_label=ttk.Label(win,text="Enter your Email Address: ")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Please Select Your Gender: ')
gender_label.grid(row=3,column=0,sticky=tk.W)

profession_label=ttk.Label(win,text="You are:")
profession_label.grid(row=4,column=0,sticky=tk.W)

# Creating Entry box (where user will type something!)

name_var=tk.StringVar()
name_entrybox=tk.Entry(win,width=30,textvariable=name_var) # this store the entered string by user into name_var
name_entrybox.grid(row=0,column=1,sticky=tk.W)

name_entrybox.focus() # whenever the application is opened the cursor will be on the "Name:" entry box  

age_var=tk.StringVar()
age_entrybox=tk.Entry(win,width=30,textvariable=age_var)
age_entrybox.grid(row=1,column=1,sticky=tk.W)

email_var=tk.StringVar()
email_entrybox=tk.Entry(win,width=30,textvariable=email_var)
email_entrybox.grid(row=2,column=1,sticky=tk.W)

# Creating a combo box (or drop down list)

gender_var=tk.StringVar()
gender_combo=ttk.Combobox(win,width=27,textvariable=gender_var,state='readonly') # this state='readonly' means will restrict the
# user from writing anything on this box
gender_combo['values']=('Male','Female','Others')
gender_combo.current(0) # this will by default display 'Male' on the combobox
gender_combo.grid(row=3,column=1,sticky=tk.W)

# Creating the radio button

usertype=StringVar()
radio_btn1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radio_btn1.grid(row=4,column=1,sticky=tk.W)

radio_btn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radio_btn2.grid(row=4,column=2,sticky=tk.W)
# Notice that same name of variable is used. This is done to make user to select only one of the options!

# Creating a check button

checkbtn_var=tk.IntVar() # this will have value 1 for checked and 0 for not checked
checkbtn=ttk.Checkbutton(win,text='Want to Subscribe Our Newsletter',variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3,sticky=tk.W) # this columnspan=3 will allow the text to extend to 3 columns without 
# distrubing the original columns

# Creating a button

def action():
    username=name_var
    userage=age_var
    useremail=email_var
    usergender=gender_var
    useris=usertype
    if checkbtn_var.get():
        subscribed="YES"
    else:
        subscribed="NO"
    with open('User_Enrolled.txt','a') as f:
        if os.stat('User_Enrolled.txt').st_size==0: # this will check whether the file is empty or not
            f.write('\n')
        f.write('USER\n')
        f.write(f'Name:      {username.get()}\n')
        f.write(f'Age:       {userage.get()}\n')  # .get() is used to get the values stored in the variables bu the user
        f.write(f'Email:     {useremail.get()}\n')
        f.write(f'Gender:    {usergender.get()}\n')
        f.write(f'User is a: {useris.get()}\n')
        f.write(f'Subsciber: {subscribed}\n')
        
        # these lines below will clear the name, age, email fields after the user submits
        name_entrybox.delete(0,tk.END)
        age_entrybox.delete(0,tk.END)
        email_entrybox.delete(0,tk.END)

        # changing color of every label after submitting
        name_label.config(foreground='Blue')
        age_label.config(foreground='Red')
        email_label.config(foreground='#FF7100') # passing hex values
        gender_label.config(foreground='Green') # passing normal color

button_var=ttk.Button(win,text="Submit",command=action) # this command = action will give instructions to button to do work
# according to some function(here 'action') when clicked
button_var.grid(row=6,column=0,sticky=tk.W)

# Note: if you want to change color of button text using .conifg then use tk not ttk 

win.mainloop()



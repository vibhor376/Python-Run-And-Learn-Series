from csv import DictWriter
with open('file3.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['Firstname','Lastname','Age']) 
    csv_writer.writeheader() # this will create our headers with Firstname,Lastname,Age
    # methods --> writerow and writerows
    # writerow()
    csv_writer.writerow({
        'Firstname':'Akshat',
        'Lastname':'Bhatnagar',
        'Age': 20
    })
    csv_writer.writerow({
        'Firstname':'Lekhansh',
        'Lastname':'Bhatnagar',
        'Age': 16
    })
    # writerows() --> [dict,dict,dict,...]
    csv_writer.writerows([{'Firstname':'Vibhor','Lastname':'Bhatnagar','Age':19},{'Firstname':'Yatharth','Lastname':'Bhatnagar','Age':16}])

    # Note: DictWriter is better than writer and DictReader is better than reader
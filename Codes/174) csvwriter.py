from csv import writer
with open('file2.csv','w',newline='') as f:    # this newline='' will write in the file by avoiding the extra spaces
    csv_writer=writer(f)
    # methods --> writerow and writerows
    # writerow()
    csv_writer.writerow(['Name','Country'])  
    csv_writer.writerow(['Akshat','INDIA'])  
    csv_writer.writerow(['Lekhansh','INDIA'])  
    # writerows()  --> [list,list,list,..]
    csv_writer.writerows([['Vibhor','INDIA'],['Yatharth','INDIA']]) # it takes list of lists 
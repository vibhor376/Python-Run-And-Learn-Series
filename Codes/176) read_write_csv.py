from csv import DictReader,DictWriter
import csv
with open('Output.csv','w',newline='') as wf:
    with open('file3.csv','r') as rf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['First_Name','Last_Name','Age'])
        csv_writer.writeheader()
        for i in csv_reader:
            csv_writer.writerow({
                'First_Name':i['Firstname'],
                'Last_Name':i['Lastname'],
                'Age':i['Age']
            })
        


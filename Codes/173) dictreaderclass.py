from csv import DictReader
# ordered dictionary
with open('file.csv','r') as f:
    csv_reader=DictReader(f,delimiter='|') # this will tell that our csv file has content separated by '|' by default it is ','
    print(csv_reader)
    for row in csv_reader: # it will print the contents of csv file in ordered dictionary format
        print(row) 
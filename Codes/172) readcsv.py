# Read .CSV files 
# CSV stands for comma separated values
from csv import reader
with open('file.csv','r') as f:
    csv_reader=reader(f) # it is an iterator
    print(csv_reader)  # it will print something like this <_csv.reader object at 0x000002983E6E7EE0> because it is an object
    next(csv_reader) # to avoid printing the header of the file
    for row in csv_reader: # this is iterator so only one time it will print the values
        print(row)

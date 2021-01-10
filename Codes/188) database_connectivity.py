import mysql.connector

conn= mysql.connector.connect(host='localhost',username='Your Username',password='Your Password')

print(conn) # this is the object of the connector

my_cursor=conn.cursor() # this will create the cursor

query='CREATE DATABASE New_Database' # this the query

my_cursor.execute(query) # this will execute our query

conn.commit()  # to reflect the changes in sql
conn.close() # to close the connection

conn= mysql.connector.connect(host='localhost',username='Your Username',password='Your Password')

my_cursor=conn.cursor()
query='SHOW DATABASES'
my_cursor.execute(query)

# This method will give all the databases in the tuple format!!
for i in my_cursor:
    print(i)

# print(my_cursor.fetchall()) # This will print all the databases in list format!!

conn.commit()
conn.close()

conn1= mysql.connector.connect(host='localhost',username='Your Username',password='Your Password',database='new_database') # this will open the "new_database" 
myc=conn1.cursor()
query1='CREATE TABLE Students (First_Name VARCHAR(200),Last_Name VARCHAR(200))'
myc.execute(query1)
conn1.commit()
conn1.close()

conn2= mysql.connector.connect(host='localhost',username='Your Username',password='Your Password',database='new_database')
myc1=conn2.cursor()
query2='INSERT INTO Students (First_Name,Last_Name) VALUES (%s,%s)' # %s is used to take all the values from the list of tuples!!
values=[('Akshat','Bhatnagar'),('Preet','Kothari'),('Lekhansh','Bhatnagar'),('Kartikay','Maharshi')]
myc1.executemany(query2,values)
conn2.commit()
conn2.close()

conn3= mysql.connector.connect(host='localhost',username='Your Username',password='Your Password',database='new_database')
myc2=conn3.cursor()
query3='SELECT * FROM Students'
myc2.execute(query3)
print(myc2.fetchall())
# for i in myc2:
#     print(i)
conn3.commit()
conn3.close()

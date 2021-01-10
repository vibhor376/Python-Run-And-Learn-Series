import os
import shutil

os.chdir(r'D:\ieeepromo(materials)')
fileiter= os.walk(r'D:\ieeepromo(materials)')  # this is a generator object and it contains 3 different values which contains 
# current path, folder names and file names in the list format
print(fileiter) 
for current_path,folder_names,file_names in fileiter:
    print(f"Current Path: {current_path}")
    print(f"Folder Names: {folder_names}")
    print(f"File Names: {file_names}")
# Note: it will perform depth first search!

os.rmdir(r'D:\Folder_by_Python_os_module') # this will delete only if the folder is empty otherwise it will give an error

open('test.txt','a').close() # creating a file named 'test.txt'

os.makedirs(r'D:\New\movies') # this will create folder named 'New' and also create a folder named 'movies' inside 'New' folder

# so in order to delete non-empty folders we use shutil module
shutil.rmtree(r'D:\New')  # this function does not place the deleted folder in recycle bin!

os.makedirs(r'D:\New\movies')
os.chdir(r'D:')

# suppose if we want to copy this above created folder into another folder, so, we do
shutil.copytree(r'D:\New',r'D:\ieeepromo(materials)/New') 

shutil.copy(r'D:\test.txt',r'D:\ieeepromo(materials)/test.txt') # this will copy the file
shutil.move(r'D:\test.txt',r'D:\ieee day/test_move.txt') # this will move the file and rename it as 'test_move'

shutil.move(r'D:\New',r'D:\ieee day/New')


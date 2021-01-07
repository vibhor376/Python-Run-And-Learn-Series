import os

print(os.getcwd()) # this will print the current working directory of the file

print(os.path.exists('Created_Folder')) # this will tell whether the folder exists or not

os.mkdir('Created_Folder') # this will create the folder named 'Created_Folder' in the current working directory

print(os.path.exists('Created_Folder'))
# Note: if you try to create a folder which exists already then it will show an error

open('Created_File.txt','a').close() # It will create a new file in the current working directory

os.mkdir(r'D:\Folder_by_Python_os_module') # this way you can create folder in another directory

os.chdir(r'D:') # this to change your current working directory

if os.path.exists('Folder_by_Python_os_module'):
    print("Already created")
else:
    os.mkdir('Folder_by_Python_os_module')

os.chdir(r'C:\Users\HP\PycharmProjects\Python training')
print(os.getcwd())

print(os.listdir()) # this will give the list of the files and folders in the current working directory
print(os.listdir(r'D:')) # this will give the list of the files and folders of the passed directory

for item in os.listdir(): # this will help us to print whole path of the files and folders
    print(os.path.join(os.getcwd(),item))



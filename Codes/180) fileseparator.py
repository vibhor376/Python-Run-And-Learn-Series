# In this program we will be having a folder which contains differnt types of files and we have to separate each type of file
# in the new folder
import os,shutil
dict_extension={
    'audio':('.mp3','.m4a','.wav','.flac'),
    'video':('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'document':('.pdf','.doc','.txt'),
    'images':('.JPG','.jpg','.png')
}

folder_path=input("Enter the folder path: ")

def file_search(folder_path,file_extension):
    # res=[]
    # for file in os.listdir(folder_path):
    #     for extension in file_extension:
    #         if file.endswith(extension):
    #             res.append(file)
    # return res
    return [file for file in os.listdir(folder_path) for extension in file_extension if file.endswith(extension)]

for type,exten in dict_extension.items():
    fpath=os.path.join(folder_path,type)
    os.mkdir(fpath)
    for item in file_search(folder_path,exten):
        fipath=os.path.join(folder_path,item)
        nfipath=os.path.join(fpath,item)
        shutil.move(fipath,nfipath)
        

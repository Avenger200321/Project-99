import shutil
import os
import time
def Main():
    deleted_folder_count = 0
    deleted_file_count = 0
    path = '/' #path to delete
    days = 30
    seconds = time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folder_count+=1
                break
            else : 
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                    if seconds>get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folder_count+=1
                for file in files :
                    file_path = os.path.join(root_folder,file)
                    if seconds>get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_file_count+=1
    else : 
        print('Path does not exist')
def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path is removed")
    else :
        print('Unable to delete')
def remove_file(path):
    if not os.remove(path):
        print("Path is removed")
    else :
        print('Unable to delete')
def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime
Main()
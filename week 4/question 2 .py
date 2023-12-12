import os
import shutil
import time

def is_file_modified_recently(file_path):
    
    mtime = os.stat(file_path).st_mtime
    ctime = os.stat(file_path).st_ctime

    
    current_time = time.time()

 
    time_diff = current_time - max(mtime, ctime)


    if time_diff <= 86400:
        return True
    else:
        return False

def update_files(file_list):
    for file in file_list:
        with open(file, 'a') as f:
            
            timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime())
            f.write(timestamp)

def main():
    
    files = os.listdir()

    
    recent_files = [file for file in files if is_file_modified_recently(file)]

    
    folder_name = "last_24hours"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    
    
    update_files(recent_files)

    for file in recent_files:
        shutil.move(file, os.path.join(folder_name, file))

if __name__ == '__main__':
    main()
    [2023-12-12 22:43:22]  
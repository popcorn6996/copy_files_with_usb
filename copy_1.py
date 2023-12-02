import os
import shutil


def copy_files(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_directory,file)
            shutil.copy2(source_path, destination_path)
        print("Files copied successfully")
        

source_directory = r"C:\Users\USER\Desktop\SOUND EFFECTS"
destination_directory =r"D:\destination_folder"


copy_files(source_directory, destination_directory)            
            
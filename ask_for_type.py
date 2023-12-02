import os
import shutil

def copy_specific_files(source_directory, destination_directory, file_extension):
    try:
        for root, dirs, files in os.walk(source_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                
                if file_name.lower().endswith(f".{file_extension.lower()}"):
                    destination_path = os.path.join(destination_directory, file_name)
                    shutil.copyfile(file_path, destination_path)
                    print(f"File Copied: {file_path} to {destination_path}")
                    
                else:
                    print(f"Skipped non-{file_extension.upper()}  file: {file_name}")
    except Exception as e:
        print(f"Error occurred: {e}")


source_directory = input('Enter source, MR JAMES BOURNE  ')
destination_directory = r"D:\specific files"
file_extension = input("Enter the file extension(eg. png, jpg, mp4)")     


copy_specific_files(source_directory, destination_directory, file_extension)                       
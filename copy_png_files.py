import os
import shutil

def copy_png_files(source_directory, destination_directory):
    try:
        for root, dirs, files in os.walk(source_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                
                if file_name.lower().endswith('.png'):
                    destination_path = os.path.join(destination_directory, file_name)
                    shutil.copyfile(file_path, destination_path)
                    print(f"File Copied: {file_path} to  {destination_path}")
                else:
                    print(f"Skipped non-png file: { file_name}") 
                    
    except Exception as e:
        print(f"Error occurred: {e}")   
        
source_directory = input('Enter your source. Mr Spy:   ')
destination_directory = r"D:\png files"


copy_png_files(source_directory, destination_directory)                        
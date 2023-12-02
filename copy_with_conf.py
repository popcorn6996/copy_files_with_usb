import os
import shutil


def copy_files_with_confirmaion(source_directory, destination_directory):
    try:
        for root, dirs, files in os.walk(source_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                
                file_size = os.path.getsize(file_path)    #This gets it in bytes 
                file_size_gb = file_size / 1024 **3 #Get it in Gigabyte
                destination_path = os.path.join(destination_directory, file_name)
                
                print(f"File: {file_name} - Size in GB: {file_size_gb} GB")
                user_input = input('Do you want to copy this file? (yes/no)').lower()
                
                
                if user_input == "yes":
                    if os.access(file_path, os.R_OK):
                        try:
                            shutil.copyfile(file_path, destination_path)
                            print(f"File copied: {file_path} to {destination_path}")
                        except PermissionError as e:
                            print(f"Permission denied error: {e}")    
                            
                    else:
                        print(f"No read access to file: ${file_path}") 
                else:
                    print('User entered a no, so he/she did not want to copy the files') 
                    return          
    except Exception as e:
        print(f"Error occured: {e}")  
        
        
  
source_directory = input("Enter the source directory path:  ")
destination_directory = r"D:\creed"



copy_files_with_confirmaion(source_directory, destination_directory)                        
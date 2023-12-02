import os
import shutil


source_directories = [
    r"C:\Users\USER\Desktop\slides",
    r"C:\Users\USER\Desktop\Desktop Screenshots",
    r"C:\Users\USER\Desktop\SOUND EFFECTS"
]

destination_directory = r"D:\copied_folders"


for source_dir in source_directories:
    if os.path.exists(source_dir):
        
        files = os.listdir(source_dir)
        
        for file_name in files:
            #create the source file path
            source_file_path = os.path.join(source_dir,file_name)
            
            if os.path.isfile(source_file_path):
                destination_path = os.path.join(destination_directory, file_name)
                
                shutil.copy(source_file_path, destination_path)
                print(f"Copied '{file_name}' to '{destination_directory}'")
                
    else:
        print('Source directory does not exist')    
        
print("We have been able to steal all of the files")                




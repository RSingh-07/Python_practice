import os 

# Specify the directory you want to list 
directory_path =  '.'

# List all files and directories in the specified path 
contents = os.listdir(directory_path)


# Print each files and directories in specified path
for item in contents:
    print(item)
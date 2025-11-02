import os
import shutil

a = os.listdir("dir")
print(a)

print(os.getcwd()) # Current working directory

print(os.path.exists("dir")) # True

print(os.path.exists("dev")) # False

# os.remove("") # Remove a file or a directory

# os.rmdir("") # Removes empty directory

# shutil.rmtree("empty_dir") # removes non-empty directory

# os.rename("dir/old_name.txt", "dir/new_name.txt") # rename a file or directory

shutil.copy("dev.txt", "John Doe.txt") # copy the dev.txt and paste it inside John Doe.txt and removes the existing content of John Doe.txt

if os.path.exists("dev.txt"): # Check if the file exists
    print("File Exists")


shutil.move("my_file.txt", "new_directory/")

















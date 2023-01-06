import os
import shutil

# Define the source and destination directories for the files
src_dir = "D:\\Ibrahim\\mohamed phone\\DCIM\\Camera"
dst_dir = src_dir + '\\files'

# Create the destination directory if it doesn't exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Get a list of all the files in the source directory
files = os.listdir(src_dir)

# Iterate through the list of files and copy_module each file to the destination directory
for file in files:
    if file.endswith('.txt') or file.endswith('.pdf'):
        shutil.copy(src_dir + '/' + file, dst_dir)
        print(f"{file} copied")


import os
import shutil

# Define the source and destination directories for the photos
src_dir = "D:\\Ibrahim\\mohamed phone\\DCIM\\Camera"
dst_dir = src_dir + '\\photos'

# Create the destination directory if it doesn't exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Get a list of all the files in the source directory
files = os.listdir(src_dir)

# Iterate through the list of files and copy each file to the destination directory
for file in files:
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif') or file.endswith(
            '.jpeg') or file.endswith('.bmp') or file.endswith('.tif') or file.endswith('.tiff'):
        shutil.copy(src_dir + '/' + file, dst_dir)

        print(file + ' copied')

import os
import shutil

# Define the source and destination directories for the photos
src_dir = "D:\\Ibrahim\\mohamed phone\\DCIM\\Camera"
dst_dir = src_dir + '\\videos'

# Create the destination directory if it doesn't exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Get a list of all the files in the source directory
files = os.listdir(src_dir)

# Iterate through the list of files and copy each file to the destination directory
for file in files:
    #video files
    if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv') or file.endswith(
            '.flv') or file.endswith('.wmv') or file.endswith('.mov') or file.endswith('.mpg') or file.endswith('.mpeg') or file.endswith('.3gp') or file.endswith('.3g2') or file.endswith('.m4v') or file.endswith('.webm') or file.endswith('.vob') or file.endswith('.ogv') or file.endswith('.ogg') or file.endswith('.drc') or file.endswith('.gifv') or file.endswith('.mng') or file.endswith('.qt') or file.endswith('.yuv') or file.endswith('.rm') or file.endswith('.rmvb') or file.endswith('.asf') or file.endswith('.amv') or file.endswith('.m4p') or file.endswith('.m4v') or file.endswith('.svi') or file.endswith('.mxf') or file.endswith('.roq') or file.endswith('.nsv') or file.endswith('.f4v') or file.endswith('.f4p') or file.endswith('.f4a') or file.endswith('.f4b'):
        shutil.copy(src_dir + '/' + file, dst_dir)

        print(file + ' copied')

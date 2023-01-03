import os
import shutil

# Define the source and destination directories for the audio files
src_dir = "D:\\Ibrahim\\mohamed phone\\DCIM\\Camera"
dst_dir = src_dir + '\\audio'

# Create the destination directory if it doesn't exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Get a list of all the files in the source directory
files = os.listdir(src_dir)

# Iterate through the list of files and copy each file to the destination directory
for file in files:
    if file.endswith('.mp3') or file.endswith('.aac') or file.endswith('.flac') or file.endswith('.ogg') or file.endswith(
            '.wav') or file.endswith('.m4a') or file.endswith('.wma') or file.endswith('.m4b') or file.endswith(
        '.m4p') or file.endswith('.amr') or file.endswith('.aiff') or file.endswith('.au') or file.endswith(
        '.mid') or file.endswith('.midi') or file.endswith('.mka') or file.endswith('.ra') or file.endswith(
        '.snd') or file.endswith('.ape') or file.endswith('.dsf') or file.endswith('.dff') or file.endswith(
        '.mpc'):
        shutil.copy(src_dir + '/' + file, dst_dir)
        print(f"{file} copied")


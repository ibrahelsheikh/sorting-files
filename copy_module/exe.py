import shutil
from pathlib import Path

# Define the source and destination directories for the photos
src_dir = Path("D:\_Projects\Downloads")
dst_dir = src_dir / 'photos'

# Create the destination directory if it doesn't exist
dst_dir.mkdir(exist_ok=True)

# Get a list of all the files in the source directory
files = src_dir.glob('*')

# Iterate through the list of files and copy_module each file to the destination directory
for file in files:
    if file.suffix in ['.jpg', '.png', '.gif', '.jpeg', '.bmp', '.tif', '.tiff', '.svg', '.webp', '.ico']:
        shutil.copy(file, dst_dir)
        print(f"{file} copied")

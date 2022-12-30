import os

# Set the directory where the files are located
directory = "D:\\Ibrahim\\mohamed phone\\DCIM\\Camera\\output"

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate over the files and rename them
for i, file in enumerate(files):
    # Get the file name and extension
    name, extension = os.path.splitext(file)
    old_name = os.path.join(directory, file)
    new_name = os.path.join(directory, str(i + 1) + extension)
    os.rename(old_name, new_name)

import shutil
from pathlib import Path


def copy_files(src):
    # Define the source and destination directories for the photos
    src_dir = Path(src)
    dst_dir = src_dir / 'files'

    # Create the destination directory if it doesn't exist
    dst_dir.mkdir(exist_ok=True)

    # Get a list of all the files in the source directory
    files = src_dir.glob('*')

    # Iterate through the list of files and copy_module each file to the destination directory
    for file in files:
        if file.suffix in ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.odp', '.ods', '.odg',
                           '.odf', '.txt', '.rtf', '.tex', '.wks', '.wps', '.wpd', '.csv']:
            shutil.copy(file, dst_dir)
            print(f"{file} copied")

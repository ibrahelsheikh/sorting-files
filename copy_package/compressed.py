import shutil
from pathlib import Path


def copy_compressed(src):
    # Define the source and destination directories for the photos
    src_dir = Path(src)
    dst_dir = src_dir / 'compressed files'

    # Create the destination directory if it doesn't exist
    dst_dir.mkdir(exist_ok=True)

    # Get a list of all the files in the source directory
    files = src_dir.glob('*')

    # Iterate through the list of files and copy_package each file to the destination directory
    for file in files:
        if file.suffix in ['.exe', '.msi', '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso', '.jar', '.war', '.apk',
                           '.deb', '.rpm']:
            shutil.copy(file, dst_dir)
            print(f"{file} copied")

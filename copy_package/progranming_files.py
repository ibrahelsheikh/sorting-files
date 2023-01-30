import shutil
from pathlib import Path


def copy_programming_files(src):
    # Define the source and destination directories for the files
    src_dir = Path(src)
    dst_dir = src_dir / 'programming_files'

    # Create the destination directory if it doesn't exist
    dst_dir.mkdir(exist_ok=True)

    # Get a list of all the files in the source directory
    files = src_dir.glob('*')

    # Iterate through the list of files and copy_package each file to the destination directory
    for file in files:
        if file.suffix in ['.py', '.c', '.cpp', '.java', '.js', '.php', '.rb', '.swift', '.go', '.pl', '.cs', '.scala',
                           '.kt', '.rs', '.dart', '.hs', '.erl', '.exs', '.fs', '.ml', '.fsx', '.vb', '.clj']:
            shutil.copy(file, dst_dir)
            print(f"{file} copied")

import shutil
from pathlib import Path


def copy_video(src):
    # Define the source and destination directories for the photos
    src_dir = Path(src)
    dst_dir = src_dir / 'videos'

    # Get a list of all the files in the source directory
    files = src_dir.glob('*')

    # Iterate through the list of files and copy_package each file to the destination directory
    for file in files:
        # video files
        if file.suffix in ['.mp4', '.avi', '.mkv', '.flv', '.wmv', '.mov', '.mpg', '.mpeg', '.3gp', '.3g2', '.m4v',
                           '.webm', '.vob', '.ogv', '.ogg', '.drc', '.gifv', '.mng', '.qt', '.yuv', '.rm', '.rmvb',
                           '.asf', '.amv', '.m4p', '.m4v', '.svi', '.mxf', '.roq', '.nsv', '.f4v', '.f4p', '.f4a',
                           '.f4b', '.h261', '.h262', '.h263', '.h264', '.h265', '.vp8', '.vp9', '.vp10', '.vp3',
                           '.vp4', '.vp5', '.vp6', '.vp7', '.vp9', '.vp10', '.theora', '.w', '.w64', '.w65', '.wv']:

            # Create the destination directory if it doesn't exist
            dst_dir.mkdir(exist_ok=True)

            shutil.copy(src_dir.joinpath(file), dst_dir)
            print(f"{file} copied")

from pathlib import Path
import shutil


def copy_audio(src):
    # Copy audio files from src to dst.
    src_dir = Path(src)
    dst_dir = src_dir/'audio'

    # Create the destination directory if it doesn't exist
    dst_dir.mkdir(exist_ok=True)

    # Get a list of all the files in the source directory
    files = src_dir.glob('*')

    # Iterate through the list of files and copy_package each file to the destination directory
    for file in files:
        if file.suffix in ['.mp3', '.wav', '.aiff', '.aif', '.aifc', '.aac', '.flac', '.m4a', '.ogg', '.wma', '.wv',
                           '.ape', '.alac', '.opus', '.tta', '.ac3', '.dts', '.amr', '.awb', '.mka', '.mpc', '.mpp',
                           '.ofr', '.ofs', '.spx', '.tak', '.wv', '.w64', '.w65', '.wv']:


            shutil.copy(src_dir / file, dst_dir)
            print(f"{file} copied")


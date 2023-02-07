import os
from pathlib import Path
import subprocess

from copy_package import files, audio, video, photos, compressed, progranming_files
import threading


def copy(path):
    t1 = threading.Thread(files.copy_files(path))
    t2 = threading.Thread(audio.copy_audio(path))
    t3 = threading.Thread(video.copy_video(path))
    t4 = threading.Thread(photos.copy_photos(path))
    t5 = threading.Thread(compressed.copy_compressed(path))
    t6 = threading.Thread(progranming_files.copy_programming_files(path))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    print("All files copied successfully")

    def remove_empty_dirs(path):
        if not os.path.isdir(path):
            return

        files = os.listdir(path)
        if len(files):
            for f in files:
                full_path = os.path.join(path, f)
                if os.path.isdir(full_path):
                    remove_empty_dirs(full_path)

        files = os.listdir(path)
        if len(files) == 0:
            os.rmdir(path)

    remove_empty_dirs(path)

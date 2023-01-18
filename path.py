from copy_module import files , audio , video , photos ,compressed , progranming_files
import threading

def copy (path):
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


if __name__ == '__main__':
    copy ("D:\_Projects\Downloads")

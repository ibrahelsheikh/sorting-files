from copy_module import files , audio , video , photos ,compressed , progranming_files

def copy (path):
    files.copy_files(path)
    audio.copy_audio(path)
    video.copy_videos(path)
    photos.copy_photos(path)
    compressed.copy_compressed(path)
    progranming_files.copy_programming_files(path)

if __name__ == '__main__':
    copy ("--your path--")

import face_recognition
import os

# Set the directory where the photos are stored
directory = '/path/to/photos'

# Load the photo of the person you want to recognize
target_image = face_recognition.load_image_file('target_photo.jpg')

# Encode the target image into a feature vector
target_encoding = face_recognition.face_encodings(target_image)[0]

# Iterate over the photos in the directory
for filename in os.listdir(directory):
    # Load the photo
    image = face_recognition.load_image_file(os.path.join(directory, filename))

    # Encode the photo into a feature vector
    encoding = face_recognition.face_encodings(image)[0]

    # Check if the target image and the current photo match
    result = face_recognition.compare_faces([target_encoding], encoding)

    # If there is a match, print a message
    if result[0]:
        print(f'Match found in {filename}')

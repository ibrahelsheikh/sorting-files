import cv2

# Load the Haar cascade classifier
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load an image
image_path = "C:\\Users\\ibrah\\PycharmProjects\\sorting-files-to-photos-videos\\detect-person\\img.jpg"
image = cv2.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print(f"Error: Could not load image at {image_path}")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    bboxes = classifier.detectMultiScale(gray_image)

    # Draw bounding boxes around the detected faces
    for (x, y, w, h) in bboxes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

# import tensorflow as tf
# import numpy as np
# import cv2
#
# # Load a pre-trained object detection model
# model = tf.saved_model.load("/path/to/model")
#
# # Load an image
# image = cv2.imread("img.jpg")
#
# # Run the model to get predictions
# predictions = model(image)
#
# # Filter the predictions to only keep those that correspond to people
# people_predictions = [pred for pred in predictions if pred.class_label == "person"]
#
# # Draw bounding boxes around the detected people
# for pred in people_predictions:
#     xmin, ymin, xmax, ymax = pred.bounding_box
#     cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
#
# # Display the image
# cv2.imshow("Image", image)
# cv2.waitKey(0)

import cv2
import os
import numpy as np

# Create LBPH Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset/cropped"

faces = []
labels = []

# Read all cropped face images
for filename in os.listdir(dataset_path):

    image_path = os.path.join(dataset_path, filename)

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        continue

    # Filename format:
    # User.1.1.jpg
    # User.2.15.jpg

    parts = filename.split(".")

    teacher_id = int(parts[1])

    faces.append(image)
    labels.append(teacher_id)

# Train Model
recognizer.train(faces, np.array(labels))

# Save Model
recognizer.save("trainer.yml")

print()
print("====================================")
print(" Model Trained Successfully!")
print("====================================")
print("Total Images :", len(faces))
print("Total Labels :", len(set(labels)))
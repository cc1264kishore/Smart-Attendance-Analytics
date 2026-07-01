import cv2
import os
import csv

# Load Face Detector
face_detector = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)

dataset_folder = "dataset"
output_folder = "dataset/cropped"

os.makedirs(output_folder, exist_ok=True)

# -----------------------------
# Read teachers.csv
# -----------------------------
teachers = {}

with open("teachers.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:

        teacher_id = row[0].strip()
        teacher_name = row[1].strip().lower()

        teachers[teacher_name] = teacher_id

# -----------------------------
# Process every teacher folder
# -----------------------------
for teacher_name in os.listdir(dataset_folder):

    input_folder = os.path.join(dataset_folder, teacher_name)

    if not os.path.isdir(input_folder):
        continue

    if teacher_name == "cropped":
        continue

    folder_name = teacher_name.lower()

    if folder_name not in teachers:
        print(f"Skipping {teacher_name} (Not found in teachers.csv)")
        continue

    teacher_id = teachers[folder_name]

    image_number = 1

    print(f"Processing {teacher_name} (ID {teacher_id})")

    for filename in os.listdir(input_folder):

        image_path = os.path.join(input_folder, filename)

        image = cv2.imread(image_path)

        if image is None:
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]

            output_name = f"User.{teacher_id}.{image_number}.jpg"

            output_path = os.path.join(
                output_folder,
                output_name
            )

            cv2.imwrite(output_path, face)

            image_number += 1

print()
print("===================================")
print("Dataset Preparation Completed!")
print("===================================")
import cv2
import csv
from attendance_manager import mark_attendance

# Load Face Detector
face_detector = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)

# Load Trained Model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")


# -----------------------------
# Get Teacher Name from CSV
# -----------------------------
def get_teacher_name(teacher_id):

    with open("teachers.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if row[0].strip() == str(teacher_id):
                return row[1].strip()

    return "Unknown"


def start_recognition():

    camera = cv2.VideoCapture(0)

    attendance_marked = False

    while True:

        success, frame = camera.read()

        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            attendance_status = ""

            # Crop Face
            face = gray[y:y+h, x:x+w]

            # Predict Face
            teacher_id, confidence = recognizer.predict(face)

            # Display Match Score
            match_score = max(0, min(100, int(100 - confidence)))

            # Recognition
            if confidence < 55:

                name = get_teacher_name(teacher_id)
                color = (0, 255, 0)

                if not attendance_marked:

                    if mark_attendance(teacher_id):
                        attendance_status = "Attendance Marked"
                    else:
                        attendance_status = "Already Marked"

                    attendance_marked = True

                else:
                    attendance_status = "Already Marked"

            else:

                name = "Unknown Person"
                color = (0, 0, 255)
                attendance_status = "Access Denied"

            # Draw Rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                color,
                2
            )

            # Name
            cv2.putText(
                frame,
                name,
                (x, y - 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # Match Score
            cv2.putText(
                frame,
                f"Match Score: {match_score}%",
                (x, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

            # Attendance Status
            cv2.putText(
                frame,
                attendance_status,
                (x, y + h + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

        cv2.imshow("Smart Attendance Analytics", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_recognition()
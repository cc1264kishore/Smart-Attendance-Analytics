import csv
from datetime import datetime


def mark_attendance(teacher_id):

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    with open("attendance.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 1:
                if row[0] == str(teacher_id) and row[1] == today:
                    return False

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [teacher_id, today, current_time, "Present"]
        )

    return True
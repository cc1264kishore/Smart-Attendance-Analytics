import csv
from datetime import datetime
from recognize_face import start_recognition

while True:
    print()
    print("===================================")
    print("   SMART ATTENDANCE ANALYTICS")
    print("===================================")

    print("1. Register Teacher")
    print("2. View Teachers")
    print("3. Mark Attendance (Manual)")
    print("4. Start AI Attendance")
    print("5. View Attendance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ==========================
    # 1. Register Teacher
    # ==========================

    if choice == "1":

        print("\nREGISTER TEACHER")

        teacher_id = input("Enter Teacher ID: ")
        teacher_name = input("Enter Teacher Name: ")
        teacher_department = input("Enter Teacher Department: ")

        duplicate = False

        with open("teachers.csv", "r") as file:
            next(file)

            for line in file:
                data = line.strip().split(",")

                if teacher_id == data[0]:
                    duplicate = True
                    break

        if duplicate:

            print("\nTeacher ID already exists!\n")

        else:

            with open("teachers.csv", "a") as file:
                file.write(
                    f"{teacher_id},{teacher_name},{teacher_department}\n"
                )

            print("\nTeacher Registered Successfully!\n")

    # ==========================
    # 2. View Teachers
    # ==========================

    elif choice == "2":

        print("\n========== TEACHERS ==========\n")

        with open("teachers.csv", "r") as file:

            next(file)

            for line in file:

                data = line.strip().split(",")

                print("Teacher ID        :", data[0])
                print("Teacher Name      :", data[1])
                print("Teacher Department:", data[2])
                print("------------------------------")

    # ==========================
    # 3. Manual Attendance
    # ==========================

    elif choice == "3":

        print("\nMARK ATTENDANCE\n")

        teacher_id = input("Enter Teacher ID: ")

        found = False

        with open("teachers.csv", "r") as file:

            next(file)

            for line in file:

                data = line.strip().split(",")

                if teacher_id == data[0]:
                    found = True
                    break

        if found:

            current = datetime.now()

            date = current.strftime("%Y-%m-%d")
            time = current.strftime("%H:%M:%S")

            status = "Present"

            already_marked = False

            with open("attendance.csv", "r") as file:

                next(file)

                for line in file:

                    data = line.strip().split(",")

                    if teacher_id == data[0] and date == data[1]:
                        already_marked = True
                        break

            if already_marked:

                print("\nAttendance already marked for today!\n")

            else:

                with open("attendance.csv", "a") as file:

                    file.write(
                        f"{teacher_id},{date},{time},{status}\n"
                    )

                print("\nAttendance Marked Successfully!\n")

        else:

            print("\nTeacher ID Not Found!\n")

    # ==========================
    # 4. AI Attendance
    # ==========================

    elif choice == "4":

        print("\nStarting AI Attendance...\n")

        start_recognition()

    # ==========================
    # 5. View Attendance
    # ==========================

    elif choice == "5":

        print("\n========== ATTENDANCE ==========\n")

        with open("attendance.csv", "r") as file:

            next(file)

            for line in file:

                data = line.strip().split(",")

                print("Teacher ID :", data[0])
                print("Date       :", data[1])
                print("IN Time    :", data[2])
                print("Status     :", data[3])
                print("------------------------------")

    # ==========================
    # 6. Exit
    # ==========================

    elif choice == "6":

        print("\nThank You for using Smart Attendance Analytics!")
        break

    else:

        print("\nInvalid Choice! Please try again.\n")
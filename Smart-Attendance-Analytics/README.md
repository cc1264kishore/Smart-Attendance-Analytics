# Smart Attendance Analytics

AI-powered attendance system built with Python, OpenCV, and LBPH face recognition.

## Features

- Teacher registration
- View teachers
- Manual attendance marking
- Face detection using Haar Cascade
- Face recognition using LBPH
- Multiple teacher support
- Automatic attendance marking
- Duplicate attendance prevention
- Unknown face handling
- CSV-based storage

## Requirements

- Python 3.10+
- OpenCV contrib package
- NumPy

## Install

```bash
pip install -r requirements.txt
```

## Project Structure

```text
Smart-Attendance-Analytics/
├── attendance_manager.py
├── prepare_dataset.py
├── train_model.py
├── recognize_face.py
├── main.py
├── teachers.csv
├── attendance.csv
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
└── dataset/
    └── <teacher_name>/
```

## How to use

### 1) Register teachers
Run:

```bash
python main.py
```

Choose **1. Register Teacher** and add teacher details to `teachers.csv`.

### 2) Add face images
Create one folder per teacher inside `dataset/`.

Example:

```text
dataset/
├── kishore/
└── vijay/
```

Add 100–200 clear face photos for each teacher.

### 3) Prepare the dataset
Run:

```bash
python prepare_dataset.py
```

This detects faces and saves cropped face images into `dataset/cropped/`.

### 4) Train the model
Run:

```bash
python train_model.py
```

This creates `trainer.yml`.

### 5) Start AI attendance
Run:

```bash
python main.py
```

Choose **4. Start AI Attendance**.

### 6) View attendance
Run:

```bash
python main.py
```

Choose **5. View Attendance**.

## Notes

- Do not upload personal face images to a public repository.
- Do not upload `trainer.yml` to GitHub if it was trained on personal data.
- The dataset and model should be generated locally by each user.

## Future upgrades

- CustomTkinter GUI
- Dashboard
- Charts
- PDF reports
- Database integration

# Smart-Attendance-Analytics
AI-powered Smart Attendance System using Python, OpenCV, and LBPH Face Recognition with Multi-Teacher Support.

### steps:
# 🚀 How to Use

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Attendance-Analytics.git
cd Smart-Attendance-Analytics
```

---

## Step 2: Install Required Packages

```bash
pip install opencv-contrib-python numpy
```

---

## Step 3: Create Dataset Folder

Inside the project, create the following structure:

```
dataset/
    teacher_name/
```

Example:

```
dataset/
    kishore/
```

Place 100–200 clear face images of the teacher inside the folder.

For multiple teachers:

```
dataset/
    kishore/
    vijay/
    rahul/
```

Each teacher should have their own folder.

---

## Step 4: Register Teachers

Run:

```bash
python main.py
```

Choose:

```
1. Register Teacher
```

Example:

```
Teacher ID : 1
Teacher Name : Kishore
Department : Cintel
```

Register every teacher before training.

---

## Step 5: Prepare Dataset

Run:

```bash
python prepare_dataset.py
```

This will:

- Detect faces
- Crop face images
- Save them inside:

```
dataset/cropped/
```

---

## Step 6: Train the Model

Run:

```bash
python train_model.py
```

This creates:

```
trainer.yml
```

which is used for face recognition.

---

## Step 7: Start AI Attendance

Run:

```bash
python main.py
```

Choose:

```
4. Start AI Attendance
```

The webcam will open.

If a registered teacher is recognized:

- ✅ Teacher name is displayed
- ✅ Attendance is marked automatically
- ✅ Duplicate attendance is prevented

If the face is unknown:

- ❌ Access Denied
- ❌ Attendance is not recorded

---

## Step 8: View Attendance

Run:

```bash
python main.py
```

Choose:

```
5. View Attendance
```

Attendance is displayed from:

```
attendance.csv
```

---

## Project Workflow

```
Register Teacher
        │
        ▼
Add Images to dataset/teacher_name/
        │
        ▼
Run prepare_dataset.py
        │
        ▼
Run train_model.py
        │
        ▼
trainer.yml Created
        │
        ▼
Start AI Attendance
        │
        ▼
Face Recognition
        │
        ▼
Attendance Stored in attendance.csv
```

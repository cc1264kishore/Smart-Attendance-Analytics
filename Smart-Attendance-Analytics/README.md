# 🎓 Smart Attendance Analytics

An AI-powered Smart Attendance System built using **Python**, **OpenCV**, and **LBPH Face Recognition**. The system automatically recognizes registered teachers through a webcam and records attendance while preventing duplicate entries.

---

## ✨ Features

- 👨‍🏫 Register Teachers
- 👥 Multiple Teacher Face Recognition
- 📷 Face Detection using Haar Cascade
- 🧠 Face Recognition using LBPH Algorithm
- ✅ Automatic Attendance Marking
- 🚫 Duplicate Attendance Prevention
- ❌ Unknown Face Detection
- 📄 CSV-based Data Storage
- 🤖 Automatic Model Training

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- NumPy
- CSV
- Haar Cascade Classifier
- LBPH Face Recognizer

---

## 📂 Project Structure

```
Smart-Attendance-Analytics/
│
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
│
├── attendance_manager.py
├── prepare_dataset.py
├── train_model.py
├── recognize_face.py
├── main.py
│
├── attendance.csv
├── teachers.csv
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Attendance-Analytics.git
cd Smart-Attendance-Analytics
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-contrib-python numpy
```

---

## 3️⃣ Register Teachers

Run the application

```bash
python main.py
```

Choose:

```
1. Register Teacher
```

Example

```
Teacher ID : 1
Teacher Name : Kishore
Department : Cintel
```

Register every teacher before training the model.

---

## 4️⃣ Create Dataset

Create a folder named **dataset**

Inside it, create one folder for each teacher.

Example:

```
dataset/
    kishore/
    vijay/
```

Place **100–200 face images** of each teacher inside their respective folder.

---

## 5️⃣ Prepare Dataset

Run:

```bash
python prepare_dataset.py
```

This will:

- Detect faces
- Crop faces
- Save processed images for training

---

## 6️⃣ Train the Face Recognition Model

Run:

```bash
python train_model.py
```

This generates:

```
trainer.yml
```

which is used during face recognition.

---

## 7️⃣ Start AI Attendance

Run:

```bash
python main.py
```

Choose:

```
4. Start AI Attendance
```

The webcam opens automatically.

If the face is recognized:

- ✅ Teacher name is displayed
- ✅ Attendance is marked automatically
- ✅ Duplicate attendance is prevented

If the face is unknown:

- ❌ Access Denied
- ❌ Attendance is not recorded

---

## 8️⃣ View Attendance

Run:

```bash
python main.py
```

Choose:

```
5. View Attendance
```

Attendance records are stored in:

```
attendance.csv
```

---

# 📌 Workflow

```
Register Teacher
        │
        ▼
Create Dataset Folder
        │
        ▼
Add Teacher Images
        │
        ▼
Prepare Dataset
        │
        ▼
Train Model
        │
        ▼
Start AI Attendance
        │
        ▼
Face Recognition
        │
        ▼
Attendance Recorded
```

---

## 📷 Screenshots

> Add screenshots of your application here.

Example:

- Main Menu
- Teacher Registration
- Face Recognition
- Attendance Records

---

## 📁 Output Files

### teachers.csv

Stores teacher information.

### attendance.csv

Stores daily attendance records.

---

## 🚀 Future Improvements

- 🎨 CustomTkinter GUI
- 📊 Attendance Dashboard
- 📈 Attendance Analytics
- 🗄️ MySQL Database Integration
- 📄 PDF Attendance Reports
- 🌐 Flask Web Application
- ☁️ Cloud Database Support

---

## 👨‍💻 Author

**Kishore C. R.**

Student, SRM Institute of Science and Technology

GitHub: https://github.com/YOUR_USERNAME

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!

import cv2
import os
import numpy as np

# Path to store face images and trained model
DATASET_PATH = "faces_dataset"
MODEL_PATH = "face_model.yml"

# Create dataset folder if not exists
os.makedirs(DATASET_PATH, exist_ok=True)

# Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Create LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

def detect_faces(frame):
    """Return list of face bounding boxes."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return faces, gray

def train_faces():
    """Train recognizer from dataset images."""
    faces, labels = [], []
    label_map = {}
    label_counter = 0

    for name in os.listdir(DATASET_PATH):
        person_path = os.path.join(DATASET_PATH, name)
        if not os.path.isdir(person_path):
            continue
        if name not in label_map:
            label_map[name] = label_counter
            label_counter += 1
        label = label_map[name]
        for file in os.listdir(person_path):
            img_path = os.path.join(person_path, file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            labels.append(label)

    if len(faces) > 0:
        recognizer.train(faces, np.array(labels))
        recognizer.write(MODEL_PATH)
        print("Training completed!")
    return label_map

def recognize_face(frame, label_map):
    faces, gray = detect_faces(frame)
    results = []
    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        try:
            label_id, confidence = recognizer.predict(roi)
            name = [k for k, v in label_map.items() if v == label_id][0]
            results.append((name, confidence, (x, y, w, h)))
        except:
            results.append(("Unknown", None, (x, y, w, h)))
    return results

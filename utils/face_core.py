import os
import cv2
import numpy as np

from ultralytics import YOLO

# Configuration
MODELS_DIR = os.path.join("data", "models")

def get_face_detector():
    """
    Returns a tuple of (YOLO model, Haar cascade detector).
    """
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    haar_cascade = cv2.CascadeClassifier(cascade_path)
    
    try:
        yolo_model = YOLO("yolov8n.pt")
    except Exception as e:
        print(f"Error loading YOLO: {e}")
        yolo_model = None
        
    return (yolo_model, haar_cascade)

def detect_faces(frame, detectors):
    """
    Detects exactly ONE face by finding the largest face via Haar Cascade.
    Returns a list of bounding boxes (x, y, w, h). If zero, returns [].
    """
    _, haar_cascade = detectors
    
    if haar_cascade is None:
        return []
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = haar_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    if len(faces) == 0:
        return []
        
    # We only want ONE face. Find the largest face in the frame
    best_face = None
    max_face_area = 0
    
    for (fx, fy, fw, fh) in faces:
        area = fw * fh
        if area > max_face_area:
            max_face_area = area
            best_face = (fx, fy, fw, fh)
            
    if best_face is None:
        return []
        
    return [best_face]

def train_recognizer(faces_dir):
    """
    Trains an LBPH recognizer on the faces in faces_dir.
    faces_dir should contain folders named 'Name_ID' with images inside.
    Returns trained recognizer and a dictionary mapping IDs to Names.
    """
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    faces = []
    ids = []
    name_map = {}
    
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir, exist_ok=True)
        return None, name_map
        
    for person_folder in os.listdir(faces_dir):
        person_path = os.path.join(faces_dir, person_folder)
        if not os.path.isdir(person_path):
            continue
            
        # Parse Name and ID
        parts = person_folder.split('_')
        if len(parts) < 2:
            continue
            
        name = parts[0]
        try:
            person_id = int(parts[1])
        except ValueError:
            continue
            
        name_map[person_id] = name
        
        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (200, 200)) # Enforce standardized size
                img = cv2.equalizeHist(img) # Maintain consistency with detection
                faces.append(img)
                ids.append(person_id)
                
    if len(faces) == 0:
        return None, name_map
        
    recognizer.train(faces, np.array(ids))
    return recognizer, name_map

import cv2
import face_recognition
import pickle

ENCODINGS_FILE = "known_faces.pkl"

def load_known_faces():
    """Load known face encodings."""
    try:
        with open(ENCODINGS_FILE, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("Encodings file not found. Please enroll faces first.")
        return {}

def recognize_face():
    """Detect and recognize a face."""
    known_faces = load_known_faces()
    video_capture = cv2.VideoCapture(0)

    print("Looking for faces...")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture video.")
            break

        # Find faces in the frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
            if True in matches:
                matched_idx = matches.index(True)
                name = list(known_faces.keys())[matched_idx]
                video_capture.release()
                cv2.destroyAllWindows()
                return name

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return None

import cv2
import face_recognition
import os
import pickle

# Directory to store encodings
ENCODINGS_FILE = "known_faces.pkl"

def load_encodings():
    """Load existing encodings from file."""
    if os.path.exists(ENCODINGS_FILE):
        with open(ENCODINGS_FILE, 'rb') as file:
            return pickle.load(file)
    return {}

def save_encodings(encodings):
    """Save encodings to file."""
    with open(ENCODINGS_FILE, 'wb') as file:
        pickle.dump(encodings, file)

def capture_and_encode(name):
    """Capture face and encode it."""
    video_capture = cv2.VideoCapture(0)

    print("Position your face in front of the camera and press 's' to save.")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture video. Exiting...")
            break

        # Show the video frame
        cv2.imshow("Face Enrollment", frame)

        # Wait for user input to save the frame
        key = cv2.waitKey(1)
        if key == ord('s'):  # 's' key to save
            # Find face locations and encodings
            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) != 1:
                print("Make sure exactly one face is visible!")
                continue

            face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
            video_capture.release()
            cv2.destroyAllWindows()
            return face_encoding

        elif key == ord('q'):  # 'q' key to quit
            print("Exiting without saving...")
            video_capture.release()
            cv2.destroyAllWindows()
            return None

def main():
    # Load existing encodings
    encodings = load_encodings()

    # Ask for the user's name
    name = input("Enter the name of the person to enroll: ").strip()

    # Capture and encode the face
    face_encoding = capture_and_encode(name)
    if face_encoding is not None:
        encodings[name] = face_encoding
        save_encodings(encodings)
        print(f"Face for {name} enrolled successfully!")

if __name__ == "__main__":
    main()

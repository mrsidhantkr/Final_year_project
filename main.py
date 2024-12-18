from face_recognition_module import recognize_face
from lcd_module import display_message
from motor_control_module import setup_motor, unlock_door
from activity_logger import log_activity

def main():
    setup_motor()
    display_message("Welcome!")
    print("Starting face recognition...")

    name = recognize_face()
    if name:
        print(f"Access granted to {name}")
        display_message(f"Welcome {name}!", 5)
        unlock_door()
        log_activity(name, "Access Granted")
    else:
        print("Access denied.")
        display_message("Access Denied!", 5)
        log_activity("Unknown", "Access Denied")

if __name__ == "__main__":
    main()

import RPi.GPIO as GPIO
import time

MOTOR_PIN1 = 24
MOTOR_PIN2 = 23
ENABLE_PIN = 25

def setup_motor():
    """Setup motor GPIO pins."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_PIN1, GPIO.OUT)
    GPIO.setup(MOTOR_PIN2, GPIO.OUT)
    GPIO.setup(ENABLE_PIN, GPIO.OUT)
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    GPIO.PWM(ENABLE_PIN, 1000).start(100)

def unlock_door():
    """Run motor to simulate unlocking the door."""
    print("Unlocking door...")
    GPIO.output(MOTOR_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    time.sleep(5)  # Run motor for 5 seconds
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)

# smart_plant_monitor.py
import RPi.GPIO as GPIO
import time

# Pin configuration
MOISTURE_PIN = 21

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOISTURE_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(MOISTURE_PIN) == GPIO.LOW:
            print("Soil is dry! Water your plant!")
        else:
            print("Soil moisture is sufficient.")
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
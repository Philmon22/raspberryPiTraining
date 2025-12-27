import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
LED_PIN = 37
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Toggle LED every second for 5 seconds
    for i in range(5):
        GPIO.output(LED_PIN, GPIO.HIGH)
        print(f"LED ON - {i+1}s")
        time.sleep(1)
        
        GPIO.output(LED_PIN, GPIO.LOW)
        print(f"LED OFF - {i+1}s")
        time.sleep(1)
        
finally:
    # Clean up
    GPIO.cleanup()
    print("GPIO cleanup complete")

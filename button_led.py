import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
BUTTON_PIN = 40
LED_PIN = 36
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    # Read button state
    button_state = GPIO.input(BUTTON_PIN)
    
    if button_state == GPIO.LOW:  # Button pressed
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
        print("Button pressed! LED ON")
        time.sleep(0.5)  # Debounce delay
    else:
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED OFF
        print("Button released! LED OFF")
    
    time.sleep(0.1)  # Polling delay
# led_state = False

# def button_callback(channel):
#     global led_state
#     # Debounce delay
#     time.sleep(0.2)
#     led_state = not led_state
#     GPIO.output(LED_PIN, led_state)
#     state_text = "ON" if led_state else "OFF"
#     print(f"Button pressed! LED turned {state_text}")

# try:
#     # Set up event detection for button press (falling edge = button pressed)
#     GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)
    
#     print("Listening for button presses on pin 36...")
#     print("Press Ctrl+C to exit")
    
#     # Keep the script running
#     while True:
#         time.sleep(1)
        
# except KeyboardInterrupt:
#     print("\nExiting...")
    
# finally:
#     # Clean up
#     GPIO.cleanup()
#     print("GPIO cleanup complete")

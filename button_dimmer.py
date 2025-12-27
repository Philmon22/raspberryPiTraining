import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.cleanup()  # Clean up any previous GPIO settings
GPIO.setmode(GPIO.BOARD)
BUTTON_PIN = 40
LED_PIN = 35
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
dimmer=GPIO.PWM(LED_PIN, 100)
dimmer.start(10)
time.sleep(2)
dimmer.ChangeDutyCycle(40)
time.sleep(2)
dimmer.ChangeDutyCycle(80)
time.sleep(2)
 
 


#used for button press
# button_pressed = False
# while True:
#     # Read button state
#     button_state = GPIO.input(BUTTON_PIN)
    
#     if button_state == GPIO.LOW:  # Button pressed
#         if not button_pressed:
#             GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
#             print("Button pressed! LED ON")
#             button_pressed = True
#             time.sleep(0.5)  # Debounce delay
#         else:
#             GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED OFF
#             print("Button released! LED OFF")
#             button_pressed = False
    
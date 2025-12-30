import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.cleanup()  # Clean up any previous GPIO settings
GPIO.setmode(GPIO.BOARD)
BUTTON_BRIGHTER_PIN = 40
BUTTON_DIMMER_PIN = 36
LED_PIN = 35
GPIO.setup(BUTTON_BRIGHTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_DIMMER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
led=GPIO.PWM(LED_PIN, 100)
led.start(0)

#used for button press
button_level = 0

# track previous states to detect edges (only trigger once per press)
brighter_prev = GPIO.HIGH
dimmer_prev = GPIO.HIGH
button_click=0
button_constant=1.3594 #100^(1/15) 15 button clicks. 
while True:
    # Read button state
    brighter_state = GPIO.input(BUTTON_BRIGHTER_PIN)
    dimmer_state = GPIO.input(BUTTON_DIMMER_PIN)
    

    # Detect press event: transition HIGH -> LOW
    if brighter_state == GPIO.LOW and brighter_prev == GPIO.HIGH:
        print("Brighter button pressed")
        if button_level < 100:
            button_click+=1
            button_level = min(100, button_constant**button_click)
            led.ChangeDutyCycle(button_level)
        else:
            print("LED is at maximum brightness")
        time.sleep(0.05)  # short debounce

    if dimmer_state == GPIO.LOW and dimmer_prev == GPIO.HIGH:
        print("Dimmer button pressed")
        if button_level > 1:
            button_click-=1
            button_level = max(0, button_constant**button_click)
            led.ChangeDutyCycle(button_level)
        else:
            print("LED is at minimum brightness")
            led.ChangeDutyCycle(0)
        time.sleep(0.05)  # short debounce

    # save states for next iteration
    brighter_prev = brighter_state
    dimmer_prev = dimmer_state

    time.sleep(0.01)  # small loop delay
 
    
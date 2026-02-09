#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.cleanup()  # Clean up any previous GPIO settings
GPIO.setmode(GPIO.BOARD)
BUTTON_RED_PIN = 37 #brown wire
BUTTON_BLUE_PIN = 36 #red wire
BUTTON_GREEN_PIN = 33 #Yellow wire
RED_LED_PIN = 13   #silver wire
BLUE_LED_PIN = 11 #white wire
GREEN_LED_PIN= 40 #orange wire
GPIO.setup(BUTTON_RED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_BLUE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_GREEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

#used for button press
Red_button_level = 0
Blue_button_level = 0
Green_button_level = 0


# track previous states to detect edges (only trigger once per press)
red_prev = GPIO.HIGH
blue_prev = GPIO.HIGH
green_prev = GPIO.HIGH
# button_click=0
GPIO.output(RED_LED_PIN, GPIO.LOW)  # Turn LED OFF
GPIO.output(BLUE_LED_PIN, GPIO.LOW)  # Turn LED OFF
GPIO.output(GREEN_LED_PIN, GPIO.LOW)  # Turn LED OFF
# button_constant=1.3594 #100^(1/15) 15 button clicks. 
try:
    while True:
        # Read button state
        Red_state = GPIO.input(BUTTON_RED_PIN)
        Blue_state = GPIO.input(BUTTON_BLUE_PIN)
        Green_state = GPIO.input(BUTTON_GREEN_PIN)
        

        # Detect press event: transition LOW -> HIGH (with pull-down, press = HIGH)
        if Red_state == GPIO.LOW and red_prev == GPIO.HIGH:
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)  # Turn LED OFF
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            print(" -> RED BUTTON PRESSED")
            GPIO.output(RED_LED_PIN, GPIO.HIGH)  # Turn LED ON
        elif Blue_state == GPIO.LOW and blue_prev == GPIO.HIGH:
            print(" -> BLUE BUTTON PRESSED")
            GPIO.output(RED_LED_PIN, GPIO.LOW)  # Turn LED OFF
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)  # Turn LED ON
        elif Green_state == GPIO.LOW and green_prev == GPIO.HIGH:
            print(" -> GREEN BUTTON PRESSED")
            GPIO.output(RED_LED_PIN, GPIO.LOW)  # Turn LED OFF
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Turn LED ON
        # else:
            # print()

        # save states for next iteration
        red_prev = Red_state
        blue_prev = Blue_state
        green_prev= Green_state

        time.sleep(0.01)  # small loop delay
    
except:
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    GPIO.output(BLUE_LED_PIN, GPIO.LOW)
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
    GPIO.cleanup()

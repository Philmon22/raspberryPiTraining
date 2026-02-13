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
rbutton_click=0
bbutton_click=0
gbutton_click=0
GPIO.output(RED_LED_PIN, GPIO.LOW)  # Turn LED OFF
GPIO.output(BLUE_LED_PIN, GPIO.LOW)  # Turn LED OFF
GPIO.output(GREEN_LED_PIN, GPIO.LOW)  # Turn LED OFF
rled=GPIO.PWM(RED_LED_PIN, 100)
bled=GPIO.PWM(BLUE_LED_PIN, 100)
gled=GPIO.PWM(GREEN_LED_PIN, 100)
rled.start(0)
bled.start(0)
gled.start(0)
button_constant=1.7783 #100^(1/8) 8 button clicks. 

try:
    while True:
        # Read button state
        Red_state = GPIO.input(BUTTON_RED_PIN)
        Blue_state = GPIO.input(BUTTON_BLUE_PIN)
        Green_state = GPIO.input(BUTTON_GREEN_PIN)
        

        # Detect press event: transition LOW -> HIGH (with pull-down, press = HIGH)
        if Red_state == GPIO.LOW and red_prev == GPIO.HIGH:
            print(" -> RED BUTTON PRESSED")
            if Red_button_level < 100:
                rbutton_click+=1
                Red_button_level = min(100, button_constant**rbutton_click)
                rled.ChangeDutyCycle(Red_button_level)
            else:
                print("turning red off")
                rbutton_click=0
                Red_button_level=0
                rled.ChangeDutyCycle(Red_button_level)
                # GPIO.output(RED_LED_PIN, GPIO.HIGH)  # Turn LED ON
        elif Blue_state == GPIO.LOW and blue_prev == GPIO.HIGH:
            print(" -> BLUE BUTTON PRESSED")
            if Blue_button_level < 100:
                bbutton_click+=1
                Blue_button_level = min(100, button_constant**bbutton_click)
                bled.ChangeDutyCycle(Blue_button_level)
            else:
                print("turning blue off")
                bbutton_click=0
                Blue_button_level=0
                bled.ChangeDutyCycle(Blue_button_level)
                # GPIO.output(BLUE_LED_PIN, GPIO.HIGH)  # Turn LED ON
        elif Green_state == GPIO.LOW and green_prev == GPIO.HIGH:
            print(" -> GREEN BUTTON PRESSED")
            if Green_button_level < 100:
                gbutton_click+=1
                Green_button_level = min(100, button_constant**gbutton_click)
                gled.ChangeDutyCycle(Green_button_level)
            else:
                print("turning green off")
                gbutton_click=0
                Green_button_level=0
                gled.ChangeDutyCycle(Green_button_level)
                # GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Turn LED ON
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

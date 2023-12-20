import RPi.GPIO as GPIO
import time
# Set the GPIO mode (BCM mode is used here)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pins for RGB LED
red_pin = 17    # GPIO pin for red
green_pin = 22  # GPIO pin for green
blue_pin = 27   # GPIO pin for blue

# Set up the GPIO pins as output
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)


# Function to set the color of the RGB LED
def set_colour(red, green, blue):
    GPIO.output(red_pin, red)
    GPIO.output(green_pin, green)
    GPIO.output(blue_pin, blue)


# 0,0,1 is yellow
# 0,1,0 is rainbow
# 1,1,0 is blue
# 101 is green
# 0,200,200 is red
def set_colour_red():
# Set the color to red
    set_colour(0,200 ,200)
    print("ALERT!!!")
    time.sleep(1)

#set_colour_red()

def reset_colour():
    set_colour(1,0,0)
    print("TEST")
    time.sleep(1)

#reset_colour()

def turn_off():
# Turn off the RGB LED
    print("Turning off!")
    GPIO.cleanup()

#turn_off()



"""
# Set the color to green
set_color(1, 0, 1)
print("green")
time.sleep(5)


# Set the color to blue
set_color(1, 0, 0)
print("blue")
time.sleep(5)
#yellow

# test colour
def test_colour():
    set_colour(1,1,1)
    print("Hejsa")
    time.sleep(5)
"""
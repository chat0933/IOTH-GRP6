import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pin
buzzer_pin = 18

# Set up GPIO pin for PWM
GPIO.setup(buzzer_pin, GPIO.OUT)
buzzer_pwm = GPIO.PWM(buzzer_pin, 1000)  # 1000 Hz PWM frequency

# Function to play a tone with variable volume
def play_tone(frequency, duration, volume=100):
    buzzer_pwm.ChangeDutyCycle(volume)
    buzzer_pwm.start(50)  # 50% duty cycle
    buzzer_pwm.ChangeFrequency(frequency)
    time.sleep(duration)
    buzzer_pwm.stop()

# Function to play a melody with variable volume
def play_melody(volume=100):
    melody = [
        (523, 1)
    ]

    for note in melody:
        play_tone(note[0], note[1], volume)

# Main loop
try:
    play_melody(volume=100)  # Adjust volume as needed

except KeyboardInterrupt:
    # Cleanup on keyboard interrupt
    GPIO.cleanup()

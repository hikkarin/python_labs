import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
for _ in range(20):
    GPIO.output(12, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(12, GPIO.LOW)
    sleep(0.1)
    GPIO.output(12, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    sleep(0.5)

GPIO.cleanup()
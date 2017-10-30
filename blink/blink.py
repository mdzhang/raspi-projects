import RPi.GPIO as GPIO
import time

LedPin = 11


def setup():
    GPIO.setmode(GPIO.BOARD)
    # specify pin in output mode
    GPIO.setup(LedPin, GPIO.OUT)
    # turn on led
    GPIO.output(LedPin, GPIO.HIGH)


def blink():
    while True:
        # turn on led
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(1)
        # turn off led
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(1)


def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()


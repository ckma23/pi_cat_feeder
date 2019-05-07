import RPi.GPIO as GPIO
import time as time

class LedLighter:
    def __init__(self,pin_number):
        self.pin_number = pin_number

    def setup_led(self):
        print ("setting up the board")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_number,GPIO.OUT)

    def light_up(self,number_of_times):
        counter = 0
        while counter < number_of_times:
            print ("LED on")
            GPIO.output(self.pin_number,GPIO.HIGH)
            time.sleep(3)
            print ("LED off")
            GPIO.output(self.pin_number,GPIO.LOW)
            time.sleep(3)
            counter += 1

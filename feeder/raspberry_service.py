import RPi.GPIO as GPIO

class LedLighter:
    def __init__(self,pin_number):
        self.pin_number = pin_number

    def setup_led():
        print ("setting up the board")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_number,GPIO.OUT)

    def light_up(number_of_times):
        while i < number_of_times:
            print ("LED on")
            GPIO.output(self.pin_number,GPIO.HIGH)
            time.sleep(1)
            print ("LED off")
            GPIO.output(self.pin_number,GPIO.LOW)
            i += 1

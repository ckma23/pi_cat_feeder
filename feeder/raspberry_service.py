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
            time.sleep(1)
            print ("LED off")
            GPIO.output(self.pin_number,GPIO.LOW)
            time.sleep(1)
            counter += 1

        GPIO.cleanup()

class FeederMotor:
    def __init__(self,pin_number):
        self.pin_number = pin_number

    def setup_motor(self):
        print ("setting up motor")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_number, GPIO.OUT)

    def motor_move(self,number_of_times):
        p = GPIO.PWM(self.pin_number,50)
        counter = 0
        p.start(1)
        while counter < number_of_times:
            print ("moving motor")
            p.ChangeDutyCycle(5)
            time.sleep(2)
            p.ChangeDutyCycle(1)
            time.sleep(2)
            # p.ChangeDutyCycle(5)
            # time.sleep(1)
            counter += 1
        GPIO.cleanup()

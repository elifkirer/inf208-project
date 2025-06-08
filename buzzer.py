import RPi.GPIO as GPIO
import time

BUZZER = 4 # BOARD da 7
def buzzer(pin): 
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.35)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.35)
    return
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)
for i in range (0,5):
    buzzer(BUZZER)
GPIO.cleanup()
GPIO.output(BUZZER,GPIO.HIGH)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SERVO = 27 # BOARD da 13

GPIO.setup(SERVO, GPIO.OUT)

pwm = GPIO.PWM(SERVO, 50)
# servolar icin genel olarak 50Hz kullanilir
pwm.start(0)

def setAngle(angle):
    duty = (angle / 18)
    GPIO.output(SERVO, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO, False)
    pwm.ChangeDutyCycle(0)

try:
    
    while True:
        i = 0
        print ("angle = ", i)
        setAngle(i)
        time.sleep(1)
        setAngle(90)
        time.sleep(1)
        setAngle(180)
        time.sleep(1)
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SERVO = 18 # BOARD da 12

GPIO.setup(SERVO, GPIO.OUT)

pwm = GPIO.PWM(SERVO, 100)
# servolar icin genel olarak 50Hz kullanilir
pwm.start(5)

def setAngle(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)

try:
    
    
#     while True:
    i = 10 # +90 derece dondurur
    print ("angle = ", 90)
    setAngle(i)
    time.sleep(1)
        
except KeyboardInterrupt:
    pwm.stop(5) # -90 derece dondurur
    GPIO.cleanup()
    

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SERVO = 18 # BOARD da 12

GPIO.setup(SERVO, GPIO.OUT)

pwm = GPIO.PWM(SERVO, 50)
# servolar icin genel olarak 50Hz kullanilir
pwm.start(0)

def setAngle(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

try:
    
    print ("angle = ", 80)
    setAngle(80)
    time.sleep(1)
    
    print ("angle = ", 35)
    setAngle(35)
    time.sleep(1)
    
    """
    istenilen acinin ayarlanmasi icin
    aci degerleri manuel ayarlandı
    (45 derece donecek)
    """    
except KeyboardInterrupt:
    pass
    
finally:
    pwm.stop() 
    GPIO.cleanup()    
    

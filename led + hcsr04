import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 11
ECHO = 8
LED = 26

print("HC-SR04 mesafe sensoru")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def blink(pin):
    for i in range(5):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.35)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.35)

def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    timeout = time.time() + 1
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start > timeout:
            return -1

    timeout = time.time() + 1
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end > timeout:
            return -1

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    if 2 < distance < 400:
        print("Mesafe:", distance - 0.5, "cm")
    else:
        print("Menzil aşıldı")

    return distance

try:
    while True:
        distance = measure_distance()
        if distance != -1 and distance < 15:
            blink(LED)
        time.sleep(1)

except KeyboardInterrupt:
    print("Program sonlandırıldı.")

finally:
    GPIO.cleanup()

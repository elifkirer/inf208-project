import RPi.GPIO as GPIO
import time

LDR_PIN = 20 # BOARD da 38

def rc_time(pin):
  count = 0
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)
  time.sleep(0.1)

  GPIO.setup(pin, GPIO.IN)

  while (GPIO.input(pin) == 0):
      count += 1

  return count

GPIO.setmode(GPIO.BCM)

try:
    while True:
        light_level = rc_time(LDR_PIN)
        print("İsik seviyesi:", light_level)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()        
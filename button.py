import RPi.GPIO as GPIO
import time

BUZZER = 4 # BOARD da 7
BUTTON = 17 # BOARD da 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT, initial=GPIO.HIGH) # baslangicta otmesi icin
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
"""
def buzzer(pin): 
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin,GPIO.HIGH)
    return
"""
def button_pressed(channel):
    if GPIO.input(channel) == GPIO.LOW: # Check if the button is actually pressed (LOW)
        print("Button pressed! Stopping buzzer.")
        GPIO.output(BUZZER, GPIO.LOW)    
try:    
    GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback = button_pressed, bouncetime = 300)    
# bounce suresi butonda olusan parazitleri engellemek icin, 300ms(0.3 sn) boyunca bir daha algılamayacak
    while True:
        time.sleep(0.1) # CPU kullanimini azaltmak icin uyutur
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()
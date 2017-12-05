import json
import time 
import RPi.GPIO as GPIO
pin_number = 18;

data = {1:"asdf"}
wert_des_schalters = False

while True:
#/* Sphinx Vorschlag */
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        time.sleep(1)
        if wert_des_schalters !=  GPIO.input(18) : # das ist gut
            time.sleep(1) # // Contact bounce protection
            print("wert wurde geaendert")
            wert_des_schalters = GPIO.input(pin_number)
            data = {1:wert_des_schalters}
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)


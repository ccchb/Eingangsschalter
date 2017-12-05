import json
import time 
import RPi.GPIO as GPIO
pin_number = 18;

data = {1:"asdf"}
wert_des_schalters = False

while True:
    time.sleep(10)  # Anzahl der sekunden, die gewartet wird

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    wert_des_schalters = GPIO.input(18)


    if wert_des_schalters == False:
        data = {1: wert_des_schalters}
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

    if wert_des_schalters == True: 
        data = {1: wert_des_schalters}
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)


#/* Sphinx Vorschlag */
'''

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    while true:
    sleep(10);
    
    if wert_des_schalters != GPIO:Input(pin_number)  # das ist gut
        sleep(1); // Contact bounce protection
        wert_des_schalters = GPIO.Input(pin_number)
        data = {1:wert_des_schalters}
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

'''

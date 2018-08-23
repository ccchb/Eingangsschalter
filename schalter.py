#!/usr/bin/env python3
#########################################################################
# Spaceapi Implementation for a 63A switch
# (using 5 V 150 mA Raspberry Pi GPIO pin)
#
#
#########################################################################

# to make sure that everything does not happen at once
import time
import datetime
# json and raspi imports
import json
# for using GPIO pins of the raspi
import RPi.GPIO as GPIO
# for logging
import logging
from systemd import journal

########################################################

#start init
journal.write("CCCHB space api switch v. 0.3")
currentState = False

#################################################################################
#function definitons:
#################################################################################

# will read the GPIO header of the pi and write the current state in the www spaceapi json file
def switched(pos):
    global currentState
    wert_des_schalters = not bool(GPIO.input(pin_number))
    if pos != wert_des_schalters:
      journal.write("state changed to: %s " %wert_des_schalters)
      chn_time = datetime.datetime.now().isoformat()
      icons = data.get("state").get('icon')
      data.update({'state':{'open':wert_des_schalters,'lastchange':chn_time, "icon":icons}})
      currentState = wert_des_schalters
      with open('/var/www/html/spaceapi.json', 'w') as outfile:
        json.dump(data, outfile,sort_keys=True)

#################################################################################

#init GPIO pin on raspi
pin_number = 18; #set GPIO Pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin_number, GPIO.BOTH, callback=switched, bouncetime=600)
journal.write("init complete... starting json foo")
#read json file
with open('spaceapi.json','r') as infile:
    data = json.load(infile)


#run switched once to get current switch status and change if needed.
#switched(wert_des_schalters)
try:
    while True:
        time.sleep(5)
        switched(currentState)
        #do other stuff otherwise just don't do anything?!
except KeyboardInterrupt:
    GPIO.cleanup()

#!/usr/bin/env python3
#########################################################################
# Spaceapi Implementation for a 63A switch
# (using 5 V 150 mA Raspberry Pi GPIO pin)
#
#
#########################################################################

# to make sure that everything does not happen at onec
import time
import datetime
# json and raspi imports
import json
# for using GPIO pins of the raspi
import RPi.GPIO as GPIO
# for logging
import logging
import systemd.journal

########################################################

#start init
log = logging.getLogger("SpaceAPI Schalter") #create a logger
log_fmt = logging.Formatter("%(levelname)s %(message)s") #define logging format
log_ch = JournalHandler() # create logging Handler
log_ch.setFormatter(log_fmt)
log.addHandler(log_ch)

log.setLevel(logging.INFO)
log.info("CCCHB space api switch v. 0.3 ")

#################################################################################
#function definitons:
#################################################################################

# will read the GPIO header of the pi and write the current state in the www spaceapi json file
def switched(pos):
    wert_des_schalters = not bool(GPIO.input(pin_number))
    icons= data.get("state").get('icon')
    if (pos!= wert_des_schalters):
      log.info("state changed to: ", wert_des_schalters)
      chn_time = datetime.datetime.now().isoformat()
      data.update({'state':{'open':wert_des_schalters,'lastchange':chn_time, "icon":icons}})
      with open('/var/www/html/spaceapi.json', 'w') as outfile:
        json.dump(data, outfile,sort_keys=True)
    return wert_des_schalters

#################################################################################

#init GPIO pin on raspi
pin_number = 18; #set GPIO Pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin_number, GPIO.BOTH, callback=switched, bouncetime=200)
log.info("init complete... starting json foo")
#read json file
with open('spaceapi.json','r') as infile:
    data = json.load(infile)
json.JSONDecoder(data) #decode json to python (may not be neccecary.)


#run switched once to get current switch status and change if needed.
#switched(wert_des_schalters)
currentValue = bool(0)
try:
    while True:
        time.sleep(1)
        currentValue = switched(currentValue)

        #include IRCBOT status here?
        #do other stuff otherwise just don't do anything?!
except KeyboardInterrupt:
    GPIO.cleanup()

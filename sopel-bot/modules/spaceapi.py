#!/usr/bin/env python3
import json
import sopel.module

SPACEAPI = "/var/www/html/spaceapi.json"
CHANNEL = "#ccchb"
PLACE = "ccchb"

cache = {
    "open": False
}

def get_spaceapi():
        with open(SPACEAPI, 'r') as infile:
                data = json.load(infile)
        return data

def status_msg(status):
    status_text = "closed"
    if status:
        status_text = "open"
    return PLACE + ' is ' + status_text

def change_status(bot, status):
    status_text = "closed"
    if status:
        status_text = "open"
    bot.say(PLACE +' changed to '+ status_text, CHANNEL)

    topic = status_msg(status)

    channel = bot.channels[CHANNEL]
    if channel.topic != None:
        topic = channel.topic.replace(status_msg(not status), topic)
    bot.write(('TOPIC', CHANNEL + ' :' + topic))

def check_status(bot, human=False):
    data = get_spaceapi()
    status = data["state"]["open"]

    if status != cache["open"]:
        cache["open"] = status
        if CHANNEL in bot.channels:
            change_status(bot, status)

    if human:
        bot.reply(status_msg(status))

@sopel.module.interval(5)
def interval_check_status(bot):
    check_status(bot)

@sopel.module.commands('status')
def cmd_check_status(bot, trigger):
    check_status(bot, True)

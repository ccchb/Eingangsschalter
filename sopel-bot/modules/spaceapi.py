#!/usr/bin/env python3
import json
import sopel.module

SPACEAPI = "/var/www/html/spaceapi.json"
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
    return '{} is {}'.format(PLACE, status_text)

def change_status(bot, status):
    status_text = "closed"
    if status:
        status_text = "open"
    for ch in bot.channels:
        bot.notice('{} changed to {}'.format(PLACE, status_text), ch)

    topic = status_msg(status)

    for ch in bot.channels:
        channel = bot.channels[ch]
        topic_new = topic
        topic_cur = status_msg(not status)
        if channel.topic != None:
            topic_new = channel.topic.replace(topic_cur, topic_new)
            topic_cur = channel.topic
        if topic_new != topic_cur:
            bot.write(('TOPIC', ch), topic_new)

def check_status(bot, human=False):
    data = get_spaceapi()
    status = data["state"]["open"]

    if status != cache["open"]:
        cache["open"] = status
        change_status(bot, status)

    if human:
        bot.reply(status_msg(status))

@sopel.module.interval(5)
def interval_check_status(bot):
    check_status(bot)

@sopel.module.commands('status')
def cmd_check_status(bot, trigger):
    check_status(bot, True)

#!/bin/sh
INSTALL_PATH=$PWD

# install dependencies
# apt-get install sopel nginx certbot

# install json (to save)
cp $INSTALL_PATH/spaceapi.json /var/www/html/spaceapi.json
chown pi:pi /var/www/html/spaceapi.json

# install mini-website
cp $INSTALL_PATH/www/index.html /var/www/html/index.html

# install ircbot
ln -s $INSTALL_PATH/sopel-bot/modules /home/pi/.sopel
if [ ! -f /home/pi/.sopel/default.cfg ]; then
	cp $INSTALL_PATH/sopel-bot/default.cfg /home/pi/.sopel/
fi

#install services
cp $INSTALL_PATH/systemd/schalter.service /etc/systemd/system
cp $INSTALL_PATH/systemd/ircbot.service /etc/systemd/system
systemctl daemon-reload
systemctl enable ircbot schalter
systemctl start ircbot schalter

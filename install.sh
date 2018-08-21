#!/usr/bin/bash
INSTALL_PATH=$PWD

# install dependencies
# apt-get install sopel nginx certbot

# install json (to save)
cp $INSTALL_PATH/spaceapi.json /var/www/html/spaceapi.json
chown pi:pi /var/www/html/spaceapi.json

# install mini-website
cp $INSTALL_PATH/www/index.html /var/www/html/index.html

# install ircbot
ln -s $INSTALL_PATH/sopel-bot /home/pi/.sopel

#install services
cp $INSTALL_PATH/systemd/{ircbot,schalter}.service /etc/systemd/system
systemctl daemon-reload
systemctl enable ircbot schalter
systemctl start ircbot schalter

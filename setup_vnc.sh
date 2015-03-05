#!/bin/sh

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install tightvncserver

tightvncpasswd

sudo ln -s /home/pi/raspberry_utils/vncboot /etc/init.d/vncboot
sudo chmod +x /etc/init.d/vncboot
sudo update-rc.d vncboot defaults

echo "remember to reboot..."

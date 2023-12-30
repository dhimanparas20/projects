sudo rm /var/lib/apt/lists/lock
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt-get upgrade-y
sudo apt-get install mosquitto mosquitto-clients -y
mosquitto -v
delay 2000
clear
sudo systemctl enable mosquitto.service
systemctl status mosquitto.service
sudo -i
echo "listner 1883" >> /etc/mosquitto/conf.d/my.conf
echo "allow_anonymous true" >> /etc/mosquitto/conf.d/my.conf
exit
sudo systemctl restart mosquitto.service

sudo rm /var/lib/apt/lists/lock
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt-get upgrade-y
sudo apt-get install mosquitto mosquitto-clients ufw -y
#mosquitto -v
delay 2000
clear
sudo systemctl enable mosquitto.service
systemctl status mosquitto.service
sudo -i
echo "persistence true" >> /etc/mosquitto/mosquitto.conf
echo "allow_anonymous false" >> /etc/mosquitto/mosquitto.conf
echo "password_file /etc/mosquitto/passwd" >> /etc/mosquitto/mosquitto.conf
echo "listener 1883 0.0.0.0" >> /etc/mosquitto/conf.d/protocols.conf
echo "protocol mqtt" >> /etc/mosquitto/conf.d/protocols.conf
echo "listener 1884 0.0.0.0" >> /etc/mosquitto/conf.d/protocols.conf
echo "protocol websockets" >> /etc/mosquitto/conf.d/protocols.conf
exit
sudo mosquitto_passwd -c /etc/mosquitto/passwd mst
sudo ufw allow 1883/tcp
sudo systemctl restart mosquitto.service

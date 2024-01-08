import configparser as cp

# Read configuration from file
cfg = cp.ConfigParser()
cfg.read('config.conf')


# READ VARIABLES from config file
USE_CREDS = cfg['MQTT']['USE_CREDS']  # True if MQTT is using Authentication
MQTT_USER = cfg['MQTT']['USER']   
MQTT_PASS = cfg['MQTT']['PASS']

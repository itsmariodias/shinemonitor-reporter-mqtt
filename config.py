debug = False  # True to enable, False to disable

# Shinemonitor settings
base_url = 'http://android.shinemonitor.com/public/'
usr = ''  # Username
pwd = ''  # Password
company_key = ''  # Company key. Obtained from portal
plant_id = ''  # Plant id (Power station ID). Obtained from portal.
pn = ''  # Datalogger PN number. Obtained from portal
sn = ''  # Device serial number. Obtained from portal
devcode = ''  # Device coding. Obtained from portal

# MQTT settings
interval_in_minutes = 5
hostname = 'localhost'
port = 1883
discovery_prefix = 'homeassistant'
base_topic = 'home/nodes'
sensor_name = 'shinemonitor-reporter'

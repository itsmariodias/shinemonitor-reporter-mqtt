# shinemonitor-reporter-mqtt
A ShineMonitor MQTT Reporter that publishes your Solar System information to an MQTT broker. 
The messages are configured to be automatically discovered as sensors in HomeAssistant.

## Installation
* Enter the required information in `config.py`. Most of the information is obtained from the [SolarPower Android App](https://play.google.com/store/apps/details?id=wifiapp.volfw.solarpower).
* Test whether the script is working by running `python get_data.py --latest` (If this doesn't work, please check whether all your plant information is correct).
* Ensure you have MQTT setup in your system. (Refer [this link](https://pimylifeup.com/raspberry-pi-mosquitto-mqtt-server/) if you're setting this up on a Raspberry Pi)
* Install the following python packages by running the command `pip install tzlocal paho-mqtt requests`.
* Starting the MQTT reporter is now as simple as running `python publish_data.py`.
* You should see your sensors appear in HomeAssistant as an MQTT device.

### Run as Systemd Daemon Service
Register the scripts to be run as a `systemd service` if you plan to run this on a Linux / Raspberry Pi system. That way you don't have to worry about starting / restarting it.  

Edit the `WorkingDirectory` and `ExecStart` lines in `shinemonitor_reporter_mqtt.service` to the directory in which this repository sits.

Then execute the below commands to register and enable the service.

```commandline
sudo ln -s shinemonitor_reporter_mqtt.service /etc/systemd/system/shinemonitor_reporter_mqtt.service

sudo systemctl daemon-reload

sudo systemctl enable shinemonitor_reporter_mqtt.service

sudo systemctl start shinemonitor_reporter_mqtt.service

sudo systemctl status shinemonitor_reporter_mqtt.service
```

### Note
* The sensors update their values every 5 minutes since that is how frequently ShineMonitor gets updated.
* I have added a `sensor_configuration.yaml` file that contains custom sensors that calculate some values that ShineMonitor does not provide directly for Solar Inverters. These are not 100% accurate and are only included to give a general sense of the battery and grid consumption.
* Exceptions get logged in a `error_log.txt` file. Most errors are response related as the API does not return expected values.

#### Adapted from works by:  
* https://github.com/ironsheep/RPi-Reporter-MQTT2HA-Daemon  
* https://github.com/sittzon/shinemonitor_api  
* https://github.com/MysterX83/shinemonitor_mqtt  
* API documentation: http://android.shinemonitor.com/chapter1/apiHelp.html

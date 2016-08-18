# Import package
import paho.mqtt.client as mqtt
import json
import Signal
import time


# Define Variables
MQTT_BROKER = "10.0.0.2"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "testTopic"



MQTT_MSG = "Hello MQTT"


# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	print "Connected to MQTT Broker"

# Define on_publish event Handler
def on_publish(client, userdata, mid):
	print "Message Published..."

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker


# Publish message to MQTT Topic 



while 1:
	real_time = time.strftime('%Y-%m-%d %H:%M:%S')

	IEEE, ESSID, Frequency, Access_Point, Bit_Rate, Tx_Power = Signal.signal_check()

	data = [ { 'time':real_time, 'location':"Moorestown Test House Point A", 'IEEE':IEEE, 'ESSID':ESSID, 'Frequency':Frequency, 'Access_Point':Access_Point, 'Bit_Rate':Bit_Rate, 'Tx_Power':Tx_Power } ]
	data_string = json.dumps(data)
#	print line.rstrip()+line2.rstrip()+line3.rstrip()
	print data_string

	mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 
	mqttc.publish(MQTT_TOPIC,data_string)
	mqttc.disconnect()

	time.sleep(1)

#file = open('input.txt', 'r')
#for line in file:
#	line2=file.next()
#	line3=file.next()
#	data = [ { 'time':line.rstrip(), 'location':line2.rstrip(), 'RF_Data':line3.rstrip() } ]
#	data_string = json.dumps(data)
##	print line.rstrip()+line2.rstrip()+line3.rstrip()
#	print data_string

#	mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 
#	mqttc.publish(MQTT_TOPIC,data_string)
#	mqttc.disconnect()


# Disconnect from MQTT_Broker


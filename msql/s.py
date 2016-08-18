import paho.mqtt.client as mqtt
import mysql.connector
import json

cnx = mysql.connector.connect(user='root', password='root',
                              database='mydb')

# Define Variables
MQTT_BROKER = "10.0.0.2"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "testTopic"


# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	#Subscribe to a the Topic
	mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"

# Define on_message event Handler
def on_message(mosq, obj, msg):

	print msg.payload
	j_data = json.loads(msg.payload)

	data = j_data[0]

	cursor = cnx.cursor()

	M_add = ("INSERT INTO Data "
           "(time, location, IEEE, ESSID, Frequency, Access_Point, Bit_Rate, Tx_Power) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

	M_data = (data['time'], data['location'], data['IEEE'],data['ESSID'], data['Frequency'], data['Access_Point'],data['Bit_Rate'], data['Tx_Power'])
	# print data['time']+data['location']+data['RF_Data']
	cursor.execute(M_add, M_data)
	cnx.commit()

	cursor.close()







# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue the network loop
mqttc.loop_forever()
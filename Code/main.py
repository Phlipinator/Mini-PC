# Code to initialize the MQTT client.
# Built upon code from: https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/ 

import time

import animations
import machine
import ubinascii
from machine import Pin
from umqttsimple import MQTTClient

# To create an MQTT client, we need to get the ESP unique ID
client_id = ubinascii.hexlify(machine.unique_id())

# MQTT Broker Data
mqtt_server = 'PUT MQTT SERVER HERE'
mqtt_port = 1883
mqtt_user = 'PUT USER HERE'
mqtt_pw = 'PUT PW HERE'

# Topic this ESP will subscribe to. Has to be specified as a bytestring (b'text').
topic2sub = b'miniPC_Julia'

# Topic this ESP will publish to. Has to be specified as a bytestring (b'text').
topic2pub = b'miniPC_Philipp'

#############
# Functions #
#############

# This callback function is called, when a message is received and should then begin handling that message.
def sub_cb(topic, msg):
    if msg == b'smile':
        animations.smile()
        publishMsg('received')
    elif msg == b'heart':
        animations.heart()
        publishMsg('received')
    elif msg == b'sad':
        animations.sad()
        publishMsg('received')
    elif msg == b'received':
        animations.received()
    else:
        print('Unhandeled Message')


# Connects to the MQTT broker specified within the mqtt_server variable.
def connectBroker():
    global client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_pw
    client = MQTTClient(client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_pw)
    client.set_callback(sub_cb)
    client.connect()
    print('Connected to MQTT broker: ' + mqtt_server)
    return client

# Connects to a topic on the connected MQTT broker. 
def subscribeTopic(topic):
    client.subscribe(topic)
    print('Subscribed to topic: ' + str(topic))

# Resets the ESP on failed connection in order to try again later.
def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

# Publishes a message to topic2pub.
def publishMsg(msg):
    try:
        client.publish(topic2pub, str.encode(msg))
    except Exception as e:
        print('Failed to publish to topic \'%s\' with error: %s' % (topic, e))

# Tries reading available messages and reboots on crash.
def tryRead():
    try:
        # Check whether a pending message from the server is available. If yes they are delivered to the callback function sepcified above.
        client.check_msg()

    except OSError as e:
        restart_and_reconnect() # On crash just reboot

#####################
# Execute on start: #
#####################
try:
    client = connectBroker() # Connect to broker
    print('MQTT connection successful!')
    
    subscribeTopic(topic2sub)

except OSError as e:
    print('Failed MQTT connection with error: %s' % e)
    restart_and_reconnect() # Try again later on fail.

# Initialize Buttons
buttonOne = Pin(1, Pin.IN, Pin.PULL_UP)
one = True

buttonTwo = Pin(3, Pin.IN, Pin.PULL_UP)
two = True

buttonThree = Pin(5, Pin.IN, Pin.PULL_UP)
three = True

###################
# Execution loop: #
###################
while True:
    tryRead()

    if not buttonOne.value() and one:
        publishMsg('smile')
        one = False
    elif buttonOne.value():
        one = True
        
    if not buttonTwo.value() and two:
        publishMsg('heart')
        two = False
    elif buttonTwo.value():
        two = True
        
    if not buttonThree.value() and three:
        publishMsg('sad')
        three = False
    elif buttonThree.value():
        three = True

    time.sleep(0.1)
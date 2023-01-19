from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import paho.mqtt.client as mqtt 

client = AWSIoTMQTTClient("A11")
client.configureEndpoint('a2028t9m0qzx3l-ats.iot.us-east-1.amazonaws.com',8883)
client.configureCredentials('AmazonRootCA1.pem','device-private.pem.key','device-certificate.pem.crt')

client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

client.connect()
print('connected to pipeline')

broker = "172.31.80.40"
port = 1883

client1 = mqtt.Client()
client1.connect(broker,port)
print('Broker Connected')

client1.subscribe('sacet/a11')

def notification(client1,userdata,msg):
    k = msg.payload
    k = k.decode('UTF-8')
    client.publish('aws/a11',k)

client1.on_message = notification
client1.loop_forever()
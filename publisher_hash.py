import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

while True:

    temp1 = random.randint(20,35)
    hum1 = random.randint(40,90)

    temp2 = random.randint(20,35)
    hum2 = random.randint(40,90)

    client.publish("room1/temperature", str(temp1))
    client.publish("room1/humidity", str(hum1))

    client.publish("room2/temperature", str(temp2))
    client.publish("room2/humidity", str(hum2))

    print("Data room1 dan room2 dikirim")

    time.sleep(3)
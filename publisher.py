import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

while True:
    suhu = random.randint(20, 35)

    client.publish("room/temperature", str(suhu))

    print(f"Mengirim suhu: {suhu}")

    time.sleep(3)
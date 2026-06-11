import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

while True:

    temperature = random.randint(20, 35)
    humidity = random.randint(40, 90)
    light = random.randint(100, 1000)

    client.publish("room/temperature", str(temperature))
    client.publish("room/humidity", str(humidity))
    client.publish("room/light", str(light))

    print("Temperature:", temperature)
    print("Humidity   :", humidity)
    print("Light      :", light)
    print("-------------------")

    time.sleep(3)
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Topik: {msg.topic}")
    print(f"Data : {msg.payload.decode()}")
    print("----------------")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("room/+")

print("Subscriber Wildcard + Aktif")

client.loop_forever()
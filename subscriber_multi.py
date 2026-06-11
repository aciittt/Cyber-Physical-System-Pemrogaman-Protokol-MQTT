import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):

    print(
        f"Topik: {msg.topic} | Data: {msg.payload.decode()}"
    )

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("room/temperature")
client.subscribe("room/humidity")
client.subscribe("room/light")

print("Monitoring Smart Room Aktif...")

client.loop_forever()
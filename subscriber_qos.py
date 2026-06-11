import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Topic : {msg.topic}")
    print(f"QoS   : {msg.qos}")
    print(f"Data  : {msg.payload.decode()}")
    print("----------------")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("room/qos", qos=2)

print("Subscriber QoS aktif...")

client.loop_forever()
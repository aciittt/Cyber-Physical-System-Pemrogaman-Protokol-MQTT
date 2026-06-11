import paho.mqtt.client as mqtt
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

client.loop_start()

for qos in [0, 1, 2]:

    pesan = f"Pesan dengan QoS {qos}"

    result = client.publish(
        "room/qos",
        pesan,
        qos=qos
    )

    result.wait_for_publish()

    print(f"Mengirim: {pesan}")

    time.sleep(2)

time.sleep(5)

client.loop_stop()
client.disconnect()
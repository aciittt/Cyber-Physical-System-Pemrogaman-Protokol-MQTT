# Cyber-Physical-System-Pemrogaman-Protokol-MQTT
Tugas Praktikum: Implementasi Komunikasi MQTT Menggunakan Python dan Mosquitto Broker

# MQTT Smart Room Monitoring

## Deskripsi Proyek

Proyek ini merupakan implementasi protokol MQTT (Message Queuing Telemetry Transport) menggunakan bahasa pemrograman Python dan Mosquitto Broker pada studi kasus Smart Room Monitoring. Sistem ini dibuat untuk memahami konsep komunikasi publish-subscribe pada Cyber Physical System (CPS) dan Internet of Things (IoT).

Dalam sistem ini, publisher berperan sebagai sensor virtual yang mengirimkan data suhu, kelembaban, dan intensitas cahaya ke broker MQTT. Subscriber berperan sebagai aplikasi monitoring yang menerima dan menampilkan data sesuai topik yang dilanggan.

---

## Tujuan

* Memahami konsep komunikasi publish-subscribe menggunakan MQTT.
* Mengimplementasikan MQTT menggunakan Python dan Mosquitto Broker.
* Mempelajari penggunaan Quality of Service (QoS) pada MQTT.
* Memahami penggunaan multiple topic.
* Memahami penggunaan wildcard topic (+ dan #).
* Menganalisis distribusi pesan pada sistem Smart Room Monitoring.

---

## Arsitektur Sistem

```text
+------------------+
| Publisher        |
| (Sensor Virtual) |
+------------------+
         |
         | Publish
         v
+------------------+
| Mosquitto Broker |
| Port 1883        |
+------------------+
         |
         | Subscribe
         v
+------------------+
| Subscriber       |
| Monitoring App   |
+------------------+
```

---

## Software yang Digunakan

| Software           | Versi          |
| ------------------ | -------------- |
| Python             | 3.13           |
| Mosquitto Broker   | 2.1.2          |
| paho-mqtt          | 2.1.0          |
| Visual Studio Code | Latest Version |

---

## Struktur Folder

```text
mqtt-smart-room-monitoring/

│
├── publisher.py
├── subscriber.py
│
├── publisher_qos.py
├── subscriber_qos.py
│
├── publisher_multi.py
├── subscriber_multi.py
│
├── subscriber_plus.py
│
├── publisher_hash.py
├── subscriber_hash.py
│
├── screenshots/
│   ├── scenario1.png
│   ├── scenario2.png
│   ├── scenario3.png
│   ├── scenario4.png
│   └── scenario5.png
│
└── README.md
```

---

# Instalasi

## 1. Install Python

Pastikan Python telah terpasang pada sistem.

Cek versi:

```bash
python --version
```

---

## 2. Install Mosquitto Broker

Download dan install Mosquitto Broker dari:

https://mosquitto.org/download/

Pastikan service Mosquitto berjalan pada port 1883.

---

## 3. Install Library MQTT

Jalankan perintah berikut:

```bash
pip install paho-mqtt
```

atau

```bash
python -m pip install paho-mqtt
```

Verifikasi instalasi:

```bash
python -m pip show paho-mqtt
```

---

# Menjalankan Program

Pastikan Mosquitto Broker sudah aktif sebelum menjalankan seluruh skenario.

---

# Skenario 1

## Komunikasi Dasar Publisher–Subscriber

### Menjalankan Subscriber

Buka terminal pertama:

```bash
python subscriber.py
```

Output:

```text
Subscriber aktif...
```

### Menjalankan Publisher

Buka terminal kedua:

```bash
python publisher.py
```

Contoh output:

```text
Mengirim suhu: 27
Mengirim suhu: 30
Mengirim suhu: 25
```

Subscriber akan menerima:

```text
Topic: room/temperature
Pesan: 27
```

---

# Skenario 2

## Pengujian Quality of Service (QoS)

### Menjalankan Subscriber

```bash
python subscriber_qos.py
```

### Menjalankan Publisher

```bash
python publisher_qos.py
```

Contoh hasil:

```text
Topic : room/qos
QoS   : 0
Data  : Pesan dengan QoS 0

Topic : room/qos
QoS   : 1
Data  : Pesan dengan QoS 1

Topic : room/qos
QoS   : 2
Data  : Pesan dengan QoS 2
```

### QoS yang Diuji

| QoS | Keterangan    |
| --- | ------------- |
| 0   | At Most Once  |
| 1   | At Least Once |
| 2   | Exactly Once  |

---

# Skenario 3

## Penggunaan Beberapa Topik

### Topik

```text
room/temperature
room/humidity
room/light
```

### Menjalankan Subscriber

```bash
python subscriber_multi.py
```

### Menjalankan Publisher

```bash
python publisher_multi.py
```

Contoh hasil:

```text
Topik: room/temperature | Data: 28
Topik: room/humidity | Data: 65
Topik: room/light | Data: 700
```

---

# Skenario 4

## Penggunaan Wildcard +

Subscriber melakukan subscribe menggunakan:

```text
room/+
```

### Menjalankan Subscriber

```bash
python subscriber_plus.py
```

### Menjalankan Publisher

```bash
python publisher_multi.py
```

Contoh hasil:

```text
Topik: room/temperature
Data : 29

Topik: room/humidity
Data : 72

Topik: room/light
Data : 800
```

Wildcard "+" memungkinkan subscriber menerima seluruh topik pada satu level hierarki.

---

# Skenario 5

## Penggunaan Wildcard

### Topik

```text
room1/temperature
room1/humidity

room2/temperature
room2/humidity
```

### Menjalankan Subscriber

```bash
python subscriber_hash.py
```

### Menjalankan Publisher

```bash
python publisher_hash.py
```

Contoh hasil:

```text
Topik : room1/temperature
Data  : 31

Topik : room1/humidity
Data  : 75
```

Wildcard "#" memungkinkan subscriber menerima seluruh sub-topik pada suatu cabang topik.

---

# Hasil Pengujian

| Skenario                              | Status   |
| ------------------------------------- | -------- |
| Komunikasi Dasar Publisher–Subscriber | Berhasil |
| QoS 0, 1, 2                           | Berhasil |
| Multiple Topic                        | Berhasil |
| Wildcard +                            | Berhasil |
| Wildcard #                            | Berhasil |

---

# Kesimpulan

Implementasi MQTT menggunakan Python dan Mosquitto Broker berhasil dilakukan pada studi kasus Smart Room Monitoring. Sistem berhasil menerapkan pola komunikasi publish-subscribe, pengiriman pesan dengan berbagai tingkat QoS, penggunaan beberapa topik, serta penggunaan wildcard topic (+ dan #). Hasil pengujian menunjukkan bahwa MQTT merupakan protokol yang ringan, fleksibel, dan sesuai untuk diterapkan pada sistem Cyber Physical System dan Internet of Things.

---

# Author

Nama : Muhammad Rasyid Hidayatullah

NIM : 235150307111037

Mata Kuliah : Cyber Physical System

Program Studi : Teknik Komputer

Universitas : Universitas Brawijaya

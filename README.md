# 🔐 ARP Poisoning Detection using Static ARP Tables

## 📘 Overview

This project demonstrates how ARP (Address Resolution Protocol) poisoning can redirect network traffic (conceptually) and provides a Python-based solution to **detect possible ARP spoofing attacks**.

Instead of performing the attack, this project focuses on:

* Understanding ARP poisoning
* Detecting suspicious ARP activity
* Preventing attacks using static ARP entries

---

## 🎯 Objective

* Study how ARP poisoning works in a network
* Detect abnormal ARP table behavior
* Implement a simple Python script for spoofing detection
* Suggest prevention using static ARP tables

---

## ⚙️ Requirements

* Python 3.x
* Windows / Linux OS
* Basic networking knowledge

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/arp-detection.git
cd arp-detection
```

2. Run the script:

```bash
python arp_detection.py
```

---

## 🔍 How Detection Works

The script:

* Reads the system ARP table using `arp -a`
* Parses IP and MAC address mappings
* Identifies suspicious behavior:

  * Same MAC address mapped to multiple IPs

### ⚠️ Example Suspicious Output

```
⚠️ Suspicious: MAC 00-14-22-01-23-45 mapped to multiple IPs: ['192.168.1.1', '192.168.1.5']
```

---

## 🛡️ Prevention Using Static ARP Tables

Static ARP entries prevent attackers from modifying ARP mappings.

### ➤ Windows

```bash
arp -s <IP Address> <MAC Address>
```

### ➤ Linux

```bash
sudo arp -s <IP Address> <MAC Address>
```

---

## 🧠 Concept: ARP Poisoning

* ARP maps IP → MAC addresses
* ARP has no authentication
* Attackers send fake ARP replies
* Traffic gets redirected through attacker

### 📌 Result:

Victim → Attacker → Router (Man-in-the-Middle)

---

## 📂 Project Structure

```
arp-detection/
│── arp_detection.py
│── README.md
```

---

## ⚠️ Ethical Consideration

This project is intended **only for educational purposes in a controlled lab environment**.
Unauthorized network attacks are illegal and punishable by law.

---

## ✅ Conclusion

ARP poisoning is a serious network vulnerability, but it can be effectively detected using ARP monitoring techniques and prevented using static ARP entries.

---

## 👨‍💻 Author

Your Name
(Replace with your GitHub profile link)

---

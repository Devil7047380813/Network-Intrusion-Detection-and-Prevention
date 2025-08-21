# Network-Intrusion-Detection-and-Prevention
A lightweight Intrusion Detection &amp; Prevention System (IDS/IPS) using Suricata and Python. Automatically detects attacker IP/MAC and blocks malicious traffic in real-time. Project demo for cyber defence
 🎯 Project Aim
- Detect and prevent network-based attacks on a system.  
- Provide real-time visibility of attacker IP, MAC address, and attack type.  
- Demonstrate IDS (detection only) and IPS (detection + blocking) modes. 

⚙️ Tech Stack
- **Python 3**  
- **Suricata IDS/IPS** (open-source network threat detection engine)  
- **Scapy** (packet analysis)  
- **joblib** (ML model integration placeholder for future expansion)  
- **iptables/ipset** (for auto-blocking attacker IPs)  

 How It Works
1. Suricata monitors network traffic and logs alerts into `eve.json`.  
2. Python script (`attacks_autoblock.py`) reads Suricata logs in real-time.  
3. On detecting an attack:
   - 🚨 Prints attacker details (Attack Type, Source IP, Destination IP, Protocol).  
   - 🔥 Auto-blocks attacker IP using `iptables` + `ipset`.  
4. Defends the system against repeated attacks in real-time.  


 How to Run the Project

 1️ Install Dependencies
Clone the repo and install Python libraries:
```bash
git clone https://github.com/Devil7047380813/Network-Intrusion-Detection-and-Prevention.git
cd Network-Intrusion-Detection-and-Prevention
pip install -r requirements.txt

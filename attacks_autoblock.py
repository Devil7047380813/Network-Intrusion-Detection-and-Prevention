#!/usr/bin/env python3
import json
import subprocess

# Path to Suricata EVE JSON log
EVE_LOG = "/var/log/suricata/eve.json"

def block_ip(ip):
    """
    Block the attacker IP using ipset + iptables.
    """
    try:
        subprocess.run(
            ["ipset", "add", "blacklist", ip],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        subprocess.run(
            ["iptables", "-A", "INPUT", "-m", "set", "--match-set", "blacklist", "src", "-j", "DROP"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        print(f"🔥 Blocked IP: {ip}")
    except Exception as e:
        print(f"[!] Failed to block {ip}: {e}")

def main():
    print("[*] Monitoring Suricata alerts for attacks... 🚨\n")

    try:
        with open(EVE_LOG, "r") as logfile:
            logfile.seek(0, 2)  # Go to end of file
            while True:
                line = logfile.readline()
                if not line:
                    continue

                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue

                # Only process alerts
                if event.get("event_type") == "alert":
                    src_ip = event.get("src_ip", "N/A")
                    dest_ip = event.get("dest_ip", "N/A")
                    proto = event.get("proto", "N/A")
                    alert_msg = event["alert"].get("signature", "Unknown Attack")

                    print("\n🚨 ATTACK DETECTED!")
                    print(f"   Attack Type   : {alert_msg}")
                    print(f"   Source IP     : {src_ip}")
                    print(f"   Destination IP: {dest_ip}")
                    print(f"   Protocol      : {proto}")

                    # Auto-block attacker
                    if src_ip != "N/A":
                        block_ip(src_ip)

    except FileNotFoundError:
        print(f"[!] Log file not found: {EVE_LOG}")
    except KeyboardInterrupt:
        print("\n[+] Stopping monitoring.")

if __name__ == "__main__":
    main()

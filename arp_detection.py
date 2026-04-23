import os
import re
import subprocess

# Function to get ARP table
def get_arp_table():
    try:
        output = subprocess.check_output("arp -a", shell=True).decode()
        return output
    except Exception as e:
        print("Error fetching ARP table:", e)
        return ""

# Function to parse ARP entries
def parse_arp(output):
    arp_entries = {}
    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([-\w]+)"

    for line in output.split("\n"):
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            mac = match.group(2)

            if mac in arp_entries:
                arp_entries[mac].append(ip)
            else:
                arp_entries[mac] = [ip]

    return arp_entries

# Function to detect suspicious entries
def detect_spoofing(arp_entries):
    print("\n🔍 Checking for ARP Spoofing...\n")
    suspicious = False

    for mac, ips in arp_entries.items():
        if len(ips) > 1:
            suspicious = True
            print(f"⚠️ Suspicious: MAC {mac} mapped to multiple IPs: {ips}")

    if not suspicious:
        print("✅ No ARP Spoofing detected.")

# Function to suggest static ARP
def suggest_static():
    print("\n🛡️ Suggested Prevention:")
    print("Use static ARP entries to prevent spoofing.\n")
    print("Windows:")
    print("  arp -s <IP> <MAC>")
    print("\nLinux:")
    print("  sudo arp -s <IP> <MAC>")

# Main
if __name__ == "__main__":
    print("=== ARP Spoofing Detection Tool ===")

    arp_output = get_arp_table()
    if arp_output:
        print("\n📡 Current ARP Table:\n")
        print(arp_output)

        entries = parse_arp(arp_output)
        detect_spoofing(entries)
        suggest_static()
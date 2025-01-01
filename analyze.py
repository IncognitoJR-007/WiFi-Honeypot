from scapy.all import sniff
import requests
from database import log_packet

# Fetch geolocation data
def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        location = data.get("loc", "0,0").split(",")
        city = data.get("city", "Unknown")
        country = data.get("country", "Unknown")
        return float(location[0]), float(location[1]), city, country
    except:
        return 0, 0, "Unknown", "Unknown"

# Packet handler
def packet_handler(packet):
    try:
        src_ip = packet[0][1].src
        dst_ip = packet[0][1].dst
        protocol = packet[0].proto
        length = len(packet)

        # Get geolocation
        latitude, longitude, city, country = get_location(src_ip)

        # Log packet details
        log_packet(src_ip, dst_ip, protocol, length, latitude, longitude, city, country)
    except:
        pass

print("Starting packet sniffing...")
sniff(prn=packet_handler)

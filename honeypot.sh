#!/bin/bash

echo "Setting up WiFi Honeypot..."
sudo apt update
sudo apt install hostapd dnsmasq -y

# Configure hostapd
cat <<EOT > /etc/hostapd/hostapd.conf
interface=wlan0
ssid=FakeWiFi
channel=6
EOT

sudo systemctl start hostapd
echo "Honeypot active. Monitoring connections..."

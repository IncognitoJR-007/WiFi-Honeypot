# WiFi Honeypot with Real-Time Location Tracking

This project creates a WiFi honeypot to monitor and analyze network traffic in real-time. It logs packet details, fetches geolocation data for connected devices, and visualizes them on an interactive map through a web dashboard.

## Features
- **Real-Time Packet Capture**: Analyze and log network packets using Scapy.
- **Device Geolocation**: Fetch device locations using [ipinfo.io](https://ipinfo.io).
- **Database Integration**: Log all activity into an SQLite database.
- **Interactive Dashboard**: Visualize data with Leaflet.js and Flask.
- **Packet Logs**: Maintain a detailed log of connections in `honeypot.log`.

---

## Installation

### Prerequisites
- Python 3.x installed
- Pip (Python package manager)
- Linux system with wireless network capabilities
- Git for cloning the repository

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/IncognitoJR-007/WiFi-Honeypot.git
   cd WiFi-Honeypot

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set Up the WiFi Honeypot**
   ```bash
   sudo bash honeypot.sh

4. **Start Packet Analysis**
   ```bash
   python analyze.py

5. **Run the Flask Server**
   ```bash
   python app.py

6. **Access the Dashboard Open http://127.0.0.1:5000 in your web browser.**

### Real-Time Location Tracking

The project uses https://ipinfo.io to fetch geolocation data for connected devices. This data is logged in the SQLite database and visualized on the dashboard using Leaflet.js.

#### Example Visualization
The `/logs` page displays:

• A table with packet details

• An interactive map with markers for device locations


## Technical Details

### Geolocation API

• Provider: https://ipinfo.io

• Integration: Implemented in `analyze.py`

### Database

• SQLite is used to store packet details.

• Fields include:

   • Source IP, Destination IP

   • Protocol, Packet Length
  
   • Latitude, Longitude, City, Country
  
### Packet Capture

• Library: Scapy

• Script: `analyze.py`

## Contributing

Feel free to submit issues or pull requests on the repository: https://github.com/IncognitoJR-007/WiFi-Honeypot

## License

• This project is licensed under the MIT License.

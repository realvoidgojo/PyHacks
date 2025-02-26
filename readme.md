# PyHacks

This PyHacks repository contains more networking related python scripts for linux system 

# Network Tools
A collection of Python scripts for various network tasks, including MAC address changing, network scanning, ARP spoofing, and ARP sniffing.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tools](#tools)
  - [MAC Changer](#mac-changer)
  - [Network Scanner](#network-scanner)
  - [ARP Spoofer](#arp-spoofer)
  - [ARP Sniffer](#arp-sniffer)
- [FAQs](#faqs)
- [Contributing](#contributing)

## Introduction
This repository provides a set of command-line tools for network manipulation and analysis. It includes tools for changing MAC addresses, scanning networks, spoofing ARP packets, and sniffing ARP traffic.

## Features
- Modular design for easy maintenance and extension.
- Command-line interface for easy usage.
- Supports multiple network tasks.

## Requirements
- Python 3.x
- Scapy library (`pip install scapy`)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/network-tools.git
   ```
2. Install required packages:
   ```
   pip install scapy
   ```

## Usage
Run the tool using the following command:
```
python3 cli.py --help
```
This will display the help menu for available commands.

## Tools

### MAC Changer
Changes the MAC address of a network interface.
```
python3 cli.py mac_changer -i wlan0 -m 11:22:33:44:55:66
```

### Network Scanner
Scans a network to discover devices.
```
python3 cli.py network_scanner -r 192.168.1.1/24
```

### ARP Spoofer
Spoofs ARP packets to manipulate network traffic.
```
python3 cli.py arp_spoofer -t 192.168.1.100 -s 192.168.1.1
```

### ARP Sniffer
Sniffs ARP packets to monitor network activity.
```
python3 cli.py arp_sniffer -i wlan0
```

## FAQs
- **Python Version**: Ensure you're using Python 3.
- **Scapy Installation**: Install Scapy using `pip install scapy`.
- **Root Privileges**: Some operations require root access.

## Contributing
Contributions are welcome! Please submit pull requests with detailed explanations of changes.

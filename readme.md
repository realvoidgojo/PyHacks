## PyHacks

This PyHacks repository contains more networking and hacking related python scripts for linux system

---
1. `mac_changer.py`
this programs helps to change your MAC address (MEDIA ACCESS CONTROL) for your devices using python in ` linux [only]`

- `prerequisites : python3`
- get interface name for the devices using `ifconfig`
- run this py script as root user , use this cmd  to get root privilege ` sudo su ` and specify interface and new mac address
`python3 mac_changer --interface wlan1 --mac 11:22:33:44:55:66`

```
shell > python3 mac_changer.py --help

python3 mac_changer --help
Usage: mac_changer.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Used to select Interface for changing MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        Used to select New MAC addresss

````
this scripts just run linux cmds in background for changing current mac address so this script works only on linux

[FAQ]
 if use python2 to run this script `subprocess.check_output()` and `subprocess.run()`is not defined in python2 , then install python3 `sudo apt install python3`
 subprocess.call() has been changed to subprocess.run() in python3
 ```
File "mac_changer.py", line 29, in get_mac_address
    ifconfig_result =  str(subprocess.check_output(["ifconfig",options.interface]),'ascii')

```
---
### Network Scanner
2.`network_scanner.py`
This Program helps to discover devices in your wifi network

- Connect the Target Wifi Network with your devices , then cmd
`ifconfig` and get the ip address (inet) eg: `192.168.1.10`

```py
python3 network_scanner  --range 192.168.1.1/24
```
This Program , Sends packets to `192.168.1.1` to `192.168.1.254`
Print the discovered Devices ip_address and MAC_address in that target network

[FAQs] if get `ImportError: No module named scapy.all` , then install scapy module 
```
pip install scapy
```
```
Usage: network_scanner.py [options]

Options:
  -h, --help            show this help message and exit
  -r RANGE, --range=RANGE
                        Use -r or --range to Scan Your Wifi Network
```

Network Scanning Using ARP

ARP Protocol is a protocol for mapping IP address to a physical machine that is recognised in the local network

ARP Illustration
- If A , B , C , D , ROUTER  is a network `192.168.43.1/24`
- A is Our machine , which says who has --range `192.168.43.1/24` IP this is ARP request , sends to devices in that network
- C Responds for that request as ARP Response  , like I have `192.168.43.7`  and My MAC address  : `00:11:22:33:44:45` for every other packet also

---
### ARP Spoofer
It's a type of attack in which a macilious actor sends false ARP message over a local network

##### Pre Exisitng ARP Spoofing Script,
Let ARP Spoofing Using `arpspoof` from `dsniff` tool
- First Scan The Local Network and discover Devices over that network , get target machine and router ip address
- Let assume Target be a windows machine , In cmd prompt , note mac address of router using `arp -a` cmd 
- Open 2 Terminal  , this required root privilege 
```
arpspoof -i wlan0 -t 192.168.0.143 192.168.0.1
arpspoof -i wlano0 -t 192.168.0.1 192.168.0.143
```


Note Mac Address of Router `arp -a` , Mac Address of Router was changed to Mac address of our machine.

**To run the script**
```
shell > python3 arp_spoofer.py --help
python3 arp_spoofer.py --help
Usage: arp_spoofer.py [options]

Options:
  -h, --help            show this help message and exit
  -t TARGET_IP , --target=TARGET_IP
                        Used to select Target Machine IP Address 
  -s SPOOF_IP , --spoof=SPOOF_IP
                        Used to select Spoof Machine IP Address (Router)
````

Spoofing Machine is Network Router Scan the network using `network_scanner.py` , find ip address , always router ip_address will be `XXX.XXX.X.1` it starts with 1
```py
python3 arp_spoofer.py -t 192.168.0.14 --s 192.168.0.1
``` 

---

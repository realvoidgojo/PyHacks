## PyHacks

This PyHacks repository contains more networking and hacking related python scripts 

---

1. mac_changer.py

this programs helps to change your MAC address (MEDIA ACCESS CONTROL) for your devices using python in `linux [only]`

`prerequisites : python3`

get interface name for the devices using `ifconfig`

run this py script as root user , use this cmd  to get root privilege ` sudo su `
```
python3 mac_changer --interface wlan1 --mac 11:22:33:44:55:66

```

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

---





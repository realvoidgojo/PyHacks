import scapy.all as scapy

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    src_dest = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast = src_dest/arp_request
    answered_list = scapy.srp(broadcast, timeout=1, verbose=False)[0]
    
    result_list = []
    for answer in answered_list:
        result_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        result_list.append(result_dict)

    print("IP \t\t\t MAC ADDRESS \n-------------------------------------------")
    for result in result_list:
        print(result["ip"] + "\t\t" + result["mac"])

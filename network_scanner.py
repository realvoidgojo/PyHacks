import scapy.all as scapy
import optparse 

# Implementing CLI Parsing
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r" , "--range" , dest="range" , help="Use -r or --range to Scan Your Wifi Network")

    options = parser.parse_args()[0]
    
    # Excecption Handling for args
    if not options.range:
        parser.error("Please specify an range !, use --help or -h to get more info.")
    else:
        return options


# Discovring Devices in Wifi Network
def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    src_dest = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast = src_dest/arp_request
    answered_list = scapy.srp(broadcast,timeout=1,verbose=False)[0]
   
    result_list = []
    for answer in answered_list:
        result_dict = { "ip" : answer[1].psrc , "mac" : answer[1].hwsrc}
        result_list.append(result_dict)

    return result_list

# Displaying Answered Packets with details
def print_result(result_list):
    print("IP \t\t\t MAC ADDRESS \n-------------------------------------------")
    for result in result_list:
        print(result["ip"] + "\t\t" + result["mac"])


options = get_arguments()
result_dict = scan(options.range)
print_result(result_dict)
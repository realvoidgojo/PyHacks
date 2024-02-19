import subprocess
from optparse import OptionParser
import re

# Implementing CLI Parsing
def get_Options():
    parser = OptionParser()
    parser.add_option("-i" , "--interface" , dest="interface" , help="Used to select Interface for changing MAC address")
    parser.add_option("-m" , "--mac" , dest= "new_mac" , help="Used to select New MAC address")
    ( options , arguments )  = parser.parse_args()
    
    # Excecption Handling for args
    if not options.interface:
        parser.error("Please specify an interface!, use --help or -h to get more info.")
    elif not options.new_mac:
        parser.error("Please specify an MAC address!, use --help or -h to get more info.")
    else:
        return options

# Changing MAC Address 
def change_Mac(interface,new_mac):
    print("\n[+] Changing MAC address :\u00A0\u00A0" + interface + "\u00A0To\u00A0\u00A0"+ new_mac + "\n" )
    subprocess.run(["ifconfig",interface,"down"])  
    subprocess.run(["ifconfig",interface,"hw","ether",new_mac]) 
    subprocess.run(["ifconfig",interface,"up"])

# Getting MAC Address
def get_mac_address(interface):
    ifconfig_result =  str(subprocess.check_output(["ifconfig",options.interface]),'ascii')
    filter_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
    if filter_result:
        return filter_result.group(0)
    else:
        print("MAC Address Not Found !!.")


options = get_Options()
mac_address_filter_result = get_mac_address(options.interface)
print("-----------------------------------------------------------------------------------------")
print("Current MAC address =",str(mac_address_filter_result))
change_Mac(options.interface,options.new_mac) 
mac_address_filter_result = get_mac_address(options.interface)

if mac_address_filter_result == get_mac_address(options.interface):
    print("MAC address changed To :",mac_address_filter_result)
else:
    print("MAC address is not changed!")
print("-----------------------------------------------------------------------------------------")








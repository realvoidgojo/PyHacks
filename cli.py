import argparse
from source.mac_changer import change_mac
from source.network_scanner import scan_network
from source.arp_spoofer import spoof_arp
from source.arp_sniffer import sniff_arp

def main():
    parser = argparse.ArgumentParser(description='Network Tools CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Sub-parser for mac_changer
    mac_changer_parser = subparsers.add_parser('mac_changer')
    mac_changer_parser.add_argument('-i', '--interface', required=True, help='Interface to change MAC')
    mac_changer_parser.add_argument('-m', '--mac', required=True, help='New MAC address')

    # Sub-parser for network_scanner
    network_scanner_parser = subparsers.add_parser('network_scanner')
    network_scanner_parser.add_argument('-r', '--range', required=True, help='IP range to scan')

    # Sub-parser for arp_spoofer
    arp_spoofer_parser = subparsers.add_parser('arp_spoofer')
    arp_spoofer_parser.add_argument('-t', '--target', required=True, help='Target IP')
    arp_spoofer_parser.add_argument('-s', '--spoof', required=True, help='Spoof IP')

    # Sub-parser for arp_sniffer
    arp_sniffer_parser = subparsers.add_parser('arp_sniffer')
    arp_sniffer_parser.add_argument('-i', '--interface', required=True, help='Interface to sniff')

    args = parser.parse_args()
    if args.command == 'mac_changer':
        change_mac(args.interface, args.mac)
    elif args.command == 'network_scanner':
        scan_network(args.range)
    elif args.command == 'arp_spoofer':
        spoof_arp(args.target, args.spoof)
    elif args.command == 'arp_sniffer':
        sniff_arp(args.interface)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

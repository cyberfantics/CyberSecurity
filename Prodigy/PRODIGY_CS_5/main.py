import socket
import struct
import textwrap
from colorama import Fore, Style
import colorama
import os
import time
import platform

# Initialize colorama
colorama.init(autoreset=True)

# Function to clear screen
def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

# Initilize logo
logo = f'''
{Fore.GREEN} ____        _  __ _ _   _            _
{Fore.RED}/ ___|  __ _| |/ _(_) | | | __ _  ___| | _____ _ __
{Fore.CYAN}\___ \ / _` | | |_| | |_| |/ _` |/ __| |/ / _ \ '__|
{Fore.YELLOW} ___) | (_| | |  _| |  _  | (_| | (__|   <  __/ |
{Fore.BLUE}|____/ \__,_|_|_| |_|_| |_|\__,_|\___|_|\_\___|_|
{Fore.MAGENTA}
'''

# Function to display logo with delay
def display_logo_with_delay(logo_text, delay=0.1):
    clear_screen()
    for line in logo_text.split('\n'):
        print(line)
        time.sleep(delay)

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\n' + Fore.YELLOW + 'Ethernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))

        # IPv4
        if eth_proto == 8:
            version, header_length, ttl, proto, src, src_host, target, target_host, data = ipv4_packet(data)
            print(Fore.CYAN + '\tIPv4 Packet:')
            print('\tVersion: {}, Header Length: {}, TTL: {}'.format(version, header_length, ttl))
            print('\tProtocol: {}, Source: {} ({}) , Target: {} ({})'.format(proto, src, src_host, target, target_host))

            # TCP
            if proto == 6:
                src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = tcp_segment(data)
                print(Fore.GREEN + '\tTCP Segment:')
                print('\tSource Port: {}, Destination Port: {}'.format(src_port, dest_port))
                print('\tSequence: {}, Acknowledgement: {}'.format(sequence, acknowledgement))
                print('\tFlags:')
                print('\tURG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN:{}'.format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))

# Unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

# Return properly formatted MAC address (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

# Unpack IPv4 packet
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    src = ipv4(src)
    target = ipv4(target)
    try:
        src_host = socket.gethostbyaddr(src)[0]
    except socket.herror:
        src_host = 'Unknown'
    try:
        target_host = socket.gethostbyaddr(target)[0]
    except socket.herror:
        target_host = 'Unknown'
    return version, header_length, ttl, proto, src, src_host, target, target_host, data[header_length:]

# Returns properly formatted IPv4 address
def ipv4(addr):
    return '.'.join(map(str, addr))

# Unpack TCP segment
def tcp_segment(data):
    (src_port, dest_port, sequence, acknowledgement, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

if __name__ == "__main__":
    display_logo_with_delay(logo)
    print(Style.BRIGHT + Fore.MAGENTA + "\n\n\t[+]" + Fore.RED + " Welcome to Advanced Packet Sniffer!")
    input()
    main()

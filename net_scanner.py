import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-r","--range",dest="ip_address",help="enter ip address")

    (user_inputs,arguments) = parse_object.parse_args()

    if not user_inputs.ip_address:
        print("enter ip address")

    return user_inputs

def scan_network(p_ip_address):
    arp_request_packet = scapy.ARP(pdst=p_ip_address)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet

    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()

user_ip = get_user_input()
scan_network(user_ip.ip_address)
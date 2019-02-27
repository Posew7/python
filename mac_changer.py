import subprocess
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="change to interface")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")
    return parse_object.parse_args()

def change_mac_address(p_interface,p_mac_address):
    subprocess.call(["ifconfig",p_interface,"down"])
    subprocess.call(["ifconfig",p_interface,"hw","ether",p_mac_address])
    subprocess.call(["ifconfig",p_interface,"up"])

def control_new_mac(p_interface):
    ifconfig = subprocess.check_output(["ifconfig",p_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("mac changer started !")
(user_inputs,arguments) = get_user_input()
change_mac_address(user_inputs.interface,user_inputs.mac_address)
finalized_mac = control_new_mac(str(user_inputs.interface))

if finalized_mac == user_inputs.mac_address:
    print("success\n\n")
    subprocess.call(["ifconfig",user_inputs.interface])
else:
    print("error")
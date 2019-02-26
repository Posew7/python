import subprocess
import optparse

def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac",help="new mac adress")

    return parse_object.parse_args()

def mac_changer(interface,mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

    subprocess.call(["ifconfig",interface])

(user_inputs,arguments) = user_input()
mac_changer(user_inputs.interface, user_inputs.mac)
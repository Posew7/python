import subprocess

interface = "wlan0"
mac = "00:11:22:11:33:22"

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])

subprocess.call(["ifconfig",interface])
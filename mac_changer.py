#!/usr/bin/env python3

import subprocess #For implementing OS commands
import optparse #Parsing User argumetns
import time
def user_input():

    Parser = optparse.OptionParser()
    Parser.add_option("-i","--interface", dest="Interface", help="This is used for assigning Interface")
    Parser.add_option("-m","--mac", dest="Mac_Address",help="For assgining MAC Address")
    (options,args) = Parser.parse_args()
    if not options.Interface and not options.Mac_Address:
        Parser.error("Please Specify both the interface and MAC Address, use --help for more info")
    elif not options.Mac_Address:
        Parser.error("Please Specify the MAC Address, use --help for more info")
    elif not options.Interface or not options.Mac_Address:
        Parser.error("Please Specify the interface, use --help for more info")
    else:
        pass

    interface = options.Interface
    mac = options.Mac_Address
    change_mac(interface,mac)


def change_mac(interface,mac):

    Current_MAC = subprocess.check_output("ip link show eth0 | awk \'/ether/ {print $2}\'",shell=True)
    print(f"[+] Changing MAC Address from {Current_MAC.decode()}")
    time.sleep(1.5)
    print(f"[+] Your new MAC Address is {mac} at Interface {interface}")
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

user_input()
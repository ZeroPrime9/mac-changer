#!/usr/bin/env python3
from colorama import Fore
import subprocess #For implementing OS commands
import optparse #Parsing User argumetns
import time
import re

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

    mac_address = ""
    try:
        print(Fore.RED)
        ifconfig_result = subprocess.check_output(["ifconfig",interface]).decode()
        mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    except:
        print(Fore.RED + "[+] An error has occured")
        exit()
    
    if mac_address:
        
        print(Fore.GREEN + "[+] Changing MAC Address from:", Fore.YELLOW + f"{mac_address.group(0)}")
        time.sleep(1.5)
        print(Fore.GREEN + "[+] Your new MAC Address is", Fore.YELLOW + f"{mac}", Fore.GREEN + "at Interface", Fore.YELLOW + f"{interface}")
        print(Fore.RED)
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",mac])
        subprocess.call(["ifconfig",interface,"up"])
        

    else:
        
        print(Fore.RED + "[-] Your Current Interface", Fore.YELLOW + f"{interface.upper()}", Fore.RED + "does not have a MAC Address")
        print(Fore.RED + "[-] MAC Address is not changed")
        

user_input()
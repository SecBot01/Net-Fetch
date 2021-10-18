#!/usr/bin/env python
# Network scan using scapy.
#
# This python script using scapy module will scan your network and returns all the clients
# within the network.
#
# this script should run with python 2.7 or python 3. any way you need to install dependencies
# for curresponding version
#
# you need two dependencies to run:
#   1.scapy
#   2.colorama
#
#          code contributed by: @nibrasmuhamed and @muhammednahil on Github
#                      
#

import scapy.all as scapy
import subprocess
import os

def main():
    
    

    # gateway = str(subprocess.call("ip route show | grep -i 'default via'| awk '{print $3 }'", shell=True))
    # gateway_ip = str((gateway+"/24"))
    gateway_ip = raw_input("Enter your gateway ip with subnet (eg:192.168.1.1/24) \n\ntip: gateway ip can be obtained by running 'route -n' command\n\nIP >> ")
    
    def scan(ip):
        arp_req = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_req_broadcast = broadcast/arp_req
        answered_lst = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
        client_list = []

        for packet in answered_lst:
            client_dic = {"ip": packet[1].psrc, "mac": packet[1].hwsrc}
            client_list.append(client_dic)

        return client_list


    def print_all(result_list):
        print("IP Address\t\t\tMac Adress\n---------------------------------------------------")
        for client in result_list:
            print(client["ip"] + "\t\t" + client["mac"])

    user_choice = input("1)pyScanner\n2)nmap\n\nChoice:")

    if user_choice == 1:
        scan_res = scan(gateway_ip)
        print_all(scan_res)
    elif user_choice == 2:
        # result = subprocess.check_output(args, text)
        os.system('sudo nmap -sn '+ gateway_ip)

if __name__ == "__main__":
   main()
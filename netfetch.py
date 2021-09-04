import sys
import assets.netscan as scan

def target_f():
	# target_ip = raw_input("enter target ip address") 
	print("1.Code Injector")
	print("2.DNS spoofer")
	print("3.File Interceptor")
	print("4.Packet Sniffer")


user_input=0
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

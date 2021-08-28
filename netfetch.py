import sys
import os

# if not os.getuid() == 0:
# 	sys.exit("Net-Fetch must be run as root(-_-)")

exit_msg="shutting down(-_-)"

def target_f():
	# target_ip = raw_input("enter target ip address") 
	print("1.Code Injector")
	print("2.DNS spoofer")
	print("3.File Interceptor")
	print("4.Packet Sniffer")

h_input=0
while h_input != "exit" : 
		print("Please type 'help' for more info")
		h_input = raw_input(">> ")
		if h_input=="help" : 
				print("help")
				print("exit")
				print("scan")
				print("target")
		elif h_input== 'target':
			target_f()
		elif h_input == 'exit':
			print(exit_msg)
			sys.exit(0)

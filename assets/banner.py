#!/usr/bin/python
# -*- coding: utf-8 -*-


import random


banner1 = '''



███╗░░██╗███████╗████████╗░░░░░░███████╗███████╗████████╗░█████╗░██╗░░██╗
████╗░██║██╔════╝╚══██╔══╝░░░░░░██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░██║
██╔██╗██║█████╗░░░░░██║░░░█████╗█████╗░░█████╗░░░░░██║░░░██║░░╚═╝███████║
██║╚████║██╔══╝░░░░░██║░░░╚════╝██╔══╝░░██╔══╝░░░░░██║░░░██║░░██╗██╔══██║
██║░╚███║███████╗░░░██║░░░░░░░░░██║░░░░░███████╗░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░░░░░░░╚═╝░░░░░╚══════╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

							The Third Guy

							

			for more information visit: github.com/secbot01
			  project by @nibrasmuhamed and @muhammednahil

'''

banner2 = '''


			┏━┓╋┏┓╋╋┏┓╋╋┏━━━┓╋╋┏┓╋╋╋┏┓
			┃┃┗┓┃┃╋┏┛┗┓╋┃┏━━┛╋┏┛┗┓╋╋┃┃
			┃┏┓┗┛┣━┻┓┏┛╋┃┗━━┳━┻┓┏╋━━┫┗━┓
			┃┃┗┓┃┃┃━┫┣━━┫┏━━┫┃━┫┃┃┏━┫┏┓┃
			┃┃╋┃┃┃┃━┫┗┳━┫┃╋╋┃┃━┫┗┫┗━┫┃┃┃
			┗┛╋┗━┻━━┻━┛╋┗┛╋╋┗━━┻━┻━━┻┛┗┛

					The Third Guy



	for more information visit: github.com/secbot01
 	 project by @nibrasmuhamed and @muhammednahil


''' 


banner3 = '''


		▒█▄░▒█ █▀▀ ▀▀█▀▀ ░░ ▒█▀▀▀ █▀▀ ▀▀█▀▀ █▀▀ █░░█ 
		▒█▒█▒█ █▀▀ ░░█░░ ▀▀ ▒█▀▀▀ █▀▀ ░░█░░ █░░ █▀▀█ 
		▒█░░▀█ ▀▀▀ ░░▀░░ ░░ ▒█░░░ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░▀

						The Third Guy


		for more information visit: github.com/secbot01
		  project by @nibrasmuhamed and @muhammednahil

'''


def showheader():
	headers = [banner1, banner2, banner3]
	return random.choice(headers)

def usage_warning():
	print("\t\tthis tool is for educational and testing purpose.")
	print("\t\tdevelopers are not responsible for any illegal uses.")
	print("\t\t\t#RespectOthersPrivacy")

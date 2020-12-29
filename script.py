#! /usr/bin/python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
	import sys
	import socket
	import requests

	url = sys.argv[1]
	wordlist = sys.argv[2]

	print bcolors.OKCYAN + "[*] Checking URL... " + bcolors.ENDC,
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		status = s.connect_ex((url, 80))
		s.close()
		if status == 0:
			print '[DONE]'
			pass
		else:
			print '[FAIL]'
			print bcolors.WARNING +'[!] Error: Cannot Reach URL %s\n' %(url) + bcolors.ENDC 
			sys.exit(1)
	except socket.error:
		print '[FAIL]'
		print bcolors.WARNING + '[!] Error: Cannot Reach URL: %s\n' %(url) + bcolors.ENDC
		sys.exit(1)

	print bcolors.OKCYAN +'[*] Trying The Wordlist... ' + bcolors.ENDC,
	try:
		with open(wordlist) as file:
			to_check = file.read().strip().split('\n')
		print '[DONE]'
		print bcolors.OKCYAN + '[*] Total Paths to Check: %s' %(str(len(to_check))) + bcolors.ENDC
	except IOError:
		print '[FAIL]'
		print bcolors.WARNING + '[!] Error: Failed to Read Specified File\n' + bcolors.ENDC
		sys.exit(1)
	
	def checkpath(path):
		try:
			response = requests.get('http://' + url + '/' + path).status_code
		except Exception:
			print bcolors.WARNING + '[!] Error: An Unexpected Error Occured' + bcolors.ENDC
			sys.exit(1)
		if response != 500 :
			print ''
			print bcolors.OKGREEN + '[*] Full Path : %s/%s (%d)' %(url,path,response) + bcolors.ENDC
	
	print bcolors.HEADER + '\n[*] Beginning Scan...\n' + bcolors.ENDC
	print bcolors.OKGREEN + 'Printing The Directories Found:'+ bcolors.ENDC
	for i in range(len(to_check)):
		checkpath(to_check[i])
	print bcolors.HEADER + '\n[*] Scan Complete!' + bcolors.ENDC
except KeyboardInterrupt:
	print bcolors.WARNING + '\n[!] Error: User Interrupted Scan' + bcolors.ENDC
	sys.exit(1)
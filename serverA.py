import socket
import os
import select
PORT = 6996
HOST = '192.168.42.144'
def main():
	print("--STARTING--")
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind((HOST,PORT))
	sock.listen(2)
	print("--LISTENING--")
	(s,clientAddr) = sock.accept()
	print(f"[NEW CONNECTION from ]{clientAddr}.")
	with s:
		while True:
			data = s.recv(1024).decode('ascii')
			if data:
				print(data)


if __name__=="__main__":
	main()

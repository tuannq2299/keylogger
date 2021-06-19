import socket
import os
import select
PORT = 9669
HOST = '127.0.0.1'
def main():
	print("--STARTING--")
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind((HOST,PORT))
	sock.listen(2)
	print("--LISTENING--")
	while True:
		(s,clientAddr) = sock.accept()
		print(f"[NEW CONNECTION from ]{clientAddr}.")
		data = s.recv(1024).decode('ascii')
		if data:
			print(data)
		sock.close()


if __name__=="__main__":
	main()

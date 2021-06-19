import socket
import os
import select
PORT = 9999
HOST = '127.0.0.1'
DATA_PATH = 'serverData'
SIZE = 4096
read_list = []
write_list = []
cmd_list = {}
msg_list = {}
def main():
	print("--STARTING--")
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	read_list.append(sock)
	sock.bind((HOST,PORT))
	sock.listen(2)
	print("--LISTENING--")
	while True:
		read_sockets, write_sockets, error_sockets = select.select(read_list ,[], [],1)
		# print(read_sockets)
		for s in read_sockets:
			if s is sock:
				(clientSock,clientAddr) = s.accept()
				read_list.append(clientSock)
				print(f"[NEW CONNECTION from ]{clientAddr}.")
				# clientSock.send("tuannq@Welcome to server".encode('ascii'))
				# handle(clientSock, clientAddr)
			else:
				try:
					data = s.recv(SIZE).decode('ascii')
					# print(data)
					if data:
						print(data)
					else:
						if s in read_list:
							read_list.remove(s)
				except:
					print(f"[DISCONNECTED] {clientAddr}")
					sock.close()
	sock.close()


if __name__=="__main__":
	main()

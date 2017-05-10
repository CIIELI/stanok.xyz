#!c:\Python\Python36-32\python.exe

from socket import *
from datetime import datetime

FILENAME = 'text_files\data.txt'

host = '0.0.0.0'
port = 21
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(10)
	
while 1:
	print('wait connection...')
	conn, addr = tcp_socket.accept()
	print('client addr: ', addr)
	data = conn.recv(1024)

	with open(FILENAME, 'w') as f:
		f.write(data.decode('utf-8'))

	data = bytes.decode(data)
	print(data)
	if data == '1':
		conn.send(b'        Message delivered! (The machine works)         ')
	elif data == '0':
		conn.send(b'  Message delivered! (The machine does not work)  ' )
	elif data == '01':
		conn.send(b'Message delivered! (The machine is being repaired)')
	conn.close()

tcp_socket.close()
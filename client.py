from tkinter import *
from tkinter.filedialog import *
from socket import *
import sys
from datetime import datetime

def on_work():
	now = datetime.today()
	print('on_work')
	host = 'localhost'
	port = 21
	addr = (host, port)
	tcp_socket = socket(AF_INET, SOCK_STREAM)
	tcp_socket.connect(addr)
	data_out = '1'
	if not data_out:
		tcp_socket.close()
		sys.exit(1)
	#encode - перекодирует введенные данные в байты, decode - обратно
	data_out = str.encode(data_out)
	tcp_socket.send(data_out)
	data_in = tcp_socket.recv(1024)
	data = bytes.decode(data_in)
	print(data)
	lab_3 = Label(root, text=data)
	lab_3.grid(row=2, column=1)
	date_time()
	
	sn = data + str(now)
	my_file = open('text_files\some.txt', 'a')
	my_file.write(sn + '\n')
	my_file.close()
	
	tcp_socket.close()
	
def under_repair():
	now = datetime.today()
	print('under_repair')
	host = 'localhost'
	port = 21
	addr = (host, port)
	tcp_socket = socket(AF_INET, SOCK_STREAM)
	tcp_socket.connect(addr)
	data_out = '01'
	if not data_out:
		tcp_socket.close()
		sys.exit(1)
	#encode - перекодирует введенные данные в байты, decode - обратно
	data_out = str.encode(data_out)
	tcp_socket.send(data_out)
	data_in = tcp_socket.recv(1024)
	data = bytes.decode(data_in)
	print(data)
	lab_3 = Label(root, text=data)
	lab_3.grid(row=2, column=1)
	date_time()
	
	sn = data + str(now)
	my_file = open('text_files\some.txt', 'a')
	my_file.write(sn + '\n')
	my_file.close()
	
	tcp_socket.close()
	
def off_work():
	now = datetime.today()
	print('off_work')
	host = 'localhost'
	port = 21
	addr = (host, port)
	tcp_socket = socket(AF_INET, SOCK_STREAM)
	tcp_socket.connect(addr)
	data_out = '0'
	if not data_out:
		tcp_socket.close()
		sys.exit(1)
	#encode - перекодирует введенные данные в байты, decode - обратно
	data_out = str.encode(data_out)
	tcp_socket.send(data_out)
	data_in = tcp_socket.recv(1024)
	data = bytes.decode(data_in)
	print(data)
	lab_3 = Label(root, text=data)
	lab_3.grid(row=2, column=1)
	date_time()

	sn = data + str(now)
	my_file = open('text_files\some.txt', 'a')
	my_file.write(sn + '\n')
	my_file.close()
	
	tcp_socket.close()	
	
def date_time():
	now = datetime.today()
	lab_5 = Label(root, text=now)
	lab_5.grid(row=3, column=1)

data = '...'
root = Tk()
root.title('Кнопка вызова')
lab_01 = Label(root, text='TRUMPF_3030', font=('Helvetica', 20))
lab_01.grid(row=0, column=0)
button_1 = Button(root, text='Станок работает', command=on_work)
button_1.grid(row=1, column=0, stick=W)
button_2 = Button(root, text='Станок ремонтируется', command=under_repair)
button_2.grid(row=1, column=1)
button_3 = Button(root, text='Станок не работает', command=off_work)
button_3.grid(row=1, column=2)
lab_2 = Label(root, text='Отчет:')
lab_2.grid(row=2, column=0)
lab_3 = Label(root, text=data)
lab_3.grid(row=2, column=1)
lab_4 = Label(root, text='Дата/Время:')
lab_4.grid(row=3, column=0)

root.mainloop()
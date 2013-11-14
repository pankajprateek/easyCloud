import socket
import select

#make a socket
def connect_server():
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('', 80))
	return s;

#def connect_host(server_con, iden):
#	server_con.send('connect'+iden)
	
def send(connection,strg):
	connection.send(strg)
	return True			#if successful

def disconnect_server(connection):
	connection.close()

def receive(connection):
	possible_readers, [],[] = select.select([connection],[],[],0)
	if possible_readers==[connection]:
		data = connection.recv(1024)
		if len(data)!=0:
			return data
		else:
			return -1
	else:
		return None

def receive_blocking(connection):
	return connection.recv(1024)

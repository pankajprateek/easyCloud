import select
import socket

#server binds itself to some socket and returns the socket it binds itself
def setup_server():
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((socket.gethostname(), 80))
	s.listen(5)
	return s;

#test for any incoming connection requests and connect to them otherwise return None
def check_for_requests_and_connect(sock):
	possible_readers, [],[] = select.select([sock],[],[],0)
	if possible_readers==[sock]:
		print 'connection request received'
		connection, addr = sock.accept()
		print 'accepted in link layer'
		return connection
	else:
		return None
		
#reads data from client. Returns None if data not available. Returns -1 if client has already disconnected
def receive(server_sock, client):
	possible_readers, [],[] = select.select([client],[],[],0)
	if possible_readers==[client]:
		data=client.recv(1024)
		if len(data)!=0:
		 	return data
		else:
			return -1  #connection is closed by host
	else:
		return None
	

def send(server_sock, client, data):
	client.send(data)
	return 1
	
def receive_blocking(server_sock,client):
	return client.recv(1024)
			

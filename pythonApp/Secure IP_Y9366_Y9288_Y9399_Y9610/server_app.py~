# File: server.py

from Tkinter import *
from aes_server import *

class App:
	

	def __init__(self, master):
			 
		self.server_setup=False
		self.server_sock=None
		self.client=None
		frame = Frame(master)
		frame.pack()
	
		#textfr=Frame(frame)

		self.text=Text(frame,height=10,width=50,background='white')
		self.text.pack()

		# put a scroll bar in the frame

		#scroll = Scrollbar(textfr)
		#self.text.configure(yscrollcommand=scroll.set)
		#scroll.pack(side=RIGHT,fill=Y)

		self.button_connect = Button(frame, text="Setup Server", fg="black", command=self.setup)
		self.button_connect.pack(side=LEFT)
		
		self.entry = Entry(frame,width=50)
		self.entry.pack()
		
		self.button_send = Button(frame, text="Send", command=self.send_data)
		self.button_send.pack(side=LEFT)
		
		
		
		#self.button_receive = Button(frame, text="Send", command=self.receive_data)
		#self.button_receive.pack(side=LEFT)

	def setup(self):
	 	if self.server_setup==False:
			self.server_sock=setup_server()
			self.text.insert(END,'Server has been setup and bound to port: '+str(self.server_sock) + '\n' )
			self.server_setup=True			
		else:
			self.text.insert(END,"Server already in place.\n")
		
	def send_data(self):
		strg=self.entry.get()
		if len(strg)!=0:
			data = send_string(self.server_sock, self.client, strg)    #will do AES and send
			self.entry.delete(0, END)
			self.text.insert(END,"You: "+strg+'\n')		

	

root=Tk()
root.title('Chat Server')



app = App(root)

def loop():
	#print 'hurray'
	if app.client==None and app.server_sock!=None:  #server has been binded to host but not connected to any client
		#print 'checking for clients'
		app.client=check_for_requests_and_connect_network(app.server_sock)
		if app.client!=None:		
			app.text.insert(END, 'Connection made to host: '+str(app.client) +"\n" )
		#print 'client made'
	if app.client!=None:    #server has connected to server
		data=receive_string(app.server_sock, app.client)      #receive_string is None
		
		if data!=None:
			#print 'byebaye'
			app.text.insert(END,"Client: "+data+'\n')
		elif data==-1:
			app.text.insert(END,"Client has closed the connection.\n")
			app.server_setup=False
			app.server_sock=None
			app.client=None
			

	root.after(500,loop)
	 

root.title('Chat Server')

root.after(100, loop)

root.mainloop()


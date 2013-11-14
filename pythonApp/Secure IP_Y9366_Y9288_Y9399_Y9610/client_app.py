# File: client.py

from Tkinter import *
from aes_client import *

class App:
	

	def __init__(self, master):

		self.connection=None

		frame = Frame(master)
		frame.pack()

		#textfr=Frame(frame)

		self.text=Text(frame,height=10,width=50,background='white')
		self.text.pack()

		# put a scroll bar in the frame

		#scroll = Scrollbar(textfr)
		#self.text.configure(yscrollcommand=scroll.set)
		#scroll.pack(side=RIGHT,fill=Y)

		self.entry = Entry(frame,width=50)
		self.entry.pack()

		self.button_connect = Button(frame, text="Connect", fg="black", command=self.connect)
		self.button_connect.pack(side=LEFT)

		self.button_send = Button(frame, text="Send", command=self.send_data)
		self.button_send.pack(side=LEFT)
			
	

	def connect(self):			
		self.text.insert(END,"Connecting to server and exchanging key...\n")
		if self.connection!=None:
			self.text.insert(END,"Error: Connection already established.")
		else:
			self.connection=establish_connection()   #establish connection and diffie hellman key-exchange
			self.text.insert(END,"Connection established with server. :D\n ")
		
		
		
		#write here code to connect to the server and do the authentication
		#diffie hellman key exchange
		#initialisation vector
	def send_data(self):
		strg=self.entry.get()
		if len(strg)!=0:
			send_string(self.connection, strg)    #will do AES and send
			self.entry.delete(0, END)
			self.text.insert(END,"You: "+strg+"\n")		
	
	
root=Tk()


app = App(root)


def loop():
	if app.connection!=None:
		data=receive_string(app.connection)
		if data!=None and data!=-1:
			app.text.insert(END,"Server: "+data+"\n")
	root.after(100, loop)
	 
root.title('Chat Client')

root.after(100, loop)

root.mainloop()


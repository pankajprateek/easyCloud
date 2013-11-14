from Tkinter import *
from easyCloud import *

class App:
	def __init__(self,master):
		self.easyCloud = easyCloud()
		self.log = None
		frame = Frame(master)
		frame.pack()
	
		#textfr=Frame(frame)

		self.dropbox_button = Button(frame, text = "Dropbox", fg = "black", command = self.authenticate_dropbox)
		self.dropbox_button.pack(side=LEFT, padx=10, pady=10)
		self.googleDrive_button = Button(frame, text = "Google Drive", fg = "black", command = self.authenticate_googleDrive)
		self.googleDrive_button.pack(side=LEFT, padx=10, pady=10)
		self.text=Text(frame,height=10,width=50,background='white')
		self.text.pack()

		# put a scroll bar in the frame

		#scroll = Scrollbar(textfr)
		#self.text.configure(yscrollcommand=scroll.set)
		#scroll.pack(side=RIGHT,fill=Y)
		
		
		self.entry = Entry(frame,width=50)
		self.entry.pack()
		
		self.submit_button = Button(frame, text = "Submit", fg = "black", command = self.submit_token)
		self.submit_button.pack(side=LEFT, padx=10, pady=10)
		
		self.location_var = StringVar(frame)
		self.location_var.set('Split')
		self.location_choices = ['Split', 'All', 'Only To Dropbox', 'Only to Google Drive', 'Only To SkyDrive']
		self.location_option = OptionMenu(frame, self.location_var, *(self.location_choices))
		self.location_option.pack(side='left', padx=10, pady=10)
		
		self.button_location = Button(frame, text = "Set", fg = "black", command = self.set_upload_location)
		self.button_location.pack(side=LEFT, padx=10, pady=10)
		
		self.sync_button = Button(frame, text = "Sync", fg = "black", command = self.sync)
		self.sync_button.pack(side=LEFT, padx=10, pady=10)
		#self.button_send = Button(frame, text="Send", command=self.send_data)
		#self.button_send.pack(side=LEFT)
		#self.button_receive = Button(frame, text="Send", command=self.receive_data)
		#self.button_receive.pack(side=LEFT)
		
	def set_upload_location(self):
		self.easyCloud.set_location(self.location_var.get())
		print self.location_var.get()
		
	def print_var(self):
		print self.easyCloud.upload_location
		
	def sync(self):
		self.easyCloud.sync()
		
	def authenticate_dropbox(self):
		self.log = "Dropbox"
		out = self.easyCloud.authenticate_dropbox()
		if out == "[loaded access token]":
			#self.text.delete(0,END)
			self.text.insert(END, out)
		else:
			#self.text.delete(0,END)
			self.text.insert(END, '1. Go to: ' + out + '\n')
			self.text.insert(END, '2. Click \"Allow\" (you might have to log in first).\n')
			self.text.insert(END, '3. Copy the authorization code.\n')
	
	def authenticate_googleDrive(self):
		self.log = "GoogleDrive"
		out = self.easyCloud.authenticate_googleDrive()
		if out == "[loaded access token]":
			#self.text.delete(0,END)
			self.text.insert(END, out)
		else:
			#self.text.delete(0,END)
			self.text.insert(END, '1. Go to: ' + out + '\n')
			self.text.insert(END, '2. Click \"Allow\" (you might have to log in first).\n')
			self.text.insert(END, '3. Copy the authorization code.\n')
	
	def submit_token(self):
		strg = self.entry.get()
		if len(strg)!=0:
			self.entry.delete(0, END)
			out = "None"
			if self.log == "Dropbox":
				out = self.easyCloud.send_dropbox_token(strg)
			elif self.log == "GoogleDrive":
				out = self.easyCloud.send_googleDrive_token(strg)
			self.text.insert(END, out)
		
root=Tk()
root.title('EasyCloud')

app = App(root)

def loop():
	#app.print_var()
	root.after(10000, loop)


root.after(1, loop)
root.mainloop()

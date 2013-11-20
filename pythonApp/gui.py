#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Tkinter import *
from easyCloud import *

class App:
	def __init__(self,master):
		self.easyCloud = easyCloud()
		self.log = None
		self.currentList = []
		frame = Frame(master)
		frame.pack()
	
		#textfr=Frame(frame)
		
		frame2 = Frame(frame, height=40, width=50)
		frame2.pack()

		self.dropbox_button = Button(frame2, text = "Dropbox", fg = "black", command = self.authenticate_dropbox)
		#self.dropbox_button.place(x=1, y=35, width=120)
		self.dropbox_button.pack(side=LEFT, padx=10, pady=2.5)
		
		self.skydrive_button = Button(frame2, text = "Skydrive", fg = "black", command = self.authenticate_skydrive)
		#self.skydrive_button.place(x=5,y=35, width=120)
		self.skydrive_button.pack(side=LEFT, padx=10, pady=2.5)
		
		self.googleDrive_button = Button(frame2, text = "Google Drive", fg = "black", command = self.authenticate_googleDrive)
		#self.googleDrive_button.place(x=5,y=35, width=120)
		self.googleDrive_button.pack(side=LEFT, padx=10, pady=2.5)
		
		
		
		
		
		self.text=Text(frame,height=10,width=50,background='white')
		self.text.place(x=70, y=40)
		self.text.pack()
		# put a scroll bar in the frame

		#scroll = Scrollbar(textfr)
		#self.text.configure(yscrollcommand=scroll.set)
		#scroll.pack(side=RIGHT,fill=Y)
		
		
		self.entry = Entry(frame,width=50)
		self.entry.place(x=30, y=90)
		self.entry.pack()
		
		
		self.submit_button = Button(frame, text = "Submit", fg = "black", command = self.submit_token)
		self.submit_button.pack(side=LEFT, padx=10, pady=10)
		
		self.sync_button = Button(frame, text = "Sync", fg = "black", command = self.sync)
		self.sync_button.pack(side=LEFT, padx=10, pady=10)
		
		self.location_var = StringVar(frame)
		self.location_var.set(str(self.easyCloud.getDefaultLocation()))
		self.location_choices = ['Split', 'All', 'Only To Dropbox', 'Only To Google Drive', 'Only To SkyDrive']
		self.location_option = OptionMenu(frame, self.location_var, *(self.location_choices))
		self.location_option.pack(side='left', padx=10, pady=10)
		
		self.button_location = Button(frame, text = "Set", fg = "black", command = self.set_upload_location)
		self.button_location.pack(side=LEFT, padx=10, pady=10)
		
		self.easyCloud.authenticate_dropbox()
		self.dropbox_button['fg'] = 'red'
		self.easyCloud.authenticate_googleDrive()
		self.googleDrive_button['fg'] = 'red'
		self.easyCloud.authenticate_skydrive()
		self.skydrive_button['fg'] = 'red'
		
	def set_upload_location(self):
		self.easyCloud.set_location(self.location_var.get())
		print self.location_var.get()
		
	def print_var(self):
		print self.easyCloud.upload_location
		
	def sync(self):
		print "Syncing..."
		self.easyCloud.sync()
		return
		
	def authenticate_dropbox(self):
		self.log = "Dropbox"
		out = self.easyCloud.authenticate_dropbox()
		if out == "[loaded access token]":
			#self.text.delete(0,END)
			self.dropbox_button['fg'] = 'red'
			self.text.insert(END, out+'\n')
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
			self.googleDrive_button['fg'] = 'red'
			self.text.insert(END, out+'\n')
		else:
			#self.text.delete(0,END)
			self.text.insert(END, '1. Go to: ' + out + '\n')
			self.text.insert(END, '2. Click \"Allow\" (you might have to log in first).\n')
			self.text.insert(END, '3. Copy the authorization code.\n')
			
	def authenticate_skydrive(self):
		self.log = "Skydrive"
		out = self.easyCloud.authenticate_skydrive()
		if out == "[loaded access token]":
			#self.text.delete(0,END)
			self.skydrive_button['fg'] = 'red'
			self.text.insert(END, out+'\n')
		else:
			#self.text.delete(0,END)
			self.text.insert(END, '1. Go to: ' + out + '\n')
			self.text.insert(END, '2. authorize there, confirm access permissions, and paste URL of an empty page (starting with "https://login.live.com/oauth20_desktop.srf") you will get redirected to in the end.\n')
	
	def submit_token(self):
		strg = self.entry.get()
		if len(strg)!=0:
			self.entry.delete(0, END)
			out = "None"
			if self.log == "Dropbox":
				out = self.easyCloud.send_dropbox_token(strg)
				if out == "[loaded access token]":
					self.dropbox_button['fg'] = 'red'
			elif self.log == "GoogleDrive":
				out = self.easyCloud.send_googleDrive_token(strg)
				if out == "[loaded access token]":
					self.googleDrive_button['fg'] = 'red'
			elif self.log == "Skydrive":
				out = self.easyCloud.send_skydrive_token(strg)
				if out == "[loaded access token]":
					self.skydrive_button['fg'] = 'red'
			self.text.insert(END, str(out)+'\n')
			self.log = None
			
	def compareLocalFileList(self):
		newList = self.easyCloud.getLocalFileList()
		if list(set(newList) - set(self.currentList)) or list(set(self.currentList) - set(newList)):
			self.currentList = newList
			return False
		else:
			self.currentList = newList
			return True
		
root=Tk()
root.title('EasyCloud')

app = App(root)

f = False
i = 0

def loop2():
	app.sync()
	root.after(900000, loop2)

def loop():
	root.after(1000, loop2)

def loop4():
	if not app.compareLocalFileList():
		app.sync()
	root.after(5000, loop4)
	
def loop3():
	root.after(1000, loop4)
	
root.after(1, loop3) #pass loop for 15min Sync, loop3 for event driven
root.mainloop()

from driveClass import *
from functions import *
from dropboxClass import *
from skydriveClass import *
from sets import Set

class easyCloud:
	def __init__(self):
		self.CONFIG_FILE = 'config'
		f = open(self.CONFIG_FILE, "r")
		self.upload_location = f.readlines()[0] #read from config file
		f.close()
		self.drop = DropboxClass()
		self.drive = DriveClass()
		self.skydrive = skydriveClass()
		self.size = []
		#self.authenticate_dropbox()
		#self.authenticate_googleDrive()
		#self.authenticate_skydrive()
		
	def getDefaultLocation(self):
		return self.upload_location
		
	def authenticate_dropbox(self):
		return self.drop.login()
	
	def send_dropbox_token(self, strg):
		return self.drop.auth(strg)
	
	def authenticate_googleDrive(self):
		return self.drive.login()
	
	def send_googleDrive_token(self, strg):
		return self.drive.run_auth_flow(strg)
	
	def authenticate_skydrive(self):
		return self.skydrive.login()
	
	def send_skydrive_token(self, strg):
		return self.skydrive.auth(strg)
		
	def auth_list(self):
		authenticated_list = []
		if self.drop.isAuthenticated():
			authenticated_list.append("dropbox")
		if self.drive.isAuthenticated():
			authenticated_list.append("googleDrive")
		if self.skydrive.isAuthenticated():
			authenticated_list.append("skyDrive")
		return authenticated_list
			
	def set_location(self, i):
		f = open(os.path.expanduser(self.CONFIG_FILE), "wb")
		f.write(i)
		f.close()
		self.upload_location = i

	def getUploadLocation(self, i):
		if self.upload_location == 'Only To Dropbox':	
			return "dropbox"
		elif self.upload_location == 'Only To Google Drive':	
			return "googleDrive"
		elif self.upload_location == 'Only To Sky Drive':	
			return "skyDrive"
		elif self.upload_location == 'All':
			return "all"
		elif self.upload_location == 'Split':
			#print "Split"
			file_size = int(self.size[i])
			config = {}
			if "dropbox" in self.auth_list():
				drop_size, drop_used = self.drop.get_quota()
				drop_empty = drop_size - drop_used
				config['dropbox'] = [int(drop_empty), int(drop_size)]
			if "googleDrive" in self.auth_list():
				drive_size, drive_used = self.drive.get_quota()
				#print drive_size, drive_used	
				drive_empty = int(drive_size) - int(drive_used)
				config['googleDrive'] = [int(drive_empty), int(drive_size)]
			if "skyDrive" in self.auth_list():
				skydrive_size, skydrive_used = self.skydrive.get_quota()
				skydrive_empty = skydrive_size - skydrive_used
				config['skyDrive'] = [int(skydrive_empty), int(skydrive_size)]
			
			maximum = 0
			for i in config:
				print config[i][0]/float(config[i][1]), file_size, config[i][0]
				if config[i][0]/float(config[i][1]) > maximum and file_size < config[i][0]:
					print "Hello"
					key = i
					maximum = config[i][0]/float(config[i][1])
					
			print key
			return key
		else:
			print self.upload_location, 'Only To Google Drive', i
			print "Hell"
			return 0
	
	def sync(self):
		sync_upload = []
		sync_download = []
		file_drive = []
		file_drop = []
		file_skydrive = []
		file_local, self.size = get_structure('~/easyCloud',0)
		
		if self.drive.isAuthenticated():
			file_drive = self.drive.retrieve_all_files();
		else: 
			file_drive = []
		
		if self.drop.isAuthenticated():
			file_drop = self.drop.display_info('/easyCloud')
		else:
			file_drop = []

		if self.skydrive.isAuthenticated():
			file_skydrive = self.skydrive.get_info()
		else:
			file_skydrive = []
			
		merged_file_list_cloud = Set()
		file_local_set = Set()

		for i in file_drop:	
			merged_file_list_cloud.add(i)
			
		for i in file_drive:	
			merged_file_list_cloud.add(i)	
			
		for i in file_skydrive:
			merged_file_list_cloud.add(i)

		for i in file_local:
			file_local_set.add(i)

		sync_download = []
		for i in merged_file_list_cloud:
			flag = False
			for j in file_local:
				if i == j:
					flag = True
			if not flag:
				sync_download.append(i)

		sync_upload = []		
		for i in file_local:
			flag = False
			for j in merged_file_list_cloud:
				if i == j:
					flag = True
			if not flag:
				sync_upload.append(i)

		print "Sync Download:",
		print sync_download
		print "Sync Upload:",
		print sync_upload

		for i in sync_download:
			if i in file_drop:	
				self.drop.download(i, i)
			elif i in file_drive:
				self.drive.download(i, i)
			elif i in file_skydrive:
				self.skydrive.download(i, i)

		for i in sync_upload:
			loc = self.getUploadLocation(i)
			print loc
			if loc == "":
				print "Not enough Space"
				continue
			elif loc == "All":
				if self.drop.isAuthenticated():
					self.drop.upload(i,i)
				if self.drive.isAuthenticated():
					self.drive.upload(i,i)
				if self.skydrive.isAuthenticated():
					self.skydrive.upload(i,i)
			elif loc == 'dropbox' and self.drop.isAuthenticated():
				self.drop.upload(i,i)
			elif loc == 'googleDrive' and self.drive.isAuthenticated():
				self.drive.upload(i,i)
			elif loc == 'skyDrive' and self.skydrive.isAuthenticated():
				self.skydrive.upload(i,i)
		
		print "Synced"
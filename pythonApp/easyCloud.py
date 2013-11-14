from driveClass import *
from functions import *
from dropboxClass import *
from sets import Set

class easyCloud:
	def __init__(self):
		self.upload_location = 'Split'
		self.CONFIG_FILE = 'config'
		self.drop = DropboxClass()
		self.drive = DriveClass()

	def set_location(self, i):
		f = open(os.path.expanduser(self.CONFIG_FILE), "wb")
		f.write(i)
		f.close()
		self.upload_location = i

	def getUploadLocation(self, i):
		return "googleDrive"
	
	def authenticate_dropbox(self):
		return self.drop.login()
	
	def send_dropbox_token(self, strg):
		return self.drop.auth(strg)
	
	def authenticate_googleDrive(self):
		return self.drive.login()
	
	def send_googleDrive_token(self, strg):
		return self.drive.run_auth_flow(strg)
	
	def sync(self):
		file_local, size = get_structure('~/easyCloud',0)
		file_drive = self.drive.retrieve_all_files()
		file_drop = self.drop.display_info('/easyCloud')

		merged_file_list_cloud = Set()
		file_local_set = Set()

		for i in file_drop:	
			merged_file_list_cloud.add(i)
			
		for i in file_drive:	
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

		for i in sync_upload:
			loc = self.getUploadLocation(i)
			if loc == 'dropbox':
				self.drop.upload(i,i)
			elif loc == 'googleDrive':
				self.drive.upload(i,i)
				
		print self.drive.get_quota()
		
		print "Synced"
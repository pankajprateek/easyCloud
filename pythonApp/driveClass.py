#!/usr/bin/python

import cmd
import locale
import os
import pprint
import shlex
import sys
import httplib2

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient import errors
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

class DriveClass:
	def __init__(self):
		self.mapping={}
		self.TOKEN_FILE = "token_drive.txt"
		# Copy your credentials from the console
		self.CLIENT_ID = '278916592295.apps.googleusercontent.com'
		self.CLIENT_SECRET = 'JjdRNzvxuleTUqrZVzIzWH3M'
		# Check https://developers.google.com/drive/scopes for all available scopes
		self.OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
		# Redirect URI for installed apps
		self.REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
		self.current_path = ''
		self.drive_client = None
		self.authenticated = False
		
	def login(self):
		try:
			storage = Storage(self.TOKEN_FILE)
			self.credentials = storage.get()
			if self.credentials == None:
				"""log in to a Drive account"""
				# Run through the OAuth flow and retrieve credentials
				self.flow = OAuth2WebServerFlow(self.CLIENT_ID, self.CLIENT_SECRET, self.OAUTH_SCOPE, self.REDIRECT_URI)
				authorize_url = self.flow.step1_get_authorize_url()
				print 'Go to the following link in your browser: ' + authorize_url
				return authorize_url
			else:
				# Create an httplib2.Http object and authorize it with our credentials
				http = httplib2.Http()
				http = self.credentials.authorize(http)
				self.drive_client = build('drive', 'v2', http=http)
				self.authenticated = True
				return "[loaded access token]"
		except IOError:
			"""log in to a Drive account"""
			# Run through the OAuth flow and retrieve credentials
			self.flow = OAuth2WebServerFlow(self.CLIENT_ID, self.CLIENT_SECRET, self.OAUTH_SCOPE, self.REDIRECT_URI)
			authorize_url = self.flow.step1_get_authorize_url()
			print 'Go to the following link in your browser: ' + authorize_url
			return authorize_url
			
	def run_auth_flow(self, code):
		#code = raw_input('Enter verification code: ').strip()
		self.credentials = self.flow.step2_exchange(code)
		storage = Storage(self.TOKEN_FILE)
		storage.put(self.credentials)
		# Create an httplib2.Http object and authorize it with our credentials
		http = httplib2.Http()
		http = self.credentials.authorize(http)
		self.drive_client = build('drive', 'v2', http=http)
		self.authenticated = True
		print "[loaded access token]"
		
	def isAuthenticated(self):
		return self.authenticated
		
	def retrieve_all_files(self):
		def restructure(out):
			cloud = []
			remove = []
			prefix = {}
			prefix2 = {}
			trashed = []
			for i in out:
				self.mapping[i['title']] = i['id']
				if i['title'] == 'easyCloud':
					cloud.append(i['parents'][0]['selfLink'][len(i['parents'][0]['selfLink'])-56:len(i['parents'][0]['selfLink'])-28])
					prefix[i['parents'][0]['selfLink'][len(i['parents'][0]['selfLink'])-56:len(i['parents'][0]['selfLink'])-28]] = '~/easyCloud'
					prefix2[i['parents'][0]['selfLink'][len(i['parents'][0]['selfLink'])-56:len(i['parents'][0]['selfLink'])-28]] = i
					remove.append(i)
				
			depth=0
			for i in remove:
				out.remove(i)
				remove.remove(i)

			cloud2 = []
			while 1:
				oldout = []
				for i in out:
					oldout.append(i)
				for i in out:
					if i['labels']['trashed'] == True:
						continue
					parentLink = i['parents'][0]['parentLink'][len(i['parents'][0]['parentLink'])-28:]
					selfLink = i['parents'][0]['selfLink'][len(i['parents'][0]['selfLink'])-65:len(i['parents'][0]['selfLink'])-37]
					if parentLink in cloud:
						cloud2.append(selfLink)
						remove.append(i)
						prefix[selfLink] = prefix[parentLink] + '/' + i['title']
						prefix2[selfLink] = i
				while remove:
					for i in remove:
						out.remove(i)
						remove.remove(i)
				cloud=cloud2
				cloud2=[]
				if oldout == out:
					break

			structure = []
			for i in prefix:
				if not prefix2[i]['mimeType'] == "application/vnd.google-apps.folder":
					structure.append(prefix[i])
			return structure

		"""Retrieve a list of File resources.

		Args:
			service: Drive API service instance.
		Returns:
			List of File resources.
		"""
		service = self.drive_client
		result = []
		page_token = None
		while True:
			try:
				param = {}
				if page_token:
					param['pageToken'] = page_token
				files = service.files().list(**param).execute()

				result.extend(files['items'])
				page_token = files.get('nextPageToken')
				if not page_token:
					break
			except errors.HttpError, error:
				print 'An error occurred: %s' % error
				break
		return restructure(result)
	
	def upload(self):
		service = self.drive_client
		file1 = GoogleDriveFile(service, metadata=None)
		#file1 = self.CreateFile()
		return
		
	def print_mapping(self):
		for i in self.mapping:
			print i, self.mapping[i]
		print
	
	def print_file(self, title):
		service = self.drive_client
		try:
			tmp = title.split('/')
			title = tmp[len(tmp)-1]
			if title in self.mapping.keys():
				file_id = self.mapping[title]
			else:
				print "File doesn't exist"
				return
			file = service.files().get(fileId=file_id).execute()
			print 'Title: %s' % file['title']
			print 'MIME type: %s' % file['mimeType']
		except errors.HttpError, error:
			print 'An error occurred: %s' % error
			
			
	def download(self, title, to_path):
		service = self.drive_client
		tmp = title.split('/')
		title = tmp[len(tmp)-1]
		if title in self.mapping.keys():
			file_id = self.mapping[title]
		else:
			print "File doesn't exist"
			return
		file = service.files().get(fileId=file_id).execute()
		download_url = file.get('downloadUrl')
		#print download_url
		if download_url:
			resp, content = service._http.request(download_url)
			if resp.status == 200:
				print 'Status: %s' % resp
				to_file = open(os.path.expanduser(to_path), "wb")
				to_file.write(content)
				#print content
			else:
				print 'An error occurred: %s' % resp
				return None
		else:
			return None
			
			
	def upload(self, title, upload_loc):
		service = self.drive_client
		tmp = title.split('/')
		title = '/home/pankaj'+title[1:]
		if tmp[len(tmp)-2] in self.mapping.keys():
			parent_id = self.mapping[tmp[len(tmp)-2]]
		else:
			tmpx = []
			for i in range(1,len(tmp)-2):
				tmpx.append(tmp[i])
				tmpx.append('/')
			t="".join(tmpx[:len(tmpx)-1])
			self.create_folder(tmp[len(tmp)-2], t)
			parent_id = self.mapping[tmp[len(tmp)-2]]
			#create_folder(tmp[len(tmp)-2], 
		#print parent_id
		#print title
		
		from_file = open(os.path.expanduser(title), "rb")
		if not from_file.read():
			print "File Empty "+title
			return
		
		#FILENAME = "document.txt"
		media_body = MediaFileUpload(title, mimetype='text/plain', resumable=True)
		body = {
			'title': tmp[len(tmp)-1],
			'description': 'A test document',
			'mimeType': 'text/plain'
		}
		body['parents'] = [{'id': parent_id}]

		file = service.files().insert(body=body, media_body=media_body).execute()
		print "Uploaded "+title
		#pprint.pprint(file)
		return
	
	def create_folder(self, name, path):
		service = self.drive_client
		tmp = path.split('/')
		if tmp[len(tmp)-1] in self.mapping.keys():
			parent_id = self.mapping[tmp[len(tmp)-1]]
		else:
			t = path.split('/')
			n = t[len(t)-1]
			tmpx = []
			for i in range(0,len(t)-1):
				tmpx.append(t[i])
				tmpx.append('/')
			x = "".join(tmpx[:len(tmpx)-1])
			self.create_folder(n,x)
			parent_id = self.mapping[tmp[len(tmp)-1]]
			#return
		body = {
			'title': name,
			'parents': [{"id": parent_id}],
			'mimeType': "application/vnd.google-apps.folder"
		}
		file = service.files().insert(body=body).execute()
		self.mapping[name]=file['id']
		print "Created Folder", name
		return


	def get_quota(self):
		service = self.drive_client
		try:
			about = service.about().get().execute()

			#print 'Current user name: %s' % about['name']
			#print 'Total quota (bytes): %s' % about['quotaBytesTotal']
			#print 'Used quota (bytes): %s' % about['quotaBytesUsed']
			return about['quotaBytesTotal'], about['quotaBytesUsed']
		except errors.HttpError, error:
			print 'An error occurred: %s' % error
			return 0
		
	def delete(self, title):  #deletes both files and folders
		service = self.drive_client
		if title in self.mapping.keys():
			file_id = self.mapping[title]
			del self.mapping[title]
		else:
			print "Not Exist"
			return
		try:
			service.files().delete(fileId=file_id).execute()
			print "Deleted", title
		except errors.HttpError, error:
			print 'An error occurred: %s' % error
		return


#drive = DriveClass()
#drive.retrieve_all_files()
#drive.delete('pic.JPG')
#drive.delete('pic.JPG')
#drive.create_folder('try','easyCloud/hello')

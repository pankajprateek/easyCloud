#!/usr/bin/python

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient import errors
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

class DriveClass:
	def __init__(self):
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
		try:
			storage = Storage(self.TOKEN_FILE)
			self.credentials = storage.get()
			if self.credentials == None:
				self.run_auth_flow()
			else:
				# Create an httplib2.Http object and authorize it with our credentials
				http = httplib2.Http()
				http = self.credentials.authorize(http)
				self.drive_client = build('drive', 'v2', http=http)
				print "[loaded access token]"
		except IOError:
			self.run_auth_flow()
			
			
	def run_auth_flow(self):
		"""log in to a Drive account"""
		# Run through the OAuth flow and retrieve credentials
		flow = OAuth2WebServerFlow(self.CLIENT_ID, self.CLIENT_SECRET, self.OAUTH_SCOPE, self.REDIRECT_URI)
		authorize_url = flow.step1_get_authorize_url()
		print 'Go to the following link in your browser: ' + authorize_url
		code = raw_input('Enter verification code: ').strip()
		self.credentials = flow.step2_exchange(code)
		storage = Storage(self.TOKEN_FILE)
		storage.put(self.credentials)
		# Create an httplib2.Http object and authorize it with our credentials
		http = httplib2.Http()
		http = self.credentials.authorize(http)
		self.drive_client = build('drive', 'v2', http=http)
		print "[Authenticated]"
		
	def retrieve_all_files(self):
		def restructure(out):
			cloud = []
			remove = []
			prefix = {}
			prefix2 = {}
			for i in out:
				if i['title'] == 'easyCloud':
					cloud.append(i['parents'][0]['selfLink'][len(i['parents'][0]['selfLink'])-56:len(i['parents'][0]['selfLink'])-28])
					prefix[i['parents'][0]['selfLink'][len(i['parents'][0]['selfLink'])-56:len(i['parents'][0]['selfLink'])-28]] = 'easycloud'
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
	
	
'''
# Path to the file to upload
FILENAME = 'document.txt'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': 'My document',
  'description': 'A test document',
  'mimeType': 'text/plain'
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)
'''

#drive = DriveClass()
#out = drive.retrieve_all_files()
#print out
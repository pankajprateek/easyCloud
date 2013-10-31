#!/usr/bin/env python

import cmd
import locale
import os
import pprint
import shlex
import sys

from dropbox import client, rest

class DropboxClass:
	def __init__(self):
		self.TOKEN_FILE = "token_store.txt"
		self.APP_KEY = '0c427x8b2xinzca'
		self.APP_SECRET = '6uncb4b907gg8bb'
		self.current_path = ''
		self.api_client = None
		try:
			token = open(self.TOKEN_FILE).read()
			self.api_client = client.DropboxClient(token)
			print "[loaded access token]"
		except IOError:
			#pass # don't worry if it's not there
			#login user if the auth-token is not found
			"""log in to a Dropbox account"""
			flow = client.DropboxOAuth2FlowNoRedirect(self.APP_KEY, self.APP_SECRET)
			authorize_url = flow.start()
			sys.stdout.write("1. Go to: " + authorize_url + "\n")
			sys.stdout.write("2. Click \"Allow\" (you might have to log in first).\n")
			sys.stdout.write("3. Copy the authorization code.\n")
			code = raw_input("Enter the authorization code here: ").strip()
			
			try:
				access_token, user_id = flow.finish(code)
			except rest.ErrorResponse, e:
				self.stdout.write('Error: %s\n' % str(e))
				return
			
			with open(self.TOKEN_FILE, 'w') as f:
				f.write(access_token)
			self.api_client = client.DropboxClient(access_token)
	
	def display_info(self,path):
		"""list files in current remote directory or directory specified by path"""
		def display_file_info(path,depth):
			if path == '':
				path = self.current_path
			resp = self.api_client.metadata(path)
			for i in resp['contents']:
				'''
				for j in range(0,depth):
					print '   ',
				print i['path']
				'''
				if i['is_dir']:
					display_file_info(i['path'],depth+1)
				else:
					structure.append(i['path'])
		structure = []
		display_file_info(path,0)
		return structure
	
	def download(self, from_path, to_path):
		to_file = open(os.path.expanduser(to_path), "wb")
		f, metadata = self.api_client.get_file_and_metadata(self.current_path + "/" + from_path)
		print 'Metadata:', metadata
		to_file.write(f.read())
		
	def upload(self, from_path, to_path):
		from_file = open(os.path.expanduser(from_path), "rb")
		self.api_client.put_file(self.current_path + "/" + to_path, from_file)
	
def main():	
	drop = DropboxClass()
	out = drop.display_info('/easyCloud')
	for i in out:
		print i
	
if __name__ == '__main__':
	main()
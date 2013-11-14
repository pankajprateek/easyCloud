#!/usr/bin/python

from __future__ import unicode_literals, print_function

import cmd
import locale
import os
import pprint
import shlex
import sys
import httplib2
import itertools as it, operator as op, functools as ft
from os.path import dirname, basename, exists, isdir, join, abspath
from collections import defaultdict
import io, re, types, json

try:
	import chardet
except ImportError: # optional
	chardet = None
	
import api_v5, conf

class skydriveClass:
	def __init__(self):
		self.TOKEN_FILE = "~/.lcrc"
		self.api_client = api_v5.PersistentSkyDriveAPI.from_conf(self.TOKEN_FILE)
		if not self.api_client.get_quota():
			print('Visit the following URL in any web browser (firefox, chrome, safari, etc),\n'
					'  authorize there, confirm access permissions, and paste URL of an empty page\n'
					'  (starting with "https://login.live.com/oauth20_desktop.srf")'
					' you will get redirected to in the end.')
			print('Alternatively, use the returned (after redirects)'
					' URL with "{} auth <URL>" command.\n'.format(sys.argv[0]))
			print('URL to visit: {}\n'.format(self.api_client.auth_user_get_url()))
			url = raw_input('URL after last redirect: ').strip()
			self.api_client.auth_user_process_url(url)
			self.api_client.auth_get_token()
			print('API auth was completed successfully')
		print("[loaded access token]")
		
	def get_quota(self):
		free, quota = self.api_client.get_quota()
		used = quota - free
		return quota, used
	
	def get_info(self):
		def id_match( s,
						_re_id=re.compile(r'^(file|folder)\.[0-9a-f]{16}\.[0-9A-F]{16}!\d+|folder\.[0-9a-f]{16}$') ):
			return s if s and _re_id.search(s) else None
		resolve_path_wrap = lambda s: self.api_client.resolve_path(s and s.replace('\\', '/').strip('/'))
		resolve_path = ( (lambda s: id_match(s) or resolve_path_wrap(s)) \
							if not False else resolve_path_wrap ) if not False else lambda obj_id: obj_id

		def get_file_info(path, prefix):
			res = list(self.api_client.listdir(resolve_path(path)))
			for i in res:
				if i['type'] == 'folder':
					get_file_info(prefix+i['name'], prefix+i['name']+'/')
				if i['type'] == 'file':
					structure.append(prefix+i['name'])

		path = '/me/skydrive'
		structure = []
		get_file_info(path, '')
		structure2 = []
		for i in structure:
			if i[:9] == 'easyCloud':
				structure2.append('~/'+i)
		#print(resolve_path(path))
		#structure = list(self.api_client.listdir(resolve_path(path)))
		return structure2
	
	def download(self, title, location):
		title = title[2:]
		def id_match( s,
						_re_id=re.compile(r'^(file|folder)\.[0-9a-f]{16}\.[0-9A-F]{16}!\d+|folder\.[0-9a-f]{16}$') ):
			return s if s and _re_id.search(s) else None
		resolve_path_wrap = lambda s: self.api_client.resolve_path(s and s.replace('\\', '/').strip('/'))
		resolve_path = ( (lambda s: id_match(s) or resolve_path_wrap(s)) \
							if not False else resolve_path_wrap ) if not False else lambda obj_id: obj_id
		
		contents = self.api_client.get(resolve_path(title), byte_range=None)
		to_file = open(os.path.expanduser(location), "wb")
		to_file.write(contents)
		print(location)
		
	def upload(self, title, location):
		def id_match( s,
						_re_id=re.compile(r'^(file|folder)\.[0-9a-f]{16}\.[0-9A-F]{16}!\d+|folder\.[0-9a-f]{16}$') ):
			return s if s and _re_id.search(s) else None
		resolve_path_wrap = lambda s: self.api_client.resolve_path(s and s.replace('\\', '/').strip('/'))
		resolve_path = ( (lambda s: id_match(s) or resolve_path_wrap(s)) \
							if not False else resolve_path_wrap ) if not False else lambda obj_id: obj_id
							
		from_file = open(os.path.expanduser(title), "rb")
		if not from_file.read():
			print("File Empty "+title)
			return

		tmp = location.split('/')
		t=''
		for i in range(0,len(tmp)-1):
			t=t+tmp[i]+'/'
		try:
			resolve_path(t[2:len(t)-1])
		except:   #Create folder here
			tmpx=''
			for i in range(0,len(tmp)-2):
				tmpx=tmpx+tmp[i]+'/'
			self.create_folder(tmp[len(tmp)-2], tmpx[2:len(tmpx)-1])
		xres = self.api_client.put('/home/pankaj'+title[1:], resolve_path(t[2:len(t)-1]), overwrite=True)
		if xres:
			print(location)
			
	def create_folder(self, title, location):
		def id_match( s,
						_re_id=re.compile(r'^(file|folder)\.[0-9a-f]{16}\.[0-9A-F]{16}!\d+|folder\.[0-9a-f]{16}$') ):
			return s if s and _re_id.search(s) else None
		resolve_path_wrap = lambda s: self.api_client.resolve_path(s and s.replace('\\', '/').strip('/'))
		resolve_path = ( (lambda s: id_match(s) or resolve_path_wrap(s)) \
							if not False else resolve_path_wrap ) if not False else lambda obj_id: obj_id
		
		try:
			resolve_path(location)
		except:
			tmpx = ''
			tmp = location.split('/')
			for i in range(0, len(tmp)-1):
				tmpx = tmpx+tmp[i]+'/'
			self.create_folder(tmp[len(tmp)-1], tmpx[:len(tmpx)-1])
		xres = self.api_client.mkdir(name=title, folder_id=resolve_path(location), metadata=None and json.loads(None) or dict())
		if xres:
			print("Created Folder:"+location+'/'+title)
		return
              
	
	
#skydrive = skydriveClass()
#print(skydrive.get_quota())
#out = skydrive.get_info()
#for i in out:
	#print(i)
	
#skydrive.download('Documents/try/conf.py','conf.py')
#skydrive.upload('conf.py', 'Documents/try/conf.py')
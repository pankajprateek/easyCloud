from dropboxClass import *
from functions import *

file_local = get_structure('~/easyCloud',0)
print "File Local:",
print file_local

drop = DropboxClass()
file_drop = drop.display_info('/easyCloud')
print "File Dropbox:",
print file_drop

sync_upload = []
sync_download = []

for i in file_drop:
	flag = False
	for j in file_local:
		if i == j:
			flag = True
	if not flag:
		sync_download.append(i)
		
for i in file_local:
	flag = False
	for j in file_drop:
		if i == j:
			flag = True
	if not flag:
		sync_upload.append(i)

print "Sync Download:",
print sync_download
print "Sync Upload:",
print sync_upload

for i in sync_download:
	drop.download(i,i)
	
for i in sync_upload:
	drop.upload(i,i)
	
	
print drop.get_quota()
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
		if i[10:] == j[11:]:
			flag = True
	if not flag:
		sync_download.append(i[10:])
		
for i in file_local:
	flag = False
	for j in file_drop:
		if i[11:] == j[10:]:
			flag = True
	if not flag:
		sync_upload.append(i[11:])

print "Sync Download:",
print sync_download
print "Sync Upload:",
print sync_upload

print 
print

for i in sync_download:
	print 'easyCloud'+i,
	drop.download('easyCloud'+i,'~/easyCloud'+i)
	
print sync_upload
for i in sync_upload:
	print 'easyCloud'+i,
	drop.upload('~/easyCloud'+i,'easyCloud'+i)
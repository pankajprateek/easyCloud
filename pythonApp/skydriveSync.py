from skydriveClass import *
from functions import *

file_local, b = get_structure('~/easyCloud',0)
print "File Local:",
print file_local

skydrive = skydriveClass()
file_sky = skydrive.get_info()
print "File skydrive:",
print file_sky

sync_upload = []
sync_download = []

for i in file_sky:
	flag = False
	for j in file_local:
		if i == j:
			flag = True
	if not flag:
		sync_download.append(i)
		
for i in file_local:
	flag = False
	for j in file_sky:
		if i == j:
			flag = True
	if not flag:
		sync_upload.append(i)
		
		
print "Sync Download:",
print sync_download
print "Sync Upload:",
print sync_upload

for i in sync_download:
	skydrive.download(i,i)
	
for i in sync_upload:
	skydrive.upload(i,i)
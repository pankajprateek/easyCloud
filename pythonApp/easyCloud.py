from driveClass import *
from functions import *
from dropboxClass import *
from sets import Set

def getUploadLocation(i):
	return "googleDrive"

drive = DriveClass()
drop = DropboxClass()

file_local, size = get_structure('~/easyCloud',0)
file_drive = drive.retrieve_all_files()
file_drop = drop.display_info('/easyCloud')

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
		drop.download(i, i)
	elif i in file_drive:
		drive.download(i, i)

for i in sync_upload:
	loc = getUploadLocation(i)
	if loc == 'dropbox':
		drop.upload(i,i)
	elif loc == 'googleDrive':
		drive.upload(i,i)
		
print drive.get_quota()



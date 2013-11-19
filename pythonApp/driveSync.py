from driveClass import *
from functions import *

file_local, b,c = get_structure('~/easyCloud',0)
print "File Local:",
print file_local

drive = DriveClass()
drive.login()
file_drive = drive.retrieve_all_files()
print "File Google Drive:",
print file_drive

print drive.getModificationData()

'''
sync_upload = []
sync_download = []

for i in file_drive:
	flag = False
	for j in file_local:
		if i == j:
			flag = True
	if not flag:
		sync_download.append(i)
		
for i in file_local:
	flag = False
	for j in file_drive:
		if i == j:
			flag = True
	if not flag:
		sync_upload.append(i)

print "Sync Download:",
print sync_download
print "Sync Upload:",
print sync_upload


#drive.print_mapping()
for i in sync_download:
	#drive.print_file(i)
	drive.download(i,i)

for i in sync_upload:
	drive.upload(i,i)
	
	
#print drive.get_quota()
#print 
#print

#for i in sync_download:
	#print 'easyCloud'+i,
	#drop.download('easyCloud'+i,'~/easyCloud'+i)
	
#print sync_upload
#for i in sync_upload:
	#print 'easyCloud'+i,
	#drop.upload('~/easyCloud'+i,'easyCloud'+i)
	
'''
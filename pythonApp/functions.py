import os
import subprocess
import commands

def sys_exec(command):
	return commands.getstatusoutput(command)
	#output = subprocess.check_output(command, shell=True)
	#os.system(command)
	
structure = []
def get_structure(path,depth):
	out = sys_exec("".join(['ls -al ',path]))
	out2=out[1].split('\n')
	for temp in out2[3:]:
		temp1 = temp.split()
		if temp1[0][0]=='d':
			tmp = get_structure("".join([path,'/',temp1[8]]),depth+1)
		else:
			structure.append("".join([path,'/',temp1[8]]))
	return structure
			
def display_structure(path,depth):
	temp = get_structure(path,depth)
	for i in temp:
		print i
	
#display_structure('~/easyCloud',0)
#out = get_structure('~/easyCloud',0)
#print out
'''
out = sys_exec("ls -al ~/easyCloud")
#print out[1]
out2=out[1].split('\n')
for temp in out2[3:]:
	temp1 = temp.split()
	print temp1[8],
	if temp1[0][0]=='d':
		print "directory",
	print
'''
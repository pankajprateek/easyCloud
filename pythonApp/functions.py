import os
import subprocess
import commands

def sys_exec(command):
	#print "executing", command
	return commands.getstatusoutput(command)
	#output = subprocess.check_output(command, shell=True)
	#os.system(command)
	
structure = []
size = {}
modified = {}
	
def get_structure(path,depth):
	def get_st(path,depth):
		out = sys_exec("".join(['ls -al ',path]))
		out2=out[1].split('\n')
		for temp in out2[3:]:
			temp1 = temp.split()
			if temp1[0][0]=='d':
				tmp = get_st("".join([path,'/',temp1[8]]),depth+1)
			else:
				size["".join([path,'/',temp1[8]])] = temp1[4]
				modified["".join([path,'/',temp1[8]])] = [temp1[5], int(temp1[6]), int(temp1[7].split(':')[0])*100+int(temp1[7].split(':')[1])]
				structure.append("".join([path,'/',temp1[8]]))
			
	structure = []
	size = {}
	modified = {}
	get_st(path,depth)
	return structure, size, modified
			
def display_structure(path,depth):
	temp,x = get_structure(path,depth)
	for i in temp:
		print i
		
#display_structure('~/easyCloud',0)
#out, b, x = get_structure('~/easyCloud',0)
#print x
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
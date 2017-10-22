filename='~/write_python'
#for line in open(filename):

# read a file
"""
with open(filename) as file_handler:
	lines = file_handler.readlines()
	for line in lines:
		print line
"""

# write and append to a file
"""
with open(filename,'w') as file_handler:
	lines = file_handler.write("write a file into python \n")
with open(filename,'a') as file_appender:
	file_appender.write("Appending a new line into python file \n")
"""
"""
Exception for unable to find a file
"""
try:
	#filename = '/var/log/notthere'
	for line in open(filename):
		print line
except IOError:
	print "File doesn't exist"
else:
	print "Done processing the file"


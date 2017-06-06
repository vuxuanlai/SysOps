#!/usr/bin/python
import os, sys
used_space_1=os.popen("df -h / | grep -v Filesystem | awk '{print $5}'").readline().strip()
used_space = int(used_space_1[:2])
#print "used space", used_space
warn = int(sys.argv[2])
#print "warn set: ", warn
crit = int(sys.argv[4])
#print "crit set: ", crit
if used_space < warn:
	print "OK - disk space used = %2f%% | used_space=%2f" % (used_space, used_space)
	sys.exit(0)
elif used_space > crit:
	print "CRITICAL - disk space used = %2f%% | used_space=%2f" % (used_space, used_space)
	sys.exit(2)
elif used_space > warn and used_space < crit:
	print "WARNING - disk space used = %2f%% | used_space=%2f" % (used_space, used_space)
	sys.exit(2)
else:
	print "UNKNOW - disk space used = %2f%% | used_space=%2f" % (used_space, used_space)
	sys.exit(3)

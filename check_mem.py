#!/usr/bin/python
import os, sys

# Threshold for warning
warning_memory   = float(sys.argv[2])
critical_memory = float(sys.argv[4])
# Get memory usage
total_memory = float(os.popen("free -m | grep Mem | awk '{print $2}'").readline().strip())
used_memory  = float(os.popen("free -m | grep Mem | awk '{print $3}'").readline().strip())
free_memory  = float(os.popen("free -m | grep Mem | awk '{print $4}'").readline().strip())

# Calculate for warning
used_memory_percent = (used_memory/total_memory)*100
free_memory_percent = 100 - used_memory_percent
if int(used_memory_percent) >= int(critical_memory):
    print "STATISTICS CRITICAL : Used memory=%.2f%% | Used_memory=%.2f%%" % (used_memory_percent, used_memory_percent)
    sys.exit(2)
elif int(used_memory_percent)<int(critical_memory) and int(used_memory_percent)>=int(warning_memory):
    print "STATISTICS WARNING : Used memory=%.2f%% | Used_memory=%.2f%%" % (used_memory_percent,  used_memory_percent)
    sys.exit(1)
else:
    print "STATISTICS OK : Used memory=%.2f%% | Used_memory=%.2f%%" % (used_memory_percent, used_memory_percent)
    sys.exit(0)

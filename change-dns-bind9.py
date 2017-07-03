#!/usr/bin/python
import os
import sys

# Arguments input
print "argument list:", str(sys.argv[1]), str(sys.argv[2])

# Load db.domain file
with open ("/etc/bind/zones/db.homelab.local") as f:
    db_file = f.read().splitlines()
f.close()

# Add  IP to db.homelab.local
if str(sys.argv[1])== '-a':
    ip_to_add = str(sys.argv[2])
    ip_to_del = 0
    print "Need to add IP: ", ip_to_add
    host_index = len(db_file)-16
    db_file.append('host'+str(host_index)+'.homelab.local.\t    IN \t    A\t    '+ip_to_add)
    print db_file
    f = open('/etc/bind/zones/db.homelab.local', "w")
    for item in db_file:
        f.write("%s\n" % item)

# Remove IP from db.homelab.local
elif str(sys.argv[1])== '-r':
    ip_to_del = str(sys.argv[2])
    ip_to_add = 0
    print "Need to del IP: ", ip_to_del
    for item in db_file:
        print item.find(ip_to_del)
        if item.find(ip_to_del)>= 0:
            db_file.remove(item)
    print db_file
    f = open('/etc/bind/zones/db.homelab.local', "w")
    for item in db_file:
        f.write("%s\n" % item)

#!/usr/bin/python
import os
import subprocess
import json

def file_to_list(file_name):
    results = []
    f = open(file_name)
    for line in f:
        results.append(line.rstrip())
    return results
if __name__ == '__main__':

    # Add host to icinga director
    hostname = os.popen("hostname -f | awk '{print $1}'").readline().strip()
    command1 = "cat /etc/hosts | grep " + hostname + " | awk \'{print $1}\'"
    host_ip = os.popen(command1).readline().strip()
    hostname = 'test_' + hostname[:3][1:] + '_' + hostname[4:]
    variables = file_to_list("add_host_template.conf")
    variables = filter(None, variables)
    variables_dict = {}
    for item in variables:
        variables_dict[item.split()[0]] = item.split()[1]
    variables_dict['display_name'] = hostname
    variables_dict['address'] = host_ip
    variables_dict['object_name'] = hostname
    variables_json =  json.dumps(variables_dict, ensure_ascii=False)
    command = 'curl -X POST -H \'Accept: application/json\' -u \'admin:admin\' http://10.0.0.6/icingaweb2/director/host -d ' + "\'" + variables_json + "\'"
    subprocess.call(command, shell = True)

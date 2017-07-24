#!/usr/bin/python
import os
import subprocess
import fileinput
import json

def file_to_list(file_name):
    results = []
    f = open(file_name)
    for line in f:
        results.append(line.rstrip())
    return results

if __name__ == '__main__':
    variables = file_to_list("icinga_agent.conf")
    variables = filter(None, variables)
    variables_dict = {}
    for item in variables:
        variables_dict[item.split()[0]] = item.split()[1]
    variables_json =  json.dumps(variables_dict, ensure_ascii=False)
    print variables_json
    command = 'curl -X POST -H \'Accept: application/json\' -u \'admin:admin\' http://54.85.238.216/icingaweb2/director/host -d ' + "\'" + variables_json + "\'"
    subprocess.call(command, shell = True)

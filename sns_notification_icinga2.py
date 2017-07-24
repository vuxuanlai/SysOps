#!/usr/bin/python
import boto3
import os
import subprocess
import sys
#subprocess.call('echo executed >> notification.log', shell=True)

# Define env variable
address = sys.argv[2]
noti_author = sys.argv[4]
noti_comment = sys.argv[6]
date_time = sys.argv[8]
service_name = sys.argv[10]
host_name = sys.argv[12]
service_output = sys.argv[14]
service_state = sys.argv[18]
noti_type = sys.argv[20]

Message_string = "Date: " + date_time + "\n"+ "Host : " + host_name + "\n"+ "Host address: " + address + "\n" + "Notification type: " + noti_type + "\n" + "Service name: " + service_name + "\n"+ "Service state: " + service_state + "\n"+ "Notification comment: " + noti_comment + "\n"+ "Notification author: " + noti_author + "\n"+ "Additional text: " + service_output

Subject_string = "[" + service_state + "]" + "  [" + date_time + "] [" + host_name + "] [" + service_name + "]"
AWS_ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client = boto3.client('sns',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY,region_name = 'us-east-1')
response = client.publish(
     TopicArn='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     Message= Message_string,
     Subject= Subject_string
)

import boto3
from pprint import pprint

AWS_ACCESS_KEY_ID = 'XXXXXXXXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

ec2 = boto3.resource('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY,region_name='us-east-1')
vpc = ec2.Vpc("vpc-xxxxxxx")
for i in vpc.instances.all():
    for tag in i.tags:
        if tag['Key'] == 'Name':
            print(tag['Value'])
for instance in vpc.instances.all():
    print(instance.id, instance.instance_type)

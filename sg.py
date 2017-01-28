#!/usr/bin/python

#Importing Libraries
import boto3
import sys

#creating variables for input to obtain required details
ec2id = sys.argv[1]
reg = sys.argv[2]
#calling ec2 client through boto3
client = boto3.client('ec2')

ec2 = boto3.resources('ec2', region_name=reg)
all_sg_ids = [sg['GroupId'] for sg in ec2.Instance(ec2id).security_groups]
for secid in all_sg_ids;
  result = client.describe_security_groups(GroupIds=[secid])
  print(result)

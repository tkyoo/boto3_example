#!/usr/bin/python3
import subprocess
import re
import time
import boto3


# Reference API: http://boto3.readthedocs.io/en/latest/reference/services/ses.html


# Check the list of yarn applications and send the email when it is empty:
popen = subprocess.Popen("yarn application -list", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
str = str(popen.communicate())
res = re.findall(r"application_[0-9]+_[0-9]+", str)

if len(res) == 0:
  # Send the email using the boto3 library
  ses = boto3.client('ses', region_name = 'us-west-2')

  response = ses.send_email(
    Source = 'your-source@email.com',
    Destination = {
      'ToAddresses' : [
        'your-destination@email.com'
      ]
    },
    Message= {
      'Subject': {
        'Data' : 'Subject - Check! EMR Cluster',
        'Charset' : 'utf-8'
      },
      'Body': {
        'Text' : {
          'Data': 'Body-Text-Data',
          'Charset' : 'utf-8'
        },
        'Html': {
          'Data' : 'The application is missing. Check the cluster status!!!',
          'Charset' : 'utf-8'
        }
      }
    },
    SourceArn='your-authorized-ses-arn-source'
  )

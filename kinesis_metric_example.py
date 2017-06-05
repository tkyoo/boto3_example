#!/usr/bin/python3
import boto3
import datetime

# Reference API: http://boto3.readthedocs.io/en/latest/reference/services/cloudwatch.html

# Get the 'GetRecords.IteratorAgeMilliseconds' metric statistics for 1 minute.
client = boto3.client('cloudwatch')

now = datetime.datetime.utcnow()
delta = datetime.timedelta(minutes = 1)
startTime = now - delta

statistics = client.get_metric_statistics(
  Namespace = 'AWS/Kinesis',
  MetricName = 'GetRecords.IteratorAgeMilliseconds',
  Dimensions = [{'Name' : 'StreamName', 'Value' : 'Your-Kinesis-Stream-Name'}],
  StartTime = startTime,
  EndTime = now,
  Period = 60,
  Statistics = [ 'Minimum', 'Maximum', 'Average' ]
)

print(statistics)

# boto3_example
Examples using the amazon boto3 python library

1. ses_example.py

Reference API: http://boto3.readthedocs.io/en/latest/reference/services/ses.html

Check the list of yarn applications and send the email when it is empty

2. kinesis_metric_example.py

Reference API: http://boto3.readthedocs.io/en/latest/reference/services/cloudwatch.html

Get the 'GetRecords.IteratorAgeMilliseconds' metric statistics for 1 minute.

'GetRecords.IteratorAgeMilliseconds' is one of the enhanced monitoring metrics which is very useful whether kinesis clients are delayed or not.

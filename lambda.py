import json
import boto3
import base64
import os

s3 = boto3.client('s3')


BUCKET_NAME = 'kinesis-bucket-leon'


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
   
    for record in event['Records']:

        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("Decoded payload:", payload)
       
        file_name = f"kinesis_data/{context.aws_request_id}-{record['eventID']}.json"
    
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=payload
        )
       
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed records.')
    }

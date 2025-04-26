import boto3
import os

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_KEY = os.getenv('SECRET_KEY')

s3 = boto3.client(
    's3',
    aws_access_key_id= ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_KEY,
    region_name='ap-south-1'
)

s3.create_bucket(
    Bucket='leon-new-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

s3.upload_file(
    Filename=r'C:\Users\Leon\Downloads\test.txt',
    Bucket='leon-new-bucket',
    Key='test.txt'  
)

s3.download_file(
    Bucket='leon-new-bucket',
    Key='test.txt',
    Filename='C:/Users/Leon/Downloads/hello_downloaded.txt'
)

s3.delete_object(
    Bucket='leon-new-bucket',
    Key='test.txt'
)

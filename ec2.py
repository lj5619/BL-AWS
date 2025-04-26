import boto3
import os

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_KEY = os.getenv('SECRET_KEY')

session = boto3.Session(
    aws_access_key_id= ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_KEY,
    region_name="ap-south-1"
)

kinesis_client = session.client("kinesis")

ec2 = session.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-002f6e91abff6eb96',
    InstanceType='t3.micro',
    SubnetId='subnet-08d7366adcf6f2426',  
    MinCount=1,
    MaxCount=1,
    KeyName='Leon',
    SecurityGroupIds=['sg-0973fe9234a0efd58'],
)

print(f'Created instance with ID: {instance[0].id}')

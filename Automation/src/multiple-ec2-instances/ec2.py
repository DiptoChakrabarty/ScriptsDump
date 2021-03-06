import boto3,os
from dotenv import load_dotenv
load_dotenv()

#Load env variables
# Add all these environment variables in your env file
# format of env file has been provided by adding an empty .env
access_key= os.getenv("ACCESS_KEY")
secret_key= os.getenv("SECRET_KEY")
ami= os.getenv("AMI")
region= os.getenv("REGION")
zone= os.getenv("ZONE")
type= os.getenv("TYPE")
subnet = os.getenv("SUBNET")

client = boto3.client(service_name='ec2', region_name=region, aws_access_key_id= access_key,aws_secret_access_key= secret_key)

# Create ec2 resource
ec2 = boto3.resource('ec2', region_name=region, aws_access_key_id= access_key,aws_secret_access_key= secret_key)
# create an instance
instance = ec2.create_instances(
    ImageId = ami,
    MinCount = 1,
    MaxCount = {specify max instances needed here},  # here replace brancket with the number of instances you need 
    InstanceType = type,   
    KeyName = key_name,  
    SubnetId = subnet)

instance.wait_until_running()
print("Instance Up and Running")

# To use the script run python3 ec2.py 

#LUIT/stopEC2-lambda.py
import boto3

def lambda_handler(event, context):
    # Create an EC2 client for the specific AWS region
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace with your region
    try:
        # Get details of running instances
        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )

        # Extract instance IDs from the response
        instance_ids = [
            instance['InstanceId']
            for reservation in response['Reservations']
            for instance in reservation['Instances']
        ]

        # Stop the instances if any are running
        if instance_ids:
            ec2.stop_instances(InstanceIds=instance_ids)
            print(f"Stopped instances: {instance_ids}")
        else:
            print("No running instances found.")
    except Exception as e:
        print(f"Error stopping instances: {e}")


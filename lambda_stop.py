import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instance_id = 'YOUR_INSTANCE_ID'

    ec2.stop_instances(
        InstanceIds=[instance_id]
    )

    print("EC2 Stopped")

    return {
        'statusCode': 200,
        'body': 'EC2 Stopped Successfully'
    }

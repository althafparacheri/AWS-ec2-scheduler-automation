import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instance_id = 'YOUR_INSTANCE_ID'

    ec2.start_instances(
        InstanceIds=[instance_id]
    )

    print("EC2 Started")

    return {
        'statusCode': 200,
        'body': 'EC2 Started Successfully'
    }

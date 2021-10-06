# bron: https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
import boto3
region = '<region_xx>'
instances = ['i-<instance_id1>', 'i-<instance_id2>']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('Started your instances: ' + str(instances))

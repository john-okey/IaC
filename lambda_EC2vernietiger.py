# bron: https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
#
import boto3
region = '<region_x>'
instances = ['i-<instance_id1>', 'i-<instance_id2>']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

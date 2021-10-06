# bron: https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
#
import boto3
region = 'ap-southeast-2'
instances = ['i-0c3eef1874b338d56', 'i-02c43780b03a9c55a']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

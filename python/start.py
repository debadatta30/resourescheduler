import boto3
import logging
ec2 = boto3.resource('ec2')

ec2c = boto3.client('ec2')

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    # filter the instances based on filters() above
    instances = ec2.instances.filter(Filters=filters)

    # instantiate empty array
    RunningInstances = []

    for instance in instances:
        # for each instance, append to array and print instance id
        RunningInstances.append(instance.id)
        print (instance.id)
        
    ec2c.start_instances(InstanceIds=RunningInstances)
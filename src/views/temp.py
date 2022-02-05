#create funtion get impar number 1 to 100
def get_impar_number():
    for i in range(1,101):
        if i % 2 != 0:
            yield i

#create funtion get par number 1 to 100
def get_par_number():
    for i in range(1,101):
        if i % 2 == 0:
            yield i


#create ec2 instance aws
def create_ec2_instance(instance_type, image_id, key_name, security_group_ids):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=security_group_ids,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Test'
                    },
                ]
            },
        ]
    )
    return instance[0].id
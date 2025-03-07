import json
import os
import boto3

region = os.environ.get('REGION', 'eu-central-1')
recipient = os.environ.get('RECIPIENT', 'abdulrahmanalaa22@gmail.com')
source = os.environ.get('SOURCE', 'abdulrahmanalaa497@gmail.com')

client = boto3.client('ses', region_name=region)

def lambda_handler(event, context):
    
    response = client.send_email(
    Destination={
        'ToAddresses': [recipient]
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'The file {} was edited by the users\' ID of {}.'.format(event.Records[0].s3.object.key,event.Records[0].userIdentity.principalId),
            }
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Editing the {} state file'.format(event.Records[0].s3.object.key),
        },
    },
    Source=source
    )
    
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }
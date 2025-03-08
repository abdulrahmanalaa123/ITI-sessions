import boto3
import botocore
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.resource('s3')
dynamo = boto3.client('dynamodb')

def lambda_handler(event, context):
    logger.info("New files uploaded to the source bucket.")
        
    filename = event['Records'][0]['s3']['object']['key']
    sequenceId = event['Records'][0]['s3']['object']['sequencer']
        
        
    try:
        response = add_file(filename, sequenceId)
        logger.info("File copied to the destination bucket successfully!")
        
    except botocore.exceptions.ClientError as error:
        logger.error("There was an error copying the file to the destination bucket")
        print('Error Message: {}'.format(error))
        
    except botocore.exceptions.ParamValidationError as error:
        logger.error("Missing required parameters while calling the API.")
        print('Error Message: {}'.format(error))

def add_file(filename,sequenceId):
    try:
        print('filename is {}'.format(filename))
        print('sequence is {}'.format(sequenceId))
           
        response = dynamo.put_item(
            TableName='s3-filenames',
            Item={
                "file-name": {
                    'S':filename, 
                },
                # "sequenceId": sequenceId,
            })

        print(response)
        return response
    except botocore.exceptions.ClientError as err:
        logger.error(
            "Couldn't add file %s to table %s. Here's why: %s: %s",
            filename,
            dynamo.table.name,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],)
        raise
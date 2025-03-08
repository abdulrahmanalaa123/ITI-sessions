import boto3
import botocore
import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):
        
    destination_bucket = 'targetbucket-abdulrahmanalaa'
        
    try:
        response = s3.upload_file("test.txt", destination_bucket, "test/testing-lambda.txt")
        logger.info("File copied to the destination bucket successfully!")
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return False
    return True
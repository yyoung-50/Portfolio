import json
import boto3

s3 = boto3.client('s3')
sqs = boto3.client('sqs')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    orders = []

    # Retrieve the file from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    content = response['Body'].read().decode('utf-8')

    # Parse the JSON data
    orders = json.loads(content)

    # Add each order to the SQS queue
    for order in orders:
        message_body = json.dumps(order)
        response = sqs.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/123456789012/my-queue',
            MessageBody=message_body
        )
        print('Added order to queue: ', order)

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully added orders to queue')
    }

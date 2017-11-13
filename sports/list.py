import json
import os

import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def list(event, context):
    os.environ['DYNAMODB_TABLE'] = 'serverless-rest-api-with-dynamodb-dev'
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all sports from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response

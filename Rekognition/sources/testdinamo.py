from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
table = dynamodb.Table('rekognition')

#table = dynamodb.Table('test2')
response = table.query(
    KeyConditionExpression=Key('FaceId').eq('96585b71-ecad-4fae-9f92-514781579f0')
)

for i in response['Items']:
    print(i['FaceId'], ":", i['nombre'])


import inotify.adapters
import os
import time

import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('leogamboa-bucket2')


#from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError






notifier = inotify.adapters.Inotify()
notifier.add_watch('/var/www/html/media')

for event in notifier.event_gen():
    if event is not None:
        # detecta la creacion de un fichero en la ruta
        if 'IN_CREATE' in event[1]: 
              print("{0}".format(event[3]))
              origen="/var/www/html/media/"+"{0}".format(event[3])
              print(origen)
              destino="{0}".format(event[3])
              print(destino)
              time.sleep(1)

              #  sube fichero a S3
              s3.Bucket('leogamboa-bucket2').upload_file(origen, destino)

              #  busca imagen desde S3 en Recognition -MyCollection

              bucket='leogamboa-bucket2'
              collectionId='MyCollection'
              fileName=destino
              threshold = 70
              maxFaces=2

              client=boto3.client('rekognition')

              response=client.search_faces_by_image(CollectionId=collectionId,
                               Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                               FaceMatchThreshold=threshold,
                               MaxFaces=maxFaces)

              faceMatches=response['FaceMatches']
              print ('Matching faces')
              for match in faceMatches:
                  face_id=match['Face']['FaceId']
                  print ('face_id:' + face_id + "/")
                  print ('FaceId:' + match['Face']['FaceId'])
                  print ('ImageId:' + match['Face']['ImageId'])
                  print ('ExternalImageId:' + match['Face']['ExternalImageId'])
                  print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                  print

              # busca el  FaceId que encuentra Rekognition en la base de dato que guada los datos en el proceso de AddFaceId.
              dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
              table = dynamodb.Table('rekognition')

              print("GetItem succeeded:")
              try:
                  response = table.query(
                    KeyConditionExpression=Key('FaceId').eq(face_id)
                    )
              except ClientError as e:
                    print(e.response['Error']['Message'])
              else:
                    for i in response['Items']:
                         print(i['FaceId'], ":", i['nombre'])

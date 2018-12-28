import inotify.adapters
import os
import time

import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('leogamboa-bucket2')


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

              #  sube imagen fichero desde S3 a Recognition -MyCollection
              bucket='leogamboa-bucket2'
              collectionId='MyCollection'
              fileName=destino
              client=boto3.client('rekognition')
              response=client.index_faces

              response=client.index_faces(CollectionId=collectionId,
                           Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                           ExternalImageId=fileName,
                           DetectionAttributes=['ALL'])

              print ('Faces in ' + fileName)
              for faceRecord in response['FaceRecords']:
                         print (faceRecord['Face']['FaceId'])
                         print (faceRecord['Face']['ImageId'])
                         print (faceRecord['Face']['ExternalImageId'])

              # sube registro con datos de Rekognition /
              dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
              table = dynamodb.Table('rekognition')

              response = table.put_item(
              Item={
                   'FaceId': faceRecord['Face']['FaceId'],
                   'ImageId': faceRecord['Face']['ImageId'],
                   'ExternalImageId': faceRecord['Face']['ExternalImageId'],
                   'empleadoId': " ",
                   'nombre': " "
              }
              )

              print("PutItem succeeded:")



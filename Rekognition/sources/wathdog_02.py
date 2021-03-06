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
        if 'IN_CREATE' in event[1]:   #detecta la creacion de un fichero 
              print("{0}".format(event[3]))
              origen="/var/www/html/media/"+"{0}".format(event[3])
              print(origen)
              destino="{0}".format(event[3])
              print(destino)
              time.sleep(1)
              s3.Bucket('leogamboa-bucket2').upload_file(origen, destino)
#
              bucket='leogamboa-bucket2'
              collectionId='MyCollection'
              fileName="monica.jpg" #destino

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


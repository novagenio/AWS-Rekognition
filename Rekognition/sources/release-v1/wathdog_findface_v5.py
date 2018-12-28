
import inotify.adapters
import os
import time
import functions_rekognition
import boto3
#s3 = boto3.resource('s3')
#bucket = s3.Bucket('leogamboa-bucket2')

import decimal

notifier = inotify.adapters.Inotify()
notifier.add_watch('/var/www/html/media')

bucket='leogamboa-bucket2'
collectionId='MyCollection'


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
              functions_rekognition.upload_file_s3(origen, destino)
              #
              fileName=destino
              # va a SearchFaceByImage a buscar los rostros de la imagen en MyCollection  y luego despliega los datos en la base de datos.
#              functions_rekognition.SearchFacesByImage(fileName)






              texto=functions_rekognition.DetectFaces(fileName)
              print('Caracteristicas de tu rostro:' + texto)
              nombre=functions_rekognition.SearchFacesByImage(fileName)
              print('y tu nombre es: :' + nombre)

              functions_rekognition.Play_Polly (" ...." + texto + ",,ha,, tu nombre es ..  " + nombre)

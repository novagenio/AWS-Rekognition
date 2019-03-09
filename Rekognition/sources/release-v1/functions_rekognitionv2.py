import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir



#--------------------------------------------------------------------------------------------------------
def Play_Polly(texto):
        session = Session(profile_name="adminuser")
        polly = session.client("polly")
        response = polly.synthesize_speech(Text=texto, OutputFormat="mp3", VoiceId="Conchita")
        if "AudioStream" in response:
                with closing(response["AudioStream"]) as stream:
                     output = os.path.join(gettempdir(), "speech.mp3")
                     with open(output, "wb") as file:
                          file.write(stream.read())
        else:
            print("Could not stream audio")
            sys.exit(-1)
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output])


#----------------------------------------------------------------------------
# DetectFaces: recive una fichero imagen , busca rostros e identifica caracteristicas del rostro
def DetectFaces(photo):  # https://docs.aws.amazon.com/es_es/rekognition/latest/dg/faces-detect-images.html
    bucket='leogamboa-bucket2'
    client=boto3.client('rekognition')

    #imageFile='input.jpg'
    #with open(imageFile, 'rb') as image:
    #    response = client.detect_labels(Image={'Bytes': image.read()})


    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])

    print("Entro en Funcion FaceDetail")
    for faceDetail in response['FaceDetails']:

        #  print(json.dumps(faceDetail, indent=4, sort_keys=True))
        maximo = 0
        index_max = 0
        i = 0
        for i in range(0, 7):
            if faceDetail['Emotions'][i]['Confidence'] > maximo:
               maximo = faceDetail['Emotions'][i]['Confidence']
               index_max = i
        #print(maximo, index_max)


        if faceDetail['Emotions'][index_max]['Type'] == "HAPPY": emosion = " felicidad "
        if faceDetail['Emotions'][index_max]['Type'] == "SAD": emosion = " tristesa "
        if faceDetail['Emotions'][index_max]['Type'] == "ANGRY": emosion = " no estas muy feliz "
        if faceDetail['Emotions'][index_max]['Type'] == "CONFUSED": emosion = " confucion "
        if faceDetail['Emotions'][index_max]['Type'] == "SURPRISED": emosion = " sorpresa "
        if faceDetail['Emotions'][index_max]['Type'] == "CALM": emosion = " calma "
        if faceDetail['Emotions'][index_max]['Type'] == "UNKNOW": emosion = " indiferencia "
       
        if faceDetail['Gender']['Value'] == "Male": sexo = " un chico "
        elif  faceDetail['Gender']['Value'] == "Female": sexo = " una chica "
     
        if faceDetail['Smile']['Value'] == True: sonrisa = ", estas sonrriendo "
        elif faceDetail['Smile']['Value'] == False: sonrisa = ", no estas sonrriendo "

        if faceDetail['Eyeglasses']['Value'] == True: gafas = ", veo que llevas gafas "
        elif faceDetail['Eyeglasses']['Value'] == False: gafas = ", veo que no llevas gafas "

        if faceDetail['EyesOpen']['Value'] == True: ojos = " , tienes los ojos bien abiertos "
        elif faceDetail['EyesOpen']['Value'] == False: ojos = ",  no tienes los ojos muy abiertos "

        if faceDetail['MouthOpen']['Value'] == True: boca = " , tienes la boca un poco abierta "
        elif faceDetail['MouthOpen']['Value'] == False: boca = ",  tienes la boca cerrada "

  

        frase = "   Hola,  veo que eres " + sexo + "de entre " + str(faceDetail['AgeRange']['Low']) + " y " + str(faceDetail['AgeRange']['High']) + " de edad, "
        frase = frase + ", ademas veo que tu expresion es de " + emosion + ", " + boca + ", " + sonrisa + ", " + ojos + ", " + gafas + " " 

        #print (frase)
    return frase

#-----------------------------------------------------------------------------
def BuscaEnBd(face_id):  # recive como parametro un  FaceId y los busca en la base de datos y despliega los datos
              dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
              table = dynamodb.Table('rekognition')
              nombre = "Desconocido o no encontro ningun rostro en la base de datos  .."
              print("GetItem succeeded:")
              try:
                     response = table.query(KeyConditionExpression=Key('FaceId').eq(face_id))
              except ClientError as e:
                     print(e.response['Error']['Message'])
              else:
                     for i in response['Items']:
                        print(i['FaceId'], ":", i['nombre'])
                        nombre=i['nombre']
              face_id=""
              return nombre


#-------------------------------------------------------------------------
# SearchFacesByImage: recive como parametro un fichero, detecta el rostro y busca la imagen en mycollection.
def SearchFacesByImage(fileName):          # https://docs.aws.amazon.com/es_es/rekognition/latest/dg/search-face-with-image-procedure.html
    threshold = 70
    maxFaces=2
#    s3 = boto3.resource('s3')
 #   bucket = s3.Bucket('leogamboa-bucket2')
    bucket='leogamboa-bucket2'
    collectionId='MyCollection'
    face_id=0
    porcentaje=0
    client=boto3.client('rekognition')
    try:
	    response=client.search_faces_by_image(CollectionId=collectionId,
                               Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                               FaceMatchThreshold=threshold,
                               MaxFaces=maxFaces)
    except ClientError as e:
            print(e.response['Error']['Message'])
    else:
            faceMatches=response['FaceMatches']
            print("Inicio funcion faceMatch")
            for match in faceMatches:
                face_id=match['Face']['FaceId']
                print ('face_id:' + face_id + "/")
                print ('FaceId:' + match['Face']['FaceId'])
                print ('ImageId:' + match['Face']['ImageId'])
                print ('ExternalImageId:' + match['Face']['ExternalImageId'])
                porcentaje="{:.2f}".format(match['Similarity'])
                print(porcentaje)
                print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                print("Fin Función FaceMatch, retorna face_id: " + face_id )	
    return face_id, porcentaje
		
#----------------------------------------------------------------------
def upload_file_s3(origen, destino): # recive como arametro la ruta y fichero origen y nombre  con que se quedara en el S3
    s3 = boto3.resource('s3')
    bucket='leogamboa-bucket2'
    s3.Bucket(bucket).upload_file(origen, destino)

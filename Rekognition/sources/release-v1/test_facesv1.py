import boto3
#import json
import functions_rekognition

if __name__ == "__main__":

    photo='leomessi2.jpg'

    texto=functions_rekognition.DetectFaces(photo)
    print('Caracteristicas de tu rostro:' + texto)    
    nombre=functions_rekognition.SearchFacesByImage(photo)
    print('y tu nombre es: :' + nombre)
    functions_rekognition.Play_Polly (texto + " " + nombre) 




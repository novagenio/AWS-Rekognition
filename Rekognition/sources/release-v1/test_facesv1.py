
import boto3
import functions_rekognitionv2

from time import time

if __name__ == "__main__":

    photo='leomesi.jpg'
    start_time = time()
    functions_rekognitionv2.upload_file_s3(photo,photo)
    elapsed_time = time() - start_time
    print("Elapsed time S3: %0.10f seconds." % elapsed_time)

    texto=functions_rekognitionv2.DetectFaces(photo)
#    print('Caracteristicas de tu rostro:' + texto)
    face_id, porcentaje=functions_rekognitionv2.SearchFacesByImage(photo)
    elapsed_time = time() - start_time
    print("Elapsed time Search Face: %0.10f seconds." % elapsed_time)

    nombre=functions_rekognitionv2.BuscaEnBd(face_id) # despliega los datos del rostro, encontrado.
    print("El nombre encintrado es: " + nombre)
    elapsed_time = time() - start_time
    print("Elapsed time Dinamo: %0.10f seconds." % elapsed_time)
 
    print('y tu nombre es: :' + nombre)
    functions_rekognitionv2.Play_Polly ( texto + " y tu nombre es " + nombre) 




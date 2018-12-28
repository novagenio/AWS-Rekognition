import boto3
import json
from boto3 import  client
from io import StringIO
from playsound import playsound
from contextlib import closing
if __name__ == "__main__":
    def checkPicture():
            Text = "Hola mundo")
            return Text 

polly = client("polly", "eu-west-1" )
response = polly.synthesize_speech( Text=checkPicture(), OutputFormat="mp3", VoiceId="Conchita")
if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        data = stream.read()
        fo = open("/home/pi/proyectos/test.mp3", "wb")
        fo.write( data )
        fo.close()
        playsound('/home/pi/proyectos/test.mp3')



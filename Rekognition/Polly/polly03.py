"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir



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


texto = "hola Paulina, veo que estas jugando con tu perro,, se llama Sara?,,, pero,,, que hace tu hija?"
Play_Polly(texto)

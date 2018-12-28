"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="adminuser")
polly = session.client("polly")

try:
    # Request speech synthesis
    response = polly.synthesize_speech(Text=" El partido entre dos equipos argentinos que los argentinos no pudieron organizar, y para el que solo encontraron la solución de que no se jugara en su territorio, aterrizó este jueves por la tarde en Madrid, cuando el presidente del Gobierno, Pedro Sánchez, anunció a través de su cuenta de Twitter, mientras volaba a Buenos Aires a la cumbre del G20: “España está dispuesta a organizar la final de la Copa Libertadores entre Boca y River”. Apenas una hora después, Alejandro Domínguez, presidente de la Conmebol, organizadora del torneo, oficializó que el encuentro se disputará el próximo domingo 9 de diciembre en el Santiago Bernabéu a las 20.30.", OutputFormat="mp3",
                                        VoiceId="Conchita")
except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)

# Access the audio stream from the response
if "AudioStream" in response:
    # Note: Closing the stream is important as the service throttles on the
    # number of parallel connections. Here we are using contextlib.closing to
    # ensure the close method of the stream object will be called automatically
    # at the end of the with statement's scope.
    with closing(response["AudioStream"]) as stream:
        output = os.path.join(gettempdir(), "speech.mp3")

        try:
            # Open a file for writing the output as a binary stream
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            # Could not write to file, exit gracefully
            print(error)
            sys.exit(-1)

else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)

# Play the audio using the platform's default player
if sys.platform == "win32":
    os.startfile(output)
else:
    # the following works on Mac and Linux. (Darwin = mac, xdg-open = linux).
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output])



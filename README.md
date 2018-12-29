Proyecto REKOGNITION 

Amazon Rekognition permite añadir fácilmente el análisis de imagen y vídeo en sus aplicaciones. Proporcione una imagen o vídeo al API Rekognition y el servicio puede identificar objetos, personas, texto, escenas y actividades. 

 

1.- Instalar RaspBerry: 

https://www.raspberrypi.org/downloads/raspberry-pi-desktop/ 

https://etcher.io/ 

 

2.- Instalar AWC CLI Consola y API (SDK PYTHON) 

    Antes habrá que instalar el pip si es que no esta. 

    sudo apt install python3-pip 

    https://docs.aws.amazon.com/es_es/rekognition/latest/dg/setup-awscli-sdk.html 

    https://docs.aws.amazon.com/es_es/cli/latest/userguide/installing.htm 

    Ahora instalar el AWC CLI 

    $ pip3 install awscli --upgrade –user 

    Posteriormente hay que incluir el export PATH=~/.local/bin:$PATH 

    ... ver en (si no... no funciona). 

     (https://docs.aws.amazon.com/es_es/cli/latest/userguide/awscli-install-linux.html#awscli-install-linux-path ) 

         nano .profile    (bajo la ruta usuario) 

         ubuntu@ip-172-31-25-169:~$ pwd 

         /home/ubuntu  (o /home/pi para RaspBerry)


    Ahora AWS SDK Python BOTO 

    https://aws.amazon.com/es/sdk-for-python/ 
     
         pip3 install boto3


Ficheros Credenciales y config de AWS CLI (respecto al usuario creado en IAM) y son las actuales credenciales que utilizo.  

Primero, para la creación de los ficheros: ejecutar 

$ aws configure 

Y poner los valores de cada campo abajo. 

  ~/.aws/credentials 

  [default] 

  aws_access_key_id = AKIAJTBI6ERJXLNZ7CLQ 

  aws_secret_access_key = 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 

 

~/.aws/config 

  [default] 

  region = us-west-2 (actualmente cambiado a eu-west-1) 

  output = text 

 

4.- Configurar (leogamboa02@outlook.com, Superleo01.) 

Amazon Rekognition 

Amazon S3  

mi bucket creado:  

  leogamboa-bucket2 eu-west-1 

 

AIM Management Console 

Usuario01, usuario02, clave: Superleo01.  

   aws_access_key_id = AKIAJTBI6ERJXLNZ7CLQ 

   aws_secret_access_key = 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 

 

 

5.- Conexión EC2 - AWS Linux 

Maquina: ec2-54-71-0-32.us-west-2.compute.amazonaws.com 

Archivo claves PKLeo.ppk, PKLeo.ppk, en Archivos/Proyecto Rekognition/archivo configuración (drive) 

 

Windows 

Public DNS 

ec2-35-163-174-224.us-west-2.compute.amazonaws.com 

User name 

Administrator 

Password 

RIo5Zp&J4=Yamxv7wvOjmTjOV9XCqj@L 

 

 

 

5.- Instalar  Inotify (watchDog) 

https://pypi.org/project/inotify/ 

 

6.- Trabajar con ficheros S3 AWS, desde Python 

https://github.com/smore-inc/tinys3 

7.- DynamoDB (eu-west-1 zona Irlanda) 

 

8.-Codigos de zona AWS 

Code 

Nombre 

us-east-1 

US East (N. Virginia) 

us-east-2 

EE.UU. Este (Ohio) 

us-west-1 

EE.UU. Oeste (Norte de California) 

us-west-2 

EE.UU. Oeste (Oregón) 

ca-central-1 

Canadá (Central) 

eu-central-1 

UE (Fráncfort) 

eu-west-1 

UE (Irlanda) 

eu-west-2 

UE (Londres) 

eu-west-3 

UE (París) 

ap-northeast-1 

Asia Pacífico (Tokio) 

ap-northeast-2 

Asia Pacífico (Seúl) 

ap-northeast-3 

Asia Pacífico (Osaka-local) 

ap-southeast-1 

Asia Pacífico (Singapur) 

ap-southeast-2 

Asia Pacífico (Sídney) 

ap-south-1 

Asia Pacífico (Mumbai) 

sa-east-1 

América del Sur (São Paulo) 

Salto de página
 

Plan de proyecto: 

1.- instalación entornos base: OK 

2.- Instalación componentes AWS CLI. OK 

3.- Instalación BOTO. OK 

4.- Programas 

: Macros start_img.py: Modulo que sube fichero imágenes a S3, a partir del watch-dog 

Incluir a start_img, la funcionalidad de subr la imagen desde S3 a la colección 

Incluir al módulo start_img, la funcionalidad de guardar los identificadores a DynamoDb 

 

 

5.- Instalar  Inotify (watchDog) 

https://pypi.org/project/inotify/ 

Ejemplo: 

import inotify.adapters 

import os 

  

notifier = inotify.adapters.Inotify() 

notifier.add_watch('/home/ubuntu/proyectos/media') 

  

for event in notifier.event_gen(): 

    if event is not None: 

        # print event      # uncomment to see all events generated 

#        IN_CLOSE_WRITE 

        if 'IN_CREATE' in event[1]: 

              print("{0}".format(event[3])) 

#             print "file '{0}' created in '{1}'".format(event[3], event[2]) 

#             os.system("your_python_script_here.py") 

              cadena="{0}".format(event[3]) 

              print(cadena) 

#              os.system("sudo rm " + "/tmp/"+cadena) 

 

 

 

 

 

 

 

 

OPENCV> 

pip3 install opencv-python 

sudo apt-get install libatlas-base-dev 

sudo apt-get install libjasper-dev 

sudo apt-get install libqtgui4 

sudo apt-get install python3-pyqt5 

sudo apt install libqt4-test 

sudo apt-get install linux-generic-lts-utopic 

 

cd ~/<my_working_directory> 

git clone https://github.com/opencv/opencv.git 

git clone https://github.com/opencv/opencv_contrib.git 

 

 

Activar camara 

sudo modprobe bcm2835-v4l2 

 

GPU memory is not set at 128 MB or greater. Run sudo raspi-config and adjust it to 128 using the menu. *reiniciar( 

Poner camara usb 

 

AttributeError: 'module' object has no attribute 'createFisherFaceRecognizer' 

pip3 install opencv-contrib-python 

ImportError: libhdf5_serial.so.100: cannot open shared object file: No such file or directory 

sudo apt-get update 
sudo apt-get install libhdf5-dev 
sudo apt-get update 
sudo apt-get install libhdf5-serial-dev 

 

VIDEOIO ERROR: V4L: can't open camera by index 0 

Warning: unable to open video source:  0 

Solución: sudo modprobe bcm2835-v4l2 

 

AWS POLLY. 

Incluir en el  

nano ~/.aws/config 

[profile adminuser] 

aws_access_key_id = AKIAJTBI6ERJXLNZ7CLQ 

aws_secret_access_key = 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 

region = eu-west-1 

 

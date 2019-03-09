import os


saludo = "Hola, Novagenio te ha identificado como "
nombre = saludo + "Leonardo Gamboa"
comando="raspistill -p '112, 40,575,400' --vflip -w 1920 -h 1440 -ae 32,0xff,0x808000 -a " + "'" + nombre + "'"
print(comando)
os.system(comando)

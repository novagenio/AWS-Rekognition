Instalar RPI Cam Web 

https://elinux.org/RPi-Cam-Web-Interface#Basic_Installation 

La configuración de las opciones se encuentra en /etc/raspimjpeg, que es una imagen del original /RPi_Cam_Web_Interface/etc/raspimjpeg (que no sirve ojo). Leerlo es muy interesante. 

Dentro de /etc/raspimjpeg, comentar la línea, #thumb_gen vit, o generara ficheros _tm_ 

      # thumb generator control 

      # Set v, i, or t in string to enable thumbs for images, videos, or lapse 

      #thumb_gen vit 

En el apartado #file location, se encuentra la definición y ubicación entre otras cosas, de las imágenes y las macros. Aquí ej. De las imágenes. 

      image_path /var/www/html/media/im_%i_%Y%M%D_%h%m%s.jpg 

Y rotation para hacer que la camara rote 180 o n grados. 

'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

import boto3
import functions_rekognitionv2



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '70dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '70dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        photo="IMG_{}.png".format(timestr)
        print("Captured " + photo)
        ##
        functions_rekognitionv2.upload_file_s3(photo,photo)
        print("s3 ")
        face_id=functions_rekognitionv2.SearchFacesByImage(photo)
        print("face ")
        nombre=functions_rekognitionv2.BuscaEnBd(face_id) 
        print("El nombre encintrado es: " + nombre)
        ##

class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()

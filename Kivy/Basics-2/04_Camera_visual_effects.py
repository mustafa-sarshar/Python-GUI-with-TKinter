'''
Source: https://kivy.org/doc/stable/examples/gen__camera__main__py.html
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

from cmath import pi
from hashlib import sha1
from turtle import shape
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import time
import numpy as np

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        # camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

        height, width = camera.texture.height, camera.texture.width
        camera_pixels = np.frombuffer(camera.texture.pixels, np.uint8)
        camera_pixels = camera_pixels.reshape(height, width, 4)
        print(camera_pixels)
        # camera.texture = camera_pixels

class TestCamera(App):

    flag_transform_image = False
    def build(self):
        # Init Layout
        layout = BoxLayout(orientation="vertical")

        # Add Widgets
        self.camera = Camera(play=True, resolution=(640, 480))
        layout.add_widget(self.camera)

        self.img_camera_transform = Image()
        layout.add_widget(self.img_camera_transform)

        self.btn_freeze_camera = ToggleButton(
            text="Freeze Camera", size_hint_y=None, height="48dp",
            on_press=self.btn_freeze_camera_pressed
        )
        layout.add_widget(self.btn_freeze_camera)

        self.btn_transform_image = ToggleButton(
            text="Transform Image", size_hint_y=None, height="48dp",
            on_press=self.btn_transform_image_pressed
        )
        layout.add_widget(self.btn_transform_image)
        self.trigger_interval = Clock.schedule_interval(self.transform_image, 1./30.)
        return layout

    def btn_freeze_camera_pressed(self, *args):
        self.camera.play = not self.camera.play

    def btn_transform_image_pressed(self, *args):
        self.flag_transform_image = not self.flag_transform_image

    def transform_image(self, *args):
        if self.flag_transform_image:
            height, width = self.camera.texture.height, self.camera.texture.width
            pixels = np.frombuffer(self.camera.texture.pixels, np.uint8).reshape(height, width, 4)
            pixels = np.flip(pixels, axis=0)    # Flip Vertically
            pixels = np.flip(pixels, axis=1)    # Flip Horizontally
            # pixels = pixels * 2                 # Add effects
            pixels = pixels.tobytes()
            texture = Texture.create(size=(width, height), colorfmt="rgba")
            texture.blit_buffer(pixels, bufferfmt="ubyte", colorfmt="rgba")
            self.img_camera_transform.texture = texture

TestCamera().run()
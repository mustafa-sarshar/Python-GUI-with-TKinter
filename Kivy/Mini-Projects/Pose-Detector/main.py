"""
Source: https://www.youtube.com/watch?v=PwUWtfk2inQ&ab_channel=CZDe
"""
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2, time

class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation="vertical")
        self.image = Image()
        layout.add_widget(self.image)
        self.btn_save_image = Button(
            text="Save Image",
            pos_hint={"center_x": .5, "center_y": .5},
            size_hint= (None, None)
        )
        self.btn_save_image.bind(on_press=self.save_image)
        layout.add_widget(self.btn_save_image)
        self.capture = cv2.VideoCapture(0)
        Clock.create_trigger(self.load_video, 1./30.)
        return layout

    def load_video(self, *args):
        res, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tostring()
        print(buffer)
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="bgr")
        texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
        self.image.texture = texture

    def save_image(self, *args):
        print("save image")
        timestr = time.strftime("%Y%m%d_%H%M%S")
        cv2.imwrite("data/images/IMG_{}.png".format(timestr), self.image_frame)
        
if __name__ == "__main__":
    MainApp().run()
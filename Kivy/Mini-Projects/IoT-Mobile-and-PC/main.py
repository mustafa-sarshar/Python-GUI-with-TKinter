# Source: https://www.youtube.com/watch?v=uv8PciALzSI&t=70s&ab_channel=ErikSandberg

import socket, time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import random
# from pyobjus import autoclass

class Client(App):
    server_IP = "127.0.1.1"
    server_port = 65436
    counter = 0
    def build(self):
        self.data = random.random() * 10 + 10

        # ip found using socket.gethostbyname(socket.gethostname()) on the server # in my case server-IP = 127.0.1.1
        # design layout
        layout = GridLayout(cols=1)
        btn_go = Button(on_release=self.go)
        self.lbl = Label()
        self.txt_host = TextInput(text=self.server_IP)
        layout.add_widget(btn_go)
        layout.add_widget(self.txt_host)
        layout.add_widget(self.lbl)
        return layout

    def go(self, *args):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_IP, self.server_port))

        while True:
            time.sleep(.25)
            self.send_msg()

    def send_msg(self, *args):
        self.socket.sendall(str(self.data))
        self.counter += 1
        self.data = random.random() * 10 + 10

    def on_stop(self):
        self.socket.close()

Client().run()
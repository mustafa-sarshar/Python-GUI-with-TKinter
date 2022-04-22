import imp
from logging import root
# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
import time

class WidgetsExample(GridLayout):
    n_clicked = 0
    my_text = StringProperty("Hello!")
    def on_button_click(self):
        self.n_clicked += 1
        self.my_text = f"Clicked for {self.n_clicked} time(s)!"


class TheLabApp(App):
    pass

if __name__ == "__main__":
    TheLabApp().run()
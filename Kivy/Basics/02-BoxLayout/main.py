# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
    
from kivy.uix.button import Button

class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn_1 = Button(text="BTN 1")
        btn_2 = Button(text="BTN 2")
        btn_3 = Button(text="BTN 3")
        self.add_widget(btn_1)
        self.add_widget(btn_2)
        self.add_widget(btn_3)
        self.orientation = "vertical"

class TheLabApp(App):
    pass

TheLabApp().run()
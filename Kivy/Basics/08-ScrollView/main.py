# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.app import App
# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.metrics import dp
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 1000):
            scaler = i/100
            size = dp(30+scaler)
            if (i % 2 == 0):
                widget = Button(text=str(i), size_hint=(None, None), size=(size, size))
            else:
                widget = Label(text=str(i), size_hint=(None, None), size=(size, size))
            self.add_widget(widget)
        self.orientation = "lr-tb"
        self.padding = (dp(20)) # left, top, right, bottom
        self.spacing = (dp(20)) # horizontally, vertically

class TheLabApp(App):
    pass

TheLabApp().run()
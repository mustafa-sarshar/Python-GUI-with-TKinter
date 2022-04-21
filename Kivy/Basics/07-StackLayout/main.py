# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 11):
            btn = Button(text=f"BTN {i}", size_hint=(.2, .2))
            self.add_widget(btn)
        for i in range(1, 11):
            btn = Button(text=f"{i} fixed", size_hint=(None, None), size=(dp(i+100), dp(i+30)))
            self.add_widget(btn)
        self.orientation = "rl-bt"
        self.padding = (dp(20)) # left, top, right, bottom
        self.spacing = (dp(20)) # horizontally, vertically

class TheLabApp(App):
    pass

TheLabApp().run()
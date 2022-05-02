from ast import arg
import os
os.environ["KIVY_TEXT"] = "pil" # in order to restrict text rendering to the PIL implementation
# os.environ["KIVY_NO_ARGS"] = "1"

from kivy.config import Config
Config.set("graphics", "width", "500")
Config.set("graphics", "height", "100")
Config.set("graphics", "borderless", "true") # equal to Config.set('graphics', 'fullscreen', 'fake')


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label())
        self.submit = Button(text="Submit", on_press=self.submit_on_press, on_release=self.submit_on_release)
        self.add_widget(self.submit)
        self.event = None

    def submit_on_press(self, event):
        if self.event == None:
            self.event = Clock.schedule_interval(self.print_credentials, 1/30.)

    def submit_on_release(self, event):
        if self.event:
            self.event.cancel() # equal to Clock.unschedule(event)
            self.event = None

    def print_credentials(self, dt):
        print(f"dt: {dt:.2f}", "Username:", self.username.text, ", Password:", self.password.text)

class MyApp(App):
    def build(self):
        return LoginScreen()
    
if __name__ == "__main__":
    MyApp().run()
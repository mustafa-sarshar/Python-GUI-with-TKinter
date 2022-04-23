# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

class WidgetsExample(GridLayout):
    n_clicked = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("Hello!")

    def on_button_click(self):
        if self.count_enabled:
            self.n_clicked += 1
            self.my_text = f"Clicked for {self.n_clicked} time(s)!"

    def on_switch_active(self, widget):
        if widget.active:
            self.count_enabled = True
        else:
            self.count_enabled = False
        message = f"Switch is {widget.active}"
        print(message)

class TheLabApp(App):
    pass

if __name__ == "__main__":
    TheLabApp().run()
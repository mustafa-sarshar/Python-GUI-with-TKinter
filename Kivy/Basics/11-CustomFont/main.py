from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

class WidgetsExample(GridLayout):
    n_clicked = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("Hello!")

    def on_button_click(self):
        self.n_clicked += 1
        self.my_text = f"Clicked\n{self.n_clicked} time(s)!"

    def on_toggle_button_state(self, widget):
        message = f"Toggle button\nis now\n{widget.state}"
        print(message)
        if (widget.state == "normal"):
            widget.text = "OFF"
            self.count_enabled = False    
        else:
            widget.text = "ON"
            self.count_enabled = True

class TheLabApp(App):
    pass

if __name__ == "__main__":
    TheLabApp().run()
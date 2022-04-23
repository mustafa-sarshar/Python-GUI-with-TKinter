# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

# Builder.load_file("kivy.kv") # Not necessary

class CanvasExample(Widget):
    inc_x = dp(100)
    inc_y = dp(10)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(1, 0, 0)
            self.circle = Line(circle=(dp(300), dp(100), dp(50)), width=3), # X_C, y_C, Radius
            print(self.circle)
            Color(0, 1, 0, .3)
            self.rect = Line(rectangle=(dp(400), dp(100), dp(150), dp(30)), width=3) # X, Y, W, H
            Color(0, 0, 1, .4)
            self.rect_filled = Rectangle(pos=(dp(10), dp(200)), size=(dp(50), dp(50)))
            Color(0, 0, 1, .4)
            self.ellipse_filled = Ellipse(pos=(dp(500), dp(10)), size=(dp(50), dp(50)))
    def on_button_move_press(self):        
        win_w, win_h = self.width, self.height
        self.update_widget_pos(widget=self.rect_filled, win_w=win_w, win_h=win_h)
        self.update_widget_pos(widget=self.ellipse_filled, win_w=win_w, win_h=win_h)
    
    def update_widget_pos(self, widget, win_w, win_h):
        pos_x, pos_y = widget.pos
        size_w, size_h = widget.size
        if (pos_x+size_w) > win_w:
            self.inc_x = dp(-100)
            print("more")
        elif (pos_x) < 0:
            self.inc_x = dp(100)
            print("less")
        if (pos_y+size_h) > win_h:
            self.inc_y = dp(-10)
            print("more")
        elif (pos_y) < 0:
            self.inc_y = dp(10)
            print("less")
        widget.pos = dp(pos_x+self.inc_x), dp(pos_y+self.inc_y)

class KivyApp(App):
    pass

if __name__ == "__main__":
    app = KivyApp()
    app.run()
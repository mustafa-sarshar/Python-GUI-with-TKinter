# Source: // https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.properties import Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse

class CanvasMain(Widget):
    ball_vx = dp(10)
    ball_vy = dp(10)
    game_speed = 0.00001 # frames per second
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update_ball_pos, self.game_speed)

    def on_size(self, *args):
        self.ball.pos = dp(self.width/2-self.ball.size[0]/2), dp(self.height/2-self.ball.size[1]/2)

    def update_ball_pos(self, delta_time):
        print("update", delta_time)
        ball_x, ball_y = self.ball.pos
        ball_w, ball_h = self.ball.size

        if (ball_x+ball_w) >= self.width:
            ball_x = self.width - ball_w
            self.ball_vx = -self.ball_vx
        elif ball_x <= 0:
            ball_x = 0
            self.ball_vx = -self.ball_vx

        if (ball_y+ball_h) >= self.height:
            ball_y = self.height - ball_h
            self.ball_vy = -self.ball_vy
        elif ball_y <= 0:
            ball_y = 0
            self.ball_vy = -self.ball_vy

        self.ball.pos = dp(ball_x+self.ball_vx), dp(ball_y+self.ball_vy)
        

class KivyApp(App):
    pass

if __name__ == "__main__":
    app = KivyApp()
    app.run()
# Source (accessed on 23.04.22):
# 1. https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3589s&ab_channel=freeCodeCamp.org
# 2. https://stackoverflow.com/questions/14014955/kivy-how-to-change-window-size
# 3. https://stackoverflow.com/questions/17280341/how-do-you-check-for-keyboard-events-with-kivy

from kivy.config import Config
Config.set("graphics", "width", "900")
Config.set("graphics", "height", "400")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import Clock, NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Quad
from kivy.core.window import Window
from kivy import platform

class MainWidget(Widget):
    from transforms import transform, transform_perspective_attraction_based, transform_2D, transform_perspective
    from user_actions import keyboard_closed, on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up

    TIME_FACTOR = 60.0
    APP_REFRESH_RATE = 1.0/TIME_FACTOR
    
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    NUM_V_LINES = 4
    SPACING_V_LINES = .1 # a percentage of the screen's width
    vertical_lines = []

    NUM_H_LINES = 14
    SPACING_H_LINES = .1 # a percentage of the screen's width
    horizontal_lines = []

    GAME_SPEED_Y = 4
    current_offset_y = 0

    GAME_SPEED_X = 12
    current_game_speed_x = 1
    current_offset_x = 0

    tiles = None
    tile_x = 2
    tile_y = 1

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("Init W:", self.width, "H: ", self.height)
        self._init_vertical_lines()
        self._init_horizontal_lines()
        self._init_tiles()

        if self.check_platform() == "Desktop-PC":
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update_app, self.APP_REFRESH_RATE)

    def check_platform(self):
        if platform in ("linux", "win", "macos"):
            return "Desktop-PC"
        else:
            return "Not Desktop-PC"

    def on_parent(self, widget, parent): # is called when MainWidget is assigned to GalaxyApp
        # print(self.width, self.height)
        pass

    def on_size(self, *args):
        # print("On_size, W:", self.width, "H:", self.height)
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height*.75
        # self.update_vertical_lines()
        # self.update_horizontal_lines()
        pass

    def on_perspective_point_x(self, widget, value):
        # print("Px:", value)
        pass

    def on_perspective_point_y(self, widget, value):
        # print("Py:", value)
        pass

    def _init_tiles(self):
        with self.canvas:
            Color(1, 1, 1, 1)
            self.tiles = Quad()

    def _init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1, 1)
            for _ in range(self.NUM_V_LINES):
                self.vertical_lines.append(Line())

    def _init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1, 1)
            for _ in range(self.NUM_H_LINES):
                self.horizontal_lines.append(Line())

    def get_line_x_from_index(self, index):
        central_line_x = self.perspective_point_x
        spacing = self.SPACING_V_LINES * self.width
        offset_x = index - .5
        return central_line_x - offset_x * spacing + self.current_offset_x # return line_x

    def get_line_y_from_index(self, index):
        spacing_y = self.SPACING_H_LINES * self.height
        return index * spacing_y - self.current_offset_y # return line_y

    def get_tile_coordinates(self, tile_x, tile_y):
        x = self.get_line_x_from_index(tile_x)
        y = self.get_line_y_from_index(tile_y)
        return x, y

    def update_tiles(self):
        x_min, y_min = self.get_tile_coordinates(self.tile_x, self.tile_y)
        x_max, y_max = self.get_tile_coordinates(self.tile_x+1, self.tile_y+1)
    
        x1, y1 = self.transform(x_min, y_min)
        x2, y2 = self.transform(x_min, y_max)
        x3, y3 = self.transform(x_max, y_max)
        x4, y4 = self.transform(x_max, y_min)
        
        self.tiles.points = [x1, y1, x2, y2, x3, y3, x4, y4]

    def update_vertical_lines(self):
        # central_line_x = int(self.width/2)
        # spacing = self.SPACING_V_LINES * self.width
        # offset_x = -int(self.NUM_V_LINES/2) + .5 # to scale and shift the lanes to the right
        start_index = -int(self.NUM_V_LINES/2) + 1
        for i in range(start_index, start_index+self.NUM_V_LINES):
            # line_x = central_line_x + offset_x * spacing + self.current_offset_x
            line_x = self.get_line_x_from_index(i)
            pos_x1, pos_y1 = self.transform(line_x, 0)
            pos_x2, pos_y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [pos_x1, pos_y1, pos_x2, pos_y2]
            # offset_x += 1

    def update_horizontal_lines(self):
        # central_line_x = int(self.width/2)
        # spacing_X = self.SPACING_V_LINES * self.width
        # offset_x = int(self.NUM_V_LINES/2) - .5 # to scale and shift the lanes to the right

        # x_min = central_line_x - offset_x * spacing_X + self.current_offset_x
        # x_max = central_line_x + offset_x * spacing_X + self.current_offset_x
        start_index = -int(self.NUM_V_LINES/2) + 1
        end_index = start_index + self.NUM_V_LINES - 1

        x_min = self.get_line_x_from_index(start_index)
        x_max = self.get_line_x_from_index(end_index)
        # spacing_y = self.SPACING_H_LINES * self.height
        for i in range(self.NUM_H_LINES):
            # line_y = i*spacing_y - self.current_offset_y
            line_y = self.get_line_x_from_index(i)
            pos_x1, pos_y1 = self.transform(x_min, line_y)
            pos_x2, pos_y2 = self.transform(x_max, line_y)
            self.horizontal_lines[i].points = [pos_x1, pos_y1, pos_x2, pos_y2]

    def update_path(self, dt):
        time_factor = dt*self.TIME_FACTOR # to have a consistant game speed on any device independent of the spped of the device

        self.current_offset_y += self.GAME_SPEED_Y * time_factor
        spacing_y = self.SPACING_H_LINES * self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y

        self.current_offset_x += self.current_game_speed_x * time_factor 

    def update_app(self, delta_time):
        # print(delta_time)
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        self.update_path(dt=delta_time)

class GalaxyApp(App):
    pass

if __name__ == "__main__":
    app = GalaxyApp()
    app.run()
    
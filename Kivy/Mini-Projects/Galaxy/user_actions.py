def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_down=self.on_keyboard_up)
    self._keyboard = None

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == "left":
        self.current_game_speed_x = self.GAME_SPEED_X
    elif keycode[1] == "right":
        self.current_game_speed_x = -self.GAME_SPEED_X

def on_keyboard_up(self, keyboard, keycode):
    self.current_game_speed_x = 0

def on_touch_down(self, touch):
    if touch.x > self.width/2:
        self.current_game_speed_x = self.GAME_SPEED_X
    else:
        self.current_game_speed_x = -self.GAME_SPEED_X
    # return super().on_touch_down(touch)

def on_touch_up(self, touch):
    self.current_game_speed_x = 0
    # return super().on_touch_up(touch)

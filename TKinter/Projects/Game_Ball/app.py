# In[] Libs
import sys, os, math
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import winsound

# In[] Inits
app_path = os.path.abspath(os.path.dirname(__file__))

# In[] Layouts
class App(tk.Tk):
    FRM_PADDING = (10, 10, 10, 10)
    BTN_PADDING = (2, 2, 2, 2)
    CANVAS_SIZE = (400, 400)
    CANVAS_BK_COLOR = "#317001"
    FIELD_EDGE = (10, 11, CANVAS_SIZE[0]-9, CANVAS_SIZE[1]-5)
    MOVEMENT_INC = 10
    COLLISION_IMPACT = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wm_title("Game - Ball")

        self.frm_main = ttk.Frame(master=self, padding=self.FRM_PADDING)
        self.frm_main.grid(row=0, column=0, sticky="EWNS")
        self.frm_animation = ttk.Frame(master=self.frm_main, padding=self.FRM_PADDING)
        self.frm_animation.grid(row=0, column=0, sticky="EWNS")

        self.animation_field = tk.Canvas(master=self.frm_animation, background=self.CANVAS_BK_COLOR, width=self.CANVAS_SIZE[0], height=self.CANVAS_SIZE[1])
        self.animation_field.pack()
        self.frm_buttons = ttk.Frame(master=self.frm_main, padding=self.FRM_PADDING)
        self.frm_buttons.grid(row=1, column=0)

        self.grid_columnconfigure(0, weight=1)
        self.frm_main.grid_columnconfigure(0, weight=1)
        self.frm_buttons.grid_columnconfigure((0, 1, 2), weight=1)

        self._init_vars()
        self._init_canvas()
        self._init_buttons()
        self.bind_all("<Key>", func=self.key_pressed)

    def _init_vars(self):
        self.var_position_x = tk.IntVar(self.animation_field, value=100)
        self.var_position_y = tk.IntVar(self.animation_field, value=100)

    def _init_canvas(self):
        self.img = Image.open(os.path.join(app_path, "assets", "ball.png"))
        self.img_ball = ImageTk.PhotoImage(self.img)
        self.animation_field.create_image((self.var_position_x.get(), self.var_position_y.get()), image=self.img_ball, tag="ball")
        self.animation_field.create_rectangle(*self.FIELD_EDGE, outline="yellow")

    def _init_buttons(self):
        self.btn_move_left = ttk.Button(master=self.frm_buttons, text="<", padding=self.BTN_PADDING, command=lambda: self.move_obj(inc_x=-self.MOVEMENT_INC, tag="ball"))
        self.btn_move_left.grid(row=1, column=0, sticky="EW")
        self.btn_move_right = ttk.Button(master=self.frm_buttons, text=">", padding=self.BTN_PADDING, command=lambda: self.move_obj(inc_x=self.MOVEMENT_INC, tag="ball"))
        self.btn_move_right.grid(row=1, column=2, sticky="EW")
        self.btn_move_up = ttk.Button(master=self.frm_buttons, text="^", padding=self.BTN_PADDING, command=lambda: self.move_obj(inc_y=-self.MOVEMENT_INC, tag="ball"))
        self.btn_move_up.grid(row=0, column=1, sticky="EW")
        self.btn_move_down = ttk.Button(master=self.frm_buttons, text="v", padding=self.BTN_PADDING, command=lambda: self.move_obj(inc_y=self.MOVEMENT_INC, tag="ball"))
        self.btn_move_down.grid(row=2, column=1, sticky="EW")
    
    def move_obj(self, inc_x:int=0, inc_y:int=0, tag:str=""):        
        obj = self.animation_field.find_withtag(tag)
        x = self.var_position_x.get() + inc_x
        y = self.var_position_y.get() + inc_y
        x, y = self.check_collision(x, y)
        self.animation_field.coords(obj, (x, y))
        self.var_position_x.set(x)
        self.var_position_y.set(y)
        self.check_collision(x, y)

    def rotate_obj(self, points, angle, center):
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        return new_points

    def key_pressed(self, e):
        if e.keysym == "Up":
            self.move_obj(inc_y=-self.MOVEMENT_INC, tag="ball")
        elif e.keysym == "Down":
            self.move_obj(inc_y=self.MOVEMENT_INC, tag="ball")
        elif e.keysym == "Left":
            self.move_obj(inc_x=-self.MOVEMENT_INC, tag="ball")
        elif e.keysym == "Right":
            self.move_obj(inc_x=self.MOVEMENT_INC, tag="ball")
        else: print(e)

    def check_collision(self, x, y):
        print(x, y)
        # Check collision for X
        if x <= self.FIELD_EDGE[0]: x = x+self.COLLISION_IMPACT
        elif x >= self.FIELD_EDGE[2]: x = x-self.COLLISION_IMPACT
        # # Check collision for y
        if y <= self.FIELD_EDGE[1]: y = y+self.COLLISION_IMPACT
        elif y >= self.FIELD_EDGE[3]: y = y-self.COLLISION_IMPACT
        return x, y

# In[] App
if __name__ == "__main__":
    app = App()
    app.mainloop()
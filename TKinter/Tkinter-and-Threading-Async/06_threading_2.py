# Source: https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
# Run tkinter code in another thread

import tkinter as tk
from tkinter import  ttk, messagebox
import threading

class AppTkinter(tk.Tk):
    def __init__(self, app_name="App Name", window_size=(300, 300), window_pos=(50, 50), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_name = app_name
        self.wm_title(app_name)
        self.protocol("WM_DELETE_WINDOW", self.on_closing_tkinter)
        self.geometry(f"{window_size[0]}x{window_size[1]}+{window_pos[0]}+{window_pos[1]}")

        # Add Frames
        frm_main = ttk.Frame(master=self)
        frm_main.pack()

        # Add Widgets to Frames
        self.lbl = ttk.Label(master=frm_main, text="That's COOOOOLLL!!!!")
        self.lbl.pack()

    def on_closing_tkinter(self):
        print(f"Bye bye from {self.app_name}")
        self.quit()

class AppMain(threading.Thread):
    def __init__(self, app_name="App Name", window_size=(300, 300), window_pos=(50, 50)):
        threading.Thread.__init__(self)
        self.app_name = app_name
        self.window_size = window_size
        self.window_pos = window_pos
        self.start()

    def run(self):
        self.app_tkinter = AppTkinter(app_name=self.app_name, window_size=self.window_size, window_pos=self.window_pos)
        self.app_tkinter.mainloop()

if __name__ == "__main__":
    app_main_1 = AppMain(app_name="Tkinter and Threading - App 1")
    app_main_2 = AppMain(app_name="Tkinter and Threading - App 2", window_size=(500, 500), window_pos=(300, 300))
    print('Now we can continue running code while mainloop runs!')
    
    app_tkinter = AppTkinter() # It stops the app till this window is closed
    app_tkinter.mainloop()

    print(app_main_1), print(app_main_2)
    # for i in range(100000):
    #     print(i)
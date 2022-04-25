# In[] Libs
import tkinter as tk
from tkinter import ttk

# In[] Layout
class AppMain(tk.Tk):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wm_title(title)
        self.frames = dict() # Frame holder

        self.container = ttk.Frame(self)
        self.container.grid(padx=10, pady=10, sticky="EW")

        PAGES = (Page_1, )
        for PageClass in PAGES:
            page = PageClass(self.container, self)
            self.frames[PageClass] = page
            page.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(Page_1)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class Page_1(ttk.Frame):
    def __init__(self, container, parent, **kwargs):
        super().__init__(container, **kwargs)

        self.lbl_1 = ttk.Label(master=self, text="A Simple OOP Example")
        self.lbl_1.pack(side=tk.TOP, fill=tk.X, expand=True)

# In[] Run the App
if __name__ == "__main__":
    app_main = AppMain(title="Main App")
    app_main.mainloop()
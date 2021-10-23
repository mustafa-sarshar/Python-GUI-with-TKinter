import tkinter as tk
from tkinter import ttk
from pages import LARGE_FONT
from startPage import StartPage
from page1 import PageOne
from page2 import PageTwo

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Graph Page!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        
        button3 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()
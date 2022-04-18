# Source: https://www.youtube.com/watch?v=QG-KvTZwxfc&ab_channel=TimWebb
import tkinter as tk
from tkinter import ttk
import asyncio, random
from datetime import datetime

def counter(count_til:int):
    for i in range(count_til):
        print(i+1)

def update_gui(e):
    current_time = datetime.now().strftime("%H:%M:%S.%f - %A, %d %B %Y")
    var_time.set(current_time)

window = tk.Tk()
window.wm_title("Asyncio in Tkinter")
window.geometry("300x300")
var_time = tk.StringVar(master=window, value="Time")

btn_counter = ttk.Button(master=window, text="Start the Counter", command=lambda: counter(10))
btn_counter.pack(side="bottom")

lbl_time = ttk.Label(master=window, textvariable=var_time)
lbl_time.pack(side="top")
lbl_time.bind("<Button>", update_gui)


if __name__ == "__main__":
    window.mainloop()

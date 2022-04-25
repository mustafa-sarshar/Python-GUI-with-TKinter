"""
Design a timer with variable speed.
"""
# In[] Libs
import tkinter as tk
import time, threading, sys
from concurrent.futures import ThreadPoolExecutor

# In[] Global Vars & Constants
timer_1_speed = 1
timer_2_speed = 0.01
timer_reaction_time_speed = 0.001

# In[] Functions
def change_timer_1_speed(increase=True):
    global timer_1_speed
    if increase: timer_1_speed += 1
    else: timer_1_speed -= 1
    print(f"Timer 1 Speed: {timer_1_speed}")

def change_timer_2_speed(increase=True):
    global timer_2_speed
    if increase: timer_2_speed += 1
    else: timer_2_speed -= 1
    print(f"Timer 2 Speed: {timer_2_speed}")

def update_timer_1():
    global lbl_timer_1
    while True:
        time.sleep(abs(timer_1_speed))
        lbl_timer_1["text"] = int(lbl_timer_1["text"]) + 1
        if lbl_timer_1["text"] >= 100: lbl_timer_1["text"] = 0

def update_timer_2():
    global lbl_timer_2
    while True:
        time.sleep(abs(timer_2_speed))
        lbl_timer_2["text"] = int(lbl_timer_2["text"]) + 1
        # if lbl_timer_2["text"] >= 100: lbl_timer_2["text"] = 0

def update_timer_reaction_time():
    global lbl_reaction_time
    while True:
        time.sleep(abs(timer_reaction_time_speed))
        lbl_reaction_time["text"] = int(lbl_reaction_time["text"]) + 10

def event_button_1(event):
    global lbl_reaction_time
    print(lbl_reaction_time["text"])
    lbl_reaction_time["text"] = 0
    print(time.process_time_ns())

def on_closing_window():
    global window
    window.destroy()    
    sys.exit("Bye bye!!!")

# In[] Design the Layout
window = tk.Tk()

frm_labels = tk.Frame(master=window, bg="red")
frm_labels.pack(side=tk.TOP, fill=tk.Y)
frm_buttons = tk.Frame(master=window, bg="blue")
frm_buttons.pack(side=tk.TOP, fill=tk.Y)
frm_reaction_time = tk.Frame(master=window)
frm_reaction_time.pack(side=tk.TOP, fill=tk.Y)

btn_timer_1_increase = tk.Button(master=frm_buttons, text="+", command=lambda: change_timer_1_speed(increase=True))
btn_timer_1_decrease = tk.Button(master=frm_buttons, text="-", command=lambda: change_timer_1_speed(increase=False))
btn_timer_2_increase = tk.Button(master=frm_buttons, text="+", command=lambda: change_timer_2_speed(increase=True))
btn_timer_2_decrease = tk.Button(master=frm_buttons, text="-", command=lambda: change_timer_2_speed(increase=False))
lbl_timer_1 = tk.Label(master=frm_labels, text="0")
lbl_timer_2 = tk.Label(master=frm_labels, text="0")
lbl_reaction_time = tk.Label(master=frm_reaction_time, text="0")

btn_timer_1_increase.grid(row=0, column=0, padx=2, pady=2, sticky="ew")
btn_timer_1_decrease.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
btn_timer_2_increase.grid(row=0, column=3, padx=2, pady=2, sticky="ew")
btn_timer_2_decrease.grid(row=0, column=4, padx=2, pady=2, sticky="ew")
lbl_timer_1.grid(row=0, column=0)
lbl_timer_2.grid(row=0, column=1)
lbl_reaction_time.grid(row=0, column=0, sticky="w")

# In[] Run the App
thread_timer_1 = threading.Thread(target=update_timer_1, daemon=True)
thread_timer_2 = threading.Thread(target=update_timer_2, daemon=True)
thread_timer_3 = threading.Thread(target=update_timer_reaction_time, daemon=True)
thread_timer_1.start()
thread_timer_2.start()
thread_timer_3.start()

# A Better Way
# executor = ThreadPoolExecutor(max_workers=2)
# thread_timer_1 = executor.submit(update_timer_1)
# thread_timer_2 = executor.submit(update_timer_2)
window.bind("<Button-1>", event_button_1)
window.protocol("WM_DELETE_WINDOW", on_closing_window)
window.mainloop()


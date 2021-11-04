"""
Using Events and Event Handlers
"""
# In[] Libs
import tkinter as tk
import random

# In[] Initializations
window = tk.Tk()
window.title("Working with Events & Event Handler in TKinter")

# In[] Using .bind()
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

def roll():
    lbl_result["text"] = str(random.randint(1, 6))

btn_roll = tk.Button(master=window, text="Roll", command=roll)
btn_roll.grid(row=1, column=1, sticky="nsew")
lbl_result = tk.Label(master=window, text="?")
lbl_result.grid(row=2, column=1, sticky="ew")

# In[] Run the App
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
window.mainloop()
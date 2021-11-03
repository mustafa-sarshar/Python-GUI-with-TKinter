# In[] Libs
import tkinter as tk

# In[] Initializations
window = tk.Tk()
window.title("Working with Frames in TKinter")

# In[] Add frames and widgets
# Assigning Widgets to Frames With Frame Widgets
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

# %% Adjusting Frame Appearance With Reliefs
""" 
Relief Attribute: (https://realpython.com/python-gui-tkinter/#working-with-widgets)
- tk.FLAT creates a frame that appears to be flat.
- tk.SUNKEN adds a border that gives the frame the appearance of being sunken into the window.
- tk.RAISED gives the frame a border that makes it appear to protrude from the screen.
- tk.GROOVE adds a border that appears as a sunken groove around an otherwise flat frame.
- tk.RIDGE gives the appearance of a raised lip around the edge of the frame.
"""
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

# In[] Run the App
window.mainloop()

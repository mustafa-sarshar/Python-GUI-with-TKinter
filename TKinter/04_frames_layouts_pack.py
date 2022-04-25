"""
Controlling Layout With Geometry Managers
- .pack()
- .place()
- .grid()
"""
# %% Libs
import tkinter as tk

# %% Define a Window
window = tk.Tk()
frames_packing = tk.Frame(window)
frames_packing.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frames_placing = tk.Frame(window)
frames_placing.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frames_griding = tk.Frame(window)
frames_griding.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frames_griding_2 = tk.Frame(window)
frames_griding_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# %% Define some Frames
# .pack() method
frame1 = tk.Frame(master=frames_packing, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=frames_packing, width=70, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=frames_packing, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# %% The .place() Geometry Manager

label1 = tk.Label(master=frames_placing, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frames_placing, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

"""
Notes: (https://realpython.com/python-gui-tkinter/#working-with-widgets)
.place() is not used often. It has two main drawbacks:
- Layout can be difficult to manage with .place(). This is especially true if your application has lots of widgets.
- Layouts created with .place() are not responsive. They don’t change as the window is resized.
"""

# %% The .grid() Geometry Manager
for i in range(3):    
    frames_griding.rowconfigure(i, weight=1, minsize=50) 
    for j in range(4):
        frames_griding.columnconfigure(j, weight=1, minsize=75)
        frame = tk.Frame(
            master=frames_griding,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}", padx=5, pady=5)
        label.pack()

# %% Use Sticky attribute
frames_griding_2.rowconfigure(0, minsize=50)
frames_griding_2.columnconfigure([0, 1, 2, 3], minsize=50, weight=10)

label1 = tk.Label(frames_griding_2, text="1", bg="black", fg="white")
label2 = tk.Label(frames_griding_2, text="2", bg="black", fg="white")
label3 = tk.Label(frames_griding_2, text="3", bg="black", fg="white")
label4 = tk.Label(frames_griding_2, text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

"""
Note:
    .grid()	            .pack()
    sticky="ns"	        fill=tk.Y
    sticky="ew"	        fill=tk.X
    sticky="nsew"	    fill=tk.BOTH
"""

# %% Run the App
window.mainloop()
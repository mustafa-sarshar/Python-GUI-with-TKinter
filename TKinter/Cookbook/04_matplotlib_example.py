# In[] Libs
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk

# In[] Global Functions
def _destroyWindow():
    window.quit()
    window.destroy()

# In[] Design the Layout
fig = Figure(figsize=(12, 6), facecolor="white")
# axis = fig.add_subplot(111) # 1 row, 1 column, only graph
axis_1 = fig.add_subplot(211) # 2 rows, 1 column, Top graph
x = np.linspace(0, 100, 1000)
y = np.sin(x) * np.cos(x)
axis_1.plot(x, y)
axis_1.set_xlabel("Timeline")
axis_1.set_ylabel("sin() x cos()")
axis_1.grid(linestyle="--")

axis_2 = fig.add_subplot(212) # 2 rows, 1 column, Bottom graph
x_2 = np.linspace(0, 100, 1000)
y_2 = np.sin(x) + np.cos(x)
l1, = axis_2.plot(x, y, label="sin() x cos()", color="purple")
l2, = axis_2.plot(x_2, y_2, label="sin() + cos()", color="red")
axis_2.set_xlabel("Timeline")
axis_2.set_ylabel("sin() + cos()")
axis_2.grid()
axis_2.legend()
# fig.legend((l1, l2), ("sin() x cos()", "sin() + cos()"), "upper right")
# flatten list of lists retrieving minimum value
y_all = [y, y_2]
minY = min([y for y_val in y_all for y in y_val])
yUpperLimit = 20 # flatten list of lists retrieving max value within defined limit
maxY = max([y for y_val in y_all for y in y_val if y < yUpperLimit])
# dynamic limits
axis_2.set_ylim(minY-1, maxY+1)
axis_2.set_xlim(min(x_2)-1, max(x_2)+1)

# Define the Window
window = tk.Tk()
window.withdraw() # Hide the window with .withdraw

# Add Canvas to the Window
canvas = FigureCanvasTkAgg(fig, master=window)
# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
canvas._tkcanvas.grid(row=1, column=0)
toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.grid(row=0, column=0, sticky="W")
toolbar.update()

window.update()
window.deiconify() # To reveal the window again
window.protocol("WM_DELETE_WINDOW", _destroyWindow)
window.mainloop()
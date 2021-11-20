# In[] Libs
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter.constants import W

# In[] Classes
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        # Display text in tooltip window
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            tw, text=self.text, justify=tk.LEFT,
            background="#ffffe0", relief=tk.SOLID,
            borderwidth=1, font=("tahoma", "8", "normal")
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

#===========================================================
def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

if __name__ == "__main__":
    win = tk.Tk()
    win.title("Tooltip Example")

    # Add a Widget
    lbl_name = ttk.Label(master=win, text="Name")
    lbl_name.grid(row=0, column=0, sticky="E")
    var_name = tk.StringVar(value="default name")
    ent_name = ttk.Entry(master=win, textvariable=var_name)
    ent_name.grid(row=0, column=1, sticky="W")
    createToolTip(widget=ent_name, text="Name Box")

    win.mainloop()
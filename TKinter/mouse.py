import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("200x100")
l =ttk.Label(root, text="Starting...")
l.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()
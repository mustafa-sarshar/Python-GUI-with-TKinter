# In[] Libs
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import W

# In[] Functions and Methods
def click_me():
    print(lbl_1["foreground"])
    if lbl_1["foreground"] == "black":
        lbl_1.configure(foreground="red")
        btn_1.configure(text="Clicked!")
    else:
        lbl_1.configure(foreground="black")
        btn_1.configure(text="Click Me Again!")

def set_the_name():
    messagebox.showinfo(title="Info!", message=f"Your name is: {var_name.get()}")

# In[] Define the Layout and Widgets
window = tk.Tk()
window.resizable(False, False)

lbl_1 = ttk.Label(master=window, text="Click the 'Click Me' button!", foreground="black")
lbl_1.grid(row=0, column=0)
btn_1 = ttk.Button(master=window, text="Click Me!", command=click_me)
btn_1.grid(row=0, column=1)

lbl_2 = ttk.Label(master=window, text="Enter a name:", foreground="black")
lbl_2.grid(row=1, column=0)
var_name = tk.StringVar(value="default text")
ent_2 = ttk.Entry(master=window, textvariable=var_name)
ent_2.grid(row=2, column=0)
btn_2 = ttk.Button(master=window, text="Set the name", command=set_the_name)
btn_2.grid(row=2, column=1)



window.mainloop()
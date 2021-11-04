"""
Building a Text Editor (Example App)
Inspired by (accessed on 03.11.2021):
    https://realpython.com/python-gui-tkinter/#working-with-widgets

There are three essential elements in the application:
    - A Button widget called btn_open for opening a file for editing
    - A Button widget called btn_save for saving a file
    - A TextBox widget called txt_edit for creating and editing the text file

The three widgets will be arranged so that the two buttons are on the left-hand 
side of the window, and the text box is on the right-hand side. The whole window 
should have a minimum height of 800 pixels, and txt_edit should have a minimum width 
of 800 pixels. The whole layout should be responsive so that if the window is resized, 
then txt_edit is resized as well. The width of the Frame holding the buttons should 
not change, however.
"""
# In[] Libs
import tkinter as tk
from tkinter import filedialog

# In[] Global Functions
def open_file():
    """Open a file for editing."""
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = filedialog.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

# In[] Define a window
window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

# In[] Add Widgets to the App
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# In[] Run the App
window.mainloop()
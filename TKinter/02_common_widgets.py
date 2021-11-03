"""
Widget Class    Description

Label	        A widget used to display text on the screen
Button	        A button that can contain text and can perform an action when clicked
Entry	        A text entry widget that allows only a single line of text
Text	        A text entry widget that allows multiline text entry
Frame	        A rectangular region used to group related widgets or provide padding between widgets
"""
# In[] Libs
import tkinter as tk

# In[] Initialization
# Create a window
window = tk.Tk()
window.title("Tell us about your self")

# Displaying Text and Images With Label Widgets
label_1 = tk.Label(
    master=window,
    text="Hello my friend",
    foreground="white",  # Set the text color to white
    background="gray"  # Set the background color to black
).pack()

# Note: a list of HTML valid color names that work well with TKinter can be found here: https://htmlcolorcodes.com/color-names/
label_2 = tk.Label(
    master=window,
    text="What's up?",
    fg="white",
    bg="black",
    width=10,
    height=1
).pack()
"""
Note:
Tkinter uses text units for width and height measurements, instead of something like inches, 
centimeters, or pixels, to ensure consistent behavior of the application across platforms.
Measuring units by the width of a character means that the size of a widget is relative to
the default font on a user’s machine. This ensures the text fits properly in labels and buttons,
no matter where the application is running.
"""
# Displaying Clickable Buttons With Button Widgets
button_1 = tk.Button(
    master=window,
    text="Click me!",
    width=10,
    height=5,
    bg="blue",
    fg="yellow",
).pack()

# Getting User Input With Entry Widgets
entry_1 = tk.Entry(
    master=window,
    fg="black",
    bg="yellow",
    width=20,
)
entry_1.insert(index=0, string="default text")
entry_1.pack()
"""
Methods:
- Retrieving text with .get()
- Deleting text with .delete()
- Inserting text with .insert()
"""
# Getting Multiline User Input With Text Widgets
text_1 = tk.Text(
    master=window,
    width=25,
    height=5,
    bg="gray"
)
text_1.insert(index="0.0", chars="Write a lot of text here ...")
text_1.pack()

# In[] Run the app
window.mainloop()
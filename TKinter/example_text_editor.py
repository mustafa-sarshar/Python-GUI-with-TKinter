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

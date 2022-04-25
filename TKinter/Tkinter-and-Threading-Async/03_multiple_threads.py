# Source: https://pypi.org/project/asynctkinter/
from concurrent.futures import ThreadPoolExecutor
import asynctkinter as at
from tkinter import Tk, Label
at.patch_unbind()

root = Tk()
label = Label(root, text='Hello', font=('', 60))
label.pack()

executer = ThreadPoolExecutor()

def func_A():
    for i in range(10):
        print("Func_A:", i)

def func_B():
    for i in range(100):
        print("Func_B:", i)       

async def some_task(widget):
    # create a new thread, run a function inside it, then
    # wait for the completion of that thread
    r = await at.run_in_thread(
        func_A, after=widget.after)
    print("return value:", r)

    # run a function inside a ThreadPoolExecutor, and wait for the completion
    r = await at.run_in_executer(
        func_A, executer, after=widget.after)
    print("return value:", r)
    r = await at.run_in_executer(
        func_B, executer, after=widget.after)
    print("return value:", r)



at.start(some_task(label))
root.mainloop()
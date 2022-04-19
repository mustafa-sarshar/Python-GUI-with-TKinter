# Source: https://pypi.org/project/asynctkinter/

from tkinter import Tk, Label
import asynctkinter as at
at.patch_unbind()

root = Tk()
label = Label(root, text='Hello', font=('', 60))
label.pack()

# async def some_task(label):
#     label['text'] = 'start heavy task'

#     while True:
#         # wait for a label to be pressed
#         event = await at.event(label, '<Button>')
#         print(f"pos: {event.x}, {event.y}")

#         # wait for 2sec
#         await at.sleep(1, after=label.after)

async def some_task(label):
    from functools import partial
    import asynctkinter as at
    sleep = partial(at.sleep, after=label.after)
    # wait until EITEHR a label is pressed OR 5sec passes
    tasks = await at.or_(
        at.event(label, '<Button>'),
        sleep(100),
    )
    print("The label was pressed" if tasks[0].done else "5sec passed")

    # wait until BOTH a label is pressed AND 5sec passes"
    tasks = await at.and_(
        at.event(label, '<Button>'),
        sleep(100),
    )
    print("The label was pressed and 5 Sec too" if tasks[0].done else "nothing")
    print(tasks)

at.start(some_task(label))
root.mainloop()

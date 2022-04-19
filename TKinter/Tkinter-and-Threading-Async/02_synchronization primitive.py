# Source: https://pypi.org/project/asynctkinter/
import asynctkinter as at
import time

async def task_A(e):
    print("Task_A:", e)
    print('A1')
    # await e.wait()
    print('A2')

async def task_B(e):
    print("Task_B:", e)
    print('B1')
    # await e.wait()
    print('B2')

async def task_C(e):
    for _ in range(10):
        print("Task_C:", e)

async def task_D(e):
    for _ in range(10):
        print("Task_D:", e)

time_start = time.perf_counter()

e = at.Event()
at.start(task_C(e))
at.start(task_D(e))
at.start(task_A(e))
# A1
at.start(task_B(e))
# B1
# e.set()
# A2
# B2
at.start(task_C(e))
at.start(task_D(e))

time_finish = time.perf_counter()
print("Duration:", time_finish-time_start)
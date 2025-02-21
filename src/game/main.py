import tkinter as tk
import time
import math

root = tk.Tk()
root.title("stock market game")
root.attributes("-fullscreen", True)
root.update()
win_size = [root.winfo_width(), root.winfo_height()]

a = tk.Label(root, text="hello", bg="lightblue",font=("arial",90))
a.grid(row=0, column=0, padx=5, pady=5)

#clock = hour.minute
clock = 0
filler_zero = ""
for i in range(48):
    clock += .25
    if clock % 1 == 0:
        filler_zero = 0
    else:
        filler_zero = ""
    a.config(text = f"{math.floor(clock)}:{filler_zero}{round(clock % 1 *60)}")
    root.update()
    time.sleep(1)
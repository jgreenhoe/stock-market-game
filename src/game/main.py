import tkinter as tk
import time
import math

root = tk.Tk()
root.title("stock market game")
root.attributes("-fullscreen", True)
root.update()
win_size = [root.winfo_width(), root.winfo_height()]

a = tk.Label(root, text="hello", font=("arial",20))
a.grid(row=0, column=0, padx=5, pady=5)

#clock = hour.minute
clock = 0
#number of increments per hour
interval = 6
while(1):
    for i in range(interval * 24):
        a.config(text = f"{math.floor(clock)}:{round(clock % 1 * 60):02d} {clock}")
        root.update()
        clock = i / interval
        time.sleep(1)
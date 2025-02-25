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
interval = 15
while(1):
    for i in range(interval * 24):
        #rounds clock when it should be an integer to avoid floating point inaccuracy
        if i % interval == 0:
            clock = round(clock)
        #adds a 0 to the display for single-digit minutes
        if clock % 1 < .1666:
            filler_zero = 0
        else:
            filler_zero = ""
        a.config(text = f"{math.floor(clock)}:{round(clock % 1 * 60):02d} {clock}")
        root.update()
        clock += 1 / interval
        time.sleep(1)
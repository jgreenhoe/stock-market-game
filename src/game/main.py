import tkinter as tk
import time

root = tk.Tk()
root.title("stock market game")
root.attributes("-fullscreen", True)
root.update()
win_size = [root.winfo_width(), root.winfo_height()]

a = tk.Label(root, text="hello", bg="lightblue",font=("arial",90))
a.grid(row=0, column=0, padx=5, pady=5)

#clock = [hour, minute]
clock = [0,0]
for i in range(48):
    if clock[1] == 1:
        clock[0] += 1
        clock[1] = 00
    else:
        clock[1] = 1
    a.config(text = f"{clock[0]}:{clock[1]*30}")
    root.update()
    time.sleep(1)
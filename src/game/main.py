import tkinter as tk

root = tk.Tk()
root.title("stock market game")
root.attributes("-fullscreen", True)
root.update()
win_size = [root.winfo_width(), root.winfo_height()]

a = tk.Label(root, text="hello", bg="lightblue",font=("arial",90))
a.grid(row=0, column=0, padx=5, pady=5)

tk.mainloop()
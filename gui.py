import tkinter as tk
import random




root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

def gen():

    x1 = entry1.get()
    int1 = int(x1)
    for c in range(int1):
        
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=+!@#$%^&*<>/~-:;?'
        x2 = random.choice(chars)
        label1 = tk.Label(root, (x2))
        canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Get the Square Root', command=gen)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

from tkinter import *
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
    length = int(e2.get())

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    myText.set(password)

    generate_random_password()

master = Tk()
master.wm_title("Password Generator")
myText = StringVar()
Label(master, text="").grid(row=0, sticky=W)
Label(master, text="").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result = Label(master, text="", textvariable=myText).grid(row=3, column=1, sticky=W)

e1 = Label(master, text="Enter Number of Characters:")
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b = Button(master, text="Get Password", command=generate_random_password)
b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

mainloop()

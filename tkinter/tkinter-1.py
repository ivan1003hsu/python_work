import tkinter as tk
import numpy as np

window = tk.Tk()
window.title('my first window')
window.geometry('200x100')

var = tk.StringVar() 

l = tk.Label(window, textvariable=var, bg='green', font=('Arial',12), width=15, height=2)
l.pack()

hit_on= False

def hit_me():
    global hit_on
    if hit_on == False:
        hit_on = True
        var.set('you hit me')
    else:
        hit_on = False
        var.set('')


b = tk.Button(window, text='hit me', width=10, height=2, command=hit_me)
b.pack()

window.mainloop()
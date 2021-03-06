import tkinter as tk
import os
import numpy.random as random
window = tk.Tk()
window.geometry("200x340")
window.title('bird')
canvas = tk.Canvas(window,bg='white',width=200,height=330)
canvas.pack()

bgimage = tk.PhotoImage(file='for_CP/flappy/bg-12.gif')  #510x340
bg1 = canvas.create_image(0,0, anchor='nw', image=bgimage)
bg2 = canvas.create_image(509,0, anchor='nw', image=bgimage)
def backgroundmoving():
    canvas.move(bg1,-0.5,0)
    canvas.move(bg2,-0.5,0)
    window.after(10,backgroundmoving)
def backgroundupdate():
    global bg1,bg2
    canvas.delete(bg1)
    bg1 = bg2
    bg2 = canvas.create_image(canvas.coords(bg1)[0]+509,0, anchor='nw', image=bgimage)
    window.after(18000,backgroundupdate)
backgroundmoving()
window.after(18000,backgroundupdate)


birdimage = tk.PhotoImage(file='for_CP/flappy/bird.gif')
bird = canvas.create_image(250,200, anchor='s', image=birdimage)
def birdmoving():
    canvas.move(bird,-1,0)
    window.after(1,birdmoving)
def birdupdate():
    global bird
    canvas.delete(bird)
    bird = canvas.create_image(250,200-random.randint(5,10)*20, anchor='c', image=birdimage)
    window.after(random.randint(16,20)*500,birdupdate)
birdmoving()
window.after(7000,birdupdate)



bgob = tk.PhotoImage(file='for_CP/flappy/bgob4.gif')
bg3 = canvas.create_image(0,330, anchor='sw', image=bgob)
bg4 = canvas.create_image(510,330, anchor='sw', image=bgob)
def bgobmoving():
    canvas.move(bg3,-4,0)
    canvas.move(bg4,-4,0)
    window.after(1,bgobmoving)
def bgobupdate():
    global bg3,bg4
    canvas.delete(bg3)
    bg3 = bg4
    bg4 = canvas.create_image(canvas.coords(bg3)[0]+510, 330, anchor='sw', image=bgob)
    window.after(2125,bgobupdate)
bgobmoving()
window.after(2200,bgobupdate)





window.mainloop()
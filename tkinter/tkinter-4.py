import tkinter as tk
window = tk.Tk()
window.geometry('250x1200')
window.title('radiobutton')

l = tk.Label(window, bg='yellow', width=20, height=2, text='choose one!')
l.pack()

def print_rb_selection():
    l.config(text='you have choosed '+ var1.get())

var1 = tk.StringVar()

rb1 = tk.Radiobutton(window, text='Option A', variable=var1, value='A',
command=print_rb_selection)
rb1.pack()

rb2 = tk.Radiobutton(window, text='Option B', variable=var1, value='B',
command=print_rb_selection)
rb2.pack()

rb3 = tk.Radiobutton(window, text='Option C', variable=var1, value='C',
command=print_rb_selection)
rb3.pack()

l2 = tk.Label(window, bg='yellow', width=20, height=2, text='try it')
l2.pack()

def print_scale_selection(v):
    l2.config(text='you have choosed ' + v)

s = tk.Scale(window, label='it', from_=5, to=11, orient=tk.HORIZONTAL, 
length=200, showvalue=1, tickinterval=2, resolution=0.01 ,command=print_scale_selection)
s.pack()


l3 = tk.Label(window, bg='yellow', width=20, height=2, text='check it you love')
l3.pack()

var2 = tk.IntVar()
var3 = tk.IntVar()

def print_ck_selection():
    var2var3 = var2.get()+var3.get()
    if var2var3 == 11:
        l3.config(text='I love both.')
    elif var2var3 == 1:
        l3.config(text='I love python.')
    elif var2var3 == 10:
        l3.config(text='I love C++.')
    else:
        l3.config(text='I do not either')

ck1 = tk.Checkbutton(window, text='python', variable=var2, onvalue=1, offvalue=0, command=print_ck_selection)
ck2 = tk.Checkbutton(window, text='C++', variable=var3, onvalue=10, offvalue=0, command=print_ck_selection)
ck1.pack()
ck2.pack()

l4 = tk.Label(window, bg='yellow', width=20, height=2,text='choose one')
l4.pack()

var5 = tk.StringVar()

def print_lb_selection():
    var5.set(lb.get(lb.curselection()))
    l4.config(text='you have choosed '+ var5.get())

b_lb = tk.Button(window, text='print_selection',command=print_lb_selection)
b_lb.pack()

var4 = tk.StringVar()
var4.set((11,22,33,44))
lb = tk.Listbox(window, listvariable=var4)
lb.pack()

canvas = tk.Canvas(window, bg='green', width=200, height=100)
canvas.pack()
image_file = tk.PhotoImage(file='tkinter/ins.gif')
image = canvas.create_image(10,10, anchor='nw', image=image_file)
line = canvas.create_line(50,50,60,60)
oval = canvas.create_oval(60,60,80,80,fill='red')
rect = canvas.create_rectangle(80,80,100,100)
arc = canvas.create_arc(100,60,120,80,start=50,extent=90)

def up():
    canvas.move(rect,0,-2)
def left():
    canvas.move(rect,-2,0)
def down():
    canvas.move(rect,0,2)
def right():
    canvas.move(rect,2,0)
canvas_button1 = tk.Button(window, text='up',command=up, width=5,height=1).pack(side='top',pady=20)
canvas_button2 = tk.Button(window, text='left',command=left, width=5,height=1).pack(side='left',padx=15, pady=5)
canvas_button3 = tk.Button(window, text='down',command=down, width=5,height=1).pack(side='left',padx=15, pady=5)
canvas_button4 = tk.Button(window, text='right',command=right, width=5,height=1).pack(side='left',padx=15, pady=5)

window.mainloop()
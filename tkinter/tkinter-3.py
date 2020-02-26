import tkinter as tk

window = tk.Tk()
window.title('listbox')
window.geometry('400x400')

var1 = tk.StringVar()

l = tk.Label(window, textvariable = var1, bg='yellow', width=4, height=2)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
b = tk.Button(window, text='print_selection', width=15, height=2, command=print_selection)
b.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable=var2)
lb.pack()

list_1=[1,2,3,4]
for i in list_1:
    lb.insert('end',i)
lb.insert(1,'a')
lb.insert(2,'b')
lb.delete(2)

window.mainloop()
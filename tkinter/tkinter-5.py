import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
window.title('my window with menu')
window.geometry('300x600')

l = tk.Label(window, bg='yellow', width=20, height=2)
l.pack()

menubar=tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)

def hello():
    l.config(text='hello')

filemenu.add_command(label='hello',command=hello)
filemenu.add_separator()
filemenu.add_command(label='exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='edit', menu=editmenu)
def goodb():
    l.config(text='goodbye')
editmenu.add_command(label='goodbye', command=goodb)

submenu=tk.Menu(filemenu)
filemenu.add_cascade(label='sub_menu', menu=submenu)
def world():
    l.config(text='world')
submenu.add_command(label='world', command=world)
window.config(menu=menubar)

l2 = tk.Label(window, text='',bg='green',width=15, height=2)
l2.pack()

def show_info():
    tk.messagebox.showinfo(title='show_info',message='Here are some information.')
tk.Button(window, text='show info', height=2, command=show_info).pack()
def show_error():
        tk.messagebox.showerror(title='show_error',message='Here is an error.')
tk.Button(window, text='show error', height=2, command=show_error).pack()
def show_warning():
        tk.messagebox.showwarning(title='show_warning',message='Here is a warning')
tk.Button(window, text='show warning', height=2, command=show_warning).pack()

def ask_ok_cancel():
  l2.config(text=(tk.messagebox.askokcancel(title='ask ok canel',message='Here is a question.')))
tk.Button(window, text='ask ok cancel', height=2, command=ask_ok_cancel).pack()
def ask_question():
      l2.config(text=(tk.messagebox.askquestion(title='ask question',message='Here is a question.')))
tk.Button(window, text='ask question', height=2, command=ask_question).pack()
def ask_yes_no():
      l2.config(text=(tk.messagebox.askyesno(title='yes no',message='Here is a question.')))
tk.Button(window, text='ask yes no', height=2, command=ask_yes_no).pack()
def ask_try_cancel():
      l2.config(text=(tk.messagebox.askretrycancel(title='try cancel',message='Here is a question.')))
tk.Button(window, text='ask try cancel', height=2, command=ask_try_cancel).pack()
def ask_yes_no_cancel():
      l2.config(text=(tk.messagebox.askyesnocancel(title='yes no cancel',message='Here is a question.')))
tk.Button(window, text='ask yes no cancel', height=2, command=ask_yes_no_cancel).pack()

## note:僅 ask question 回傳的是'yes' 和 'no' ,以及 ask yes no cancel中的 cancel 不回傳
## 其餘的都是布林值

window.mainloop()
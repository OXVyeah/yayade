#-*- coding: UTF-8 -*-
from Tkinter import *


def profile_find_run():

    root = Tk()
    root.title("file chooser")
    root.geometry("250x350")

    var_pro = StringVar()

    def print_item(event):
        s = lb.get(lb.curselection())
        var_pro.set(s)
        var2.set(s)  # 设置文本框中的值

    lb = Listbox(root, listvariable=var_pro, height=15, width=30)
    list_item = [1, 2, 3, 4]
    for item in list_item:
        lb.insert(END, item)
    lb.delete(2, 4)
    var_pro.set(('a', 'b', 'c', 'd'))

    lb.bind('<ButtonRelease-1>', print_item)
    lb.pack()

    var2 = StringVar()
    e = Entry(root, textvariable=var2, width=30)
    e.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

    def ok():
        print var2.get()

    def cancel():
        root.destroy()

    def goback():
        print -1

    Button(root, height=2, width=8, text="OK", command=ok).pack(side=RIGHT)
    Button(root, height=2, width=8, text="Cancel", command=cancel).pack(side=LEFT)
    Button(root, height=2, width=8, text="Last", command=goback).pack(side=LEFT)

    root.mainloop()  # 进入消息循环

    return 0

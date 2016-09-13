#-*- coding: UTF-8 -*-
from Tkinter import *
import findfl
import socket
#import gridtest


def pro_find_run():
    global p
    root = Tk()
    root.title("file chooser")
    root.geometry("530x340")

    var = StringVar()
    var2 = StringVar()
    fl = []
    isf = [FALSE]

    def print_item(event):
        s = lb.get(lb.curselection())
        print(s)
        if isf[0] == TRUE:
            fl.pop()
        fl.append(s)
        p = '\\'.join(fl)
        if findfl.GetFileList(p) != 0:
            if '\\' not in p:
                p += '\\'
            lb.delete(0, END)
            for item in findfl.GetFileList(p):
                lb.insert(END, item)
            lb.bind('<ButtonRelease-1>', print_item)
        else:
            isf[0] = TRUE
        var2.set(p)  # 设置文本框中的值
        print(p)
        gridtest.file_connect(p)
        return (p)
    lb = Listbox(root, listvariable=var, height=15, width=90)
    list_item = []
    if findfl.GetFileList('c:\\') != 0:
        list_item.append('c:')
    if findfl.GetFileList('d:\\') != 0:
        list_item.append('d:')
    if findfl.GetFileList('e:\\') != 0:
        list_item.append('e:')
    if findfl.GetFileList('f:\\') != 0:
        list_item.append('f:')
    if findfl.GetFileList('g:\\') != 0:
        list_item.append('g:')
    for item in list_item:
        lb.insert(END, item)
    lb.bind('<ButtonRelease-1>', print_item)
    lb.pack()

    e = Entry(root, textvariable=var2, width=90)
    e.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM


    def ok():
        print("llaaaaaaaaaaaaaaaaaaaaaa")
        s=var2.get()
        print(s)
        #
        #
        #
        # file_connect("findfile open")
        # file_connect("s")
        root.destroy()
        return s
        #break
    def cancel():
        root.destroy()

    def goback():
        if isf[0] == TRUE:
            fl.pop()
            isf[0] = FALSE
        if fl:
            fl.pop()
            p = '\\'.join(fl)
            if '\\' not in p:
                p += '\\'
            lb.delete(0, END)
            for item in findfl.GetFileList(p):
                lb.insert(END, item)
            lb.bind('<ButtonRelease-1>', print_item)
            var2.set(p)  # 设置文本框中的值
            if p == '\\':
                lb.delete(0, END)
                for item in list_item:
                    lb.insert(END, item)
                lb.bind('<ButtonRelease-1>', print_item)
            if not fl:
                var2.set(" ")

    # icon = PhotoImage(file = 'C:\\Users\\yu\\Documents\\workspace\\nasd\\qwr.gif')
    Button(root, text="OK", height=1, width=8, command=ok).pack(side=RIGHT, padx=10)
    Button(root, height=1, width=8, text="Cancel", command=cancel).pack(side=LEFT, padx=10)
    Button(root, height=1, width=8, text="Last", command=goback).pack(side=LEFT)

    root.mainloop()  # 进入消息循环


#pro_find_run()
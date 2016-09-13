# # -*- coding:utf-8 -*-
#
# """
# Text    文本框样例
# 实现功能有：Ctrl+a全选文本， 竖向滚动条，横向滚动条（不自动换行） 自动缩放
#
# 有谁知道全选文本的方法为会要 return 'break' 吗？
# http://blog.csdn.net/xxb2008
# """
#
# # import Tkinter
# #
# #
# # class MainFrame(Tkinter.Frame):
# #     def __init__(self, master=None):
# #         Tkinter.Frame.__init__(self, master)
# #         self.grid(row=0, column=0, sticky="nsew")
# #         self.createFrame()
# #
# #     def createFrame(self):
# #         label_frame_top = Tkinter.LabelFrame(self)
# #         # label_frame_top.pack()
# #
# #         label_frame_center = Tkinter.LabelFrame(self)
# #         label_frame_center.pack(fill="x")
# #
# #         lfc_field_1 = Tkinter.LabelFrame(label_frame_center)
# #         lfc_field_1.pack(fill="x")
# #
# #         self.lfc_field_1_l = Tkinter.Label(lfc_field_1, text="文件路径：", width=10)
# #         self.lfc_field_1_l.pack(fill="y", expand=0, side=Tkinter.LEFT)
# #
# #         self.lfc_field_1_b = Tkinter.Button(lfc_field_1, text="清除：", width=10, height=1, command=self.clearText)
# #         self.lfc_field_1_b.pack(fill="none", expand=0, side=Tkinter.RIGHT, anchor=Tkinter.SE)
# #
# #         ##########文本框与滚动条
# #         self.lfc_field_1_t_sv = Tkinter.Scrollbar(lfc_field_1, orient=Tkinter.VERTICAL)  # 文本框-竖向滚动条
# #         self.lfc_field_1_t_sh = Tkinter.Scrollbar(lfc_field_1, orient=Tkinter.HORIZONTAL)  # 文本框-横向滚动条
# #         self.computer_button=Tkinter.Button(lfc_field_1,text="computer1")
# #
# #         self.lfc_field_1_t = Tkinter.Text(lfc_field_1, height=15, yscrollcommand=self.lfc_field_1_t_sv.set,
# #                                           xscrollcommand=self.lfc_field_1_t_sh.set, wrap='c')  # 设置滚动条-不换行
# #         # 滚动事件
# #         self.lfc_field_1_t_sv.config(command=self.lfc_field_1_t.yview)
# #         self.lfc_field_1_t_sh.config(command=self.lfc_field_1_t.xview)
# #
# #         # 布局
# #         self.lfc_field_1_t_sv.pack(fill="y", expand=0, side=Tkinter.RIGHT, anchor=Tkinter.N)
# #         self.lfc_field_1_t_sh.pack(fill="x", expand=0, side=Tkinter.BOTTOM, anchor=Tkinter.N)
# #         self.lfc_field_1_t.pack(fill="x", expand=1, side=Tkinter.LEFT)
# #
# #         # 绑定事件
# #         self.lfc_field_1_t.bind("<Control-Key-a>", self.selectText)
# #         self.lfc_field_1_t.bind("<Control-Key-A>", self.selectText)
# #
# #         ##########文本框与滚动条end
# #
# #
# #
# #         label_frame_bottom = Tkinter.LabelFrame(self)
# #         # label_frame_bottom.pack()
# #
# #         pass
# #
# #         # 文本全选
# #
# #     def selectText(self, event):
# #         self.lfc_field_1_t.tag_add(Tkinter.SEL, "1.0", Tkinter.END)
# #         # self.lfc_field_1_t.mark_set(Tkinter.INSERT, "1.0")
# #         # self.lfc_field_1_t.see(Tkinter.INSERT)
# #         return 'break'  # 为什么要return 'break'
# #
# #     # 文本清空
# #     def clearText(self):
# #         self.lfc_field_1_t.delete(0.0, Tkinter.END)
# #
# #
# # def main():
# #     root = Tkinter.Tk()
# #     root.columnconfigure(0, weight=1)
# #     root.rowconfigure(0, weight=1)
# #     root.geometry('640x360')  # 设置了主窗口的初始大小960x540 800x450 640x360
# #
# #     main_frame = MainFrame(root)
# #     main_frame.mainloop()
# #
# #
# # if __name__ == "__main__":
# #     main()
# #     pass
# #
# #
# # from Tkinter import *
# # def callCheckbutton():
# #     global mac
# #     config_dict[mac].append("DownloadFile")
# # root = Tk()
# # Checkbutton(root,text = 'check python',command = callCheckbutton).pack()
# # root.mainloop()
# # from Tkinter import *
# # root = Tk()
# # #将一字符串与Checkbutton的值绑定，每次点击Checkbutton，将打印出当前的值
# # v = StringVar()
# # def callCheckbutton():
# #     print v.get()
# # mac='0'
# # com_background= "computer2.gif"
# #
# # img = PhotoImage(file=com_background)
# # H=Checkbutton(root,
# #             image=img,
# #             variable = v,
# #             text = mac,
# #             onvalue = mac,        #设置On的值
# #             #offvalue = '0',    #设置Off的值
# #             command = callCheckbutton)
# # Checkbutton().pack()
# # root.mainloop()
#
# #!/usr/bin/env python
# #encoding=utf-8
#
# import pythoncom
# import pyHook
# import time, os
#
# def onMouseEvent(event):
# 	# """监听鼠标事件"""
# 	global preWindowName, switch
# 	if not os.path.exists(mouseFilepath):
# 		os.makedirs(mouseFilepath)
# 	if switch:
# 		localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# 		datafileName = localTime[:localTime.find(" ")] + ".txt"
# 		#time  WindowName
# 		if not os.path.exists(mouseFilepath + datafileName):
# 			f = open(mouseFilepath + datafileName, "w")
# 			f.write("localTime				windowname\n")
# 			f.close()
#
# 		if type(event.WindowName) ==  str:
# 			if event.WindowName != preWindowName:
# 				datafileContent = localTime + ',	' + event.WindowName + '\n'
# 				f = open(mouseFilepath + datafileName, "a")
# 				f.write(datafileContent)
# 				f.close()
# 				preWindowName = event.WindowName
# 	#返回True以便将事件传给其他处理程序
# 	return True
#
# def onKeyboardEvent(event):
# 	"""监听键盘事件"""
# 	global switch
# 	if not os.path.exists(keyboardFilepath):
# 		os.makedirs(keyboardFilepath)
#
# 	if switch:
# 		localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# 		datafileName = localTime[:localTime.find(" ")] + ".txt"
# 		#time keyvalue Key WindowName
# 		if not os.path.exists(keyboardFilepath + datafileName):
# 			f = open(keyboardFilepath + datafileName, "w")
# 			f.write("localTime		keyvalue		key		windowname\n")
# 			f.close()
#
# 		if type(event.WindowName) ==  str:
# 			datafileContent = localTime + ',	' + chr(event.Ascii) + ',	' \
# 					+ event.Key + ',	' + event.WindowName + '\n'
# 			f = open(keyboardFilepath + datafileName, "a")
# 			f.write(datafileContent)
# 			f.close()
#
# 	if event.KeyID == 118:#Key=F7
# 		switch = False
# 	if event.KeyID == 115:#Key=F4
# 		switch = True
# 	# print event.KeyID
# 	#同鼠标监听事件函数的返回值
# 	return True
#
# def main():
# 	"""创建一个'钩子'管理对象"""
# 	hm = pyHook.HookManager()
#
# 	#监听所有键盘事件
# 	hm.KeyDown = onKeyboardEvent
# 	#设置键盘'钩子'
# 	hm.HookKeyboard()
#
# 	#监听所有鼠标事件
# 	hm.MouseAll = onMouseEvent
# 	#设置鼠标'钩子'
# 	hm.HookMouse()
#
# 	#进入循环，如不手动关闭，程序将一直处于监听状态
# 	pythoncom.PumpMessages()
#
# if __name__ == '__main__':
# 	keyboardFilepath = "./log/keyboard/"
# 	mouseFilepath = "./log/mouse/"
# 	preWindowName = ''
# 	switch = True #控制是否开启日志功能
# 	main()




import win32ui
import win32con
import pyHook
import pythoncom
import win32gui
#import wx


def hookhandle(event):
	if event.KeyID == 9:  # tab键值
		try:
			pwin = win32ui.FindWindow('AfxMDIFrame70', None)  # 主窗口 AfxMDIFrame70就是你用#spyxx.exe查找到的窗口类名
			pwin1 = win32ui.FindWindowEx(pwin, None, 'MDIClient', None)
			pwin2 = win32ui.FindWindowEx(pwin1, None, 'AfxFrameOrView70', None)
			pwin3 = win32ui.FindWindowEx(pwin2, None, "AfxOleControl70", None)
			pwin4 = win32ui.FindWindowEx(pwin3, None, None,
										 "PatientCardControl Frame")  # 可以根据窗口#的标题名称查找 标题名称一般外接程序是不变的 而类名有时是变化的 比如机器重启 关闭等
			pwin5 = win32ui.FindWindowEx(pwin4, None, "AfxMDIFrame70", None)
			pwin6 = win32ui.FindWindowEx(pwin5, None, "AfxWnd70", None)
			pwin7 = win32ui.FindWindowEx(pwin6, None, "#32770", None)

			textbox = pwin7.GetDlgItem(222)  # 获取控件的ID
			textbox2 = pwin7.GetDlgItem(224)

			buf = '0x0' * 1024
			buf2 = '0x0' * 1024
			textbox.SendMessage(win32con.WM_SETTEXT, "")  # 先清空控件内容
			textbox2.SendMessage(win32con.WM_SETTEXT, "")

			oldlen = textbox.SendMessage(win32con.WM_GETTEXT, buf)
			oldlen2 = textbox2.SendMessage(win32con.WM_GETTEXT, buf2)

			textbox.SendMessage(win32con.WM_SETTEXT, buf[0:oldlen] + str(blh))  # 发送消息 注意不能##用%s 替换 所以一般需要全局变量 来替换
			textbox2.SendMessage(win32con.WM_SETTEXT, buf2[0:oldlen] + str(name))
		except:
			wx.LogMessage('没有发现可用的窗口！请确保程序已经运行')



hm = pyHook.HookManager()  # 初始实例
hm.KeyDown = hookhandle
hm.HookKeyboard()
pythoncom.PumpMessages(5000)  # 据说是winctype的新功能 延迟吧 具体什么也不清楚
hm.UnhookKeyboard()  # 释放键盘捕捉 好像效果不明显
# for i in range (0,40):
# win32api.Sleep(20)
# if win32ui.PumpWaitingMessages(0,-1):
win32api.PostQuitMessage(0)  # 退出监控消息 很关键 必须配合sys.setrecursionlimit(4000)使用效果##才明显 不然的话 程序无法退出。


# raise exceptions.SystemExit



#
#
# def OnClose(self, event):
# 	sys.setrecursionlimit(4000)  # 相当关键
# 	self.Close(True)
# 	self.Destroy()
#
# import keylogger
# keylogger.run()

# import threading
# import inspect
# import ctypes
#
#
# def _async_raise(tid, exctype):
# 	"""raises the exception, performs cleanup if needed"""
# 	if not inspect.isclass(exctype):
# 		raise TypeError("Only types can be raised (not instances)")
# 	res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
# 	if res == 0:
# 		raise ValueError("invalid thread id")
# 	elif res != 1:
# 		# """if it returns a number greater than one, you're in trouble,
# 		# and you should call it again with exc=NULL to revert the effect"""
# 		ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
# 		raise SystemError("PyThreadState_SetAsyncExc failed")
#
#
# class Thread(threading.Thread):
# 	def _get_my_tid(self):
# 		"""determines this (self's) thread id"""
# 		if not self.isAlive():
# 			raise threading.ThreadError("the thread is not active")
#
# 		# do we have it cached?
# 		if hasattr(self, "_thread_id"):
# 			return self._thread_id
#
# 		# no, look for it in the _active dict
# 		for tid, tobj in threading._active.items():
# 			if tobj is self:
# 				self._thread_id = tid
# 				return tid
#
# 		raise AssertionError("could not determine the thread's id")
#
#
# def raise_exc(self, exctype):
# 	"""raises the given exception type in the context of this thread"""
# 	_async_raise(self._get_my_tid(), exctype)
#
#
# def terminate(self):
# 	"""raises SystemExit in the context of the given thread, which should
#     cause the thread to exit silently (unless caught)"""
# 	self.raise_exc(SystemExit)


# _*_ coding:UTF-8 _*_
import win32api
import win32con
import win32gui
from ctypes import *
import time
import msvcrt
import threading
from time import sleep
import sys
import ctypes.wintypes

EXIT = False


def mouse_click(x=None, y=None):
	if not x is None and not y is None:
		mouse_move(x, y)
		time.sleep(0.05)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_move(x, y):
	windll.user32.SetCursorPos(x, y)


class Hotkey(threading.Thread):  # 创建一个Thread.threading的扩展类

	def run(self):
		global EXIT  # 定义全局变量，这个可以在不同线程见共用。
		user32 = ctypes.windll.user32  # 加载user32.dll
		if not user32.RegisterHotKey(None, 99, win32con.MOD_ALT, win32con.VK_F3):  # 注册快捷键 alt + f3 并判断是否成功。
			raise  # 返回一个错误信息
		# 以下为判断快捷键冲突，释放快捷键
		try:
			msg = ctypes.wintypes.MSG()
			# print msg
			while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
				if msg.message == win32con.WM_HOTKEY:
					if msg.wParam == 99:
						EXIT = True
						return
				user32.TranslateMessage(ctypes.byref(msg))
				user32.DispatchMessageA(ctypes.byref(msg))
		finally:
			user32.UnregisterHotKey(None, 1)


if __name__ == "__main__":
	hotkey = Hotkey()
	hotkey.start()
	for event in range(1, 30):
		mouse_click(1150, 665)
		win32api.keybd_event(17, 0, 0, 0)
		win32api.keybd_event(86, 0, 0, 0)
		win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
		mouse_click(1272, 669)
		if EXIT:
			sys.exit()



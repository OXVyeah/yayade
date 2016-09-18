
def getNeed(rep,pcname):
	if rep.contents("path/"+pcname+".txt") == None :
		rep.create_file("path/"+pcname+".txt",pcname +"getNeed readfile create","")
	con = rep.contents("path/"+pcname+".txt")
	msg = base64.decodestring(str(con.content))	
	newmsg = ""
	l = msg.split("\n")
	for i in l :
		if i == "" or i == " ": continue;
		else :
			upFiles(i,rep)
			print "upload "+i

def upFiles(filename,rep):
	fileHandle = open(filename, 'rb')
	binstr=fileHandle.read()
	if rep.contents("data/"+pcname+"/doc/"+filename) != None :
		con = rep.contents("data/"+pcname+"/doc/"+filename)
		con.update("update file automatically from py",binstr)
	else:
		rep.create_file("data/"+pcname+"/doc/"+filename,"upload file " +filename,binstr)
    fileHandle.close()
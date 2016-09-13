
import os,sys,re
import subprocess
import socket
from github3 import *
import fileOperation


def connect_to_github():
    gh = login(username="OXVyeah", password="heiya233")
    repo0 = gh.repository("OXVyeah", "TROyeah")

    branch0 = repo0.branch("master")

    return repo0


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

def connect_dict():
    rep = connect_to_github()
    con = rep.contents("ip/mumaip.txt")
    # test hack
    fileOperation.writeIpOfHack(rep)
    l = fileOperation.getRightIp(con)
    print l

    canConnect = []
    for ips in l:
        if NetCheck(ips) == 'UP':
            canConnect.append(ips)

    return canConnect



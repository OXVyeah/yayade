#-*- coding: UTF-8 -*-
import pymongo
import time
import re

client = pymongo.MongoClient('localhost', 27017)
# 从MongoDB中选择名称为 URL_LISTS 的数据库
TROJAN= client['TROJAN']
# 从 URL_LISTS 数据库选择名称为 BLACK_LISTS 的表
PATH = TROJAN['PATH']
list_paths = []

# for line in open("paths.txt"):
#
#     path=line.replace('\\', '/')
#     list_paths.append(path)
#
# for path in list_paths:
#     dic_path = {
#         'path': path,
#         'time': time.time()
#     }
#
#     #print(dic_path)
#     PATH.insert_one(dic_path)

def search_file(p):
    paths = PATH.find({"path": re.compile(p)}).limit(10)
    # for data in PATH.aggregate(pipline):
    for data in paths:
        print data
search_file("c:")

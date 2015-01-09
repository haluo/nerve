#coding: utf-8
__author__ = 'zhufeng'

import os,datetime;
from sys import argv;
'''
导出图片URL
'''


try:
    script,path = argv;
except:
    print("with path name please--------------")

# print "listing path:%s"%path
count = 0;
for path,dirs,files in os.walk(path):
    # print(path,dirs,files)
    for file in files:
        count+=1
        allpath = os.path.join(path, file);
        allpath = allpath.replace('/data/upext','http://www1.autoimg.cn')
        print allpath
# print(count)




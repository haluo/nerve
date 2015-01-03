#coding: utf-8
__author__ = 'zhufeng'

import os,datetime;
from sys import argv;
'''
统计文件夹下文件个数，创建日期,文件大小
'''


try:
    script,path = argv;
except:
    print("with path name please--------------")

print "listing path:%s"%path
count = 0;
for path,dirs,files in os.walk(path):
    # print(path,dirs,files)
    for file in files:
        count+=1
        allpath = os.path.join(path, file);
        timestamp = os.path.getctime(allpath);
        date = datetime.datetime.fromtimestamp(timestamp)
        today = datetime.datetime.today()
        # print(today-date)
        print "file %s create date %s  today %s byte %d" %(file,date.strftime('%Y-%m-%d %H:%M:%S'),today.strftime('%Y-%m-%d %H:%M:%S'),os.path.getsize(allpath))
print(count)




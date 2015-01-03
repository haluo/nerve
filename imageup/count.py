__author__ = 'zhufeng'

import os,datetime;
from sys import argv;



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
        timestamp = os.path.getctime(os.path.join(path, file));
        date = datetime.datetime.fromtimestamp(timestamp)
        print(file,date.strftime('%Y-%m-%d %H:%M:%S'))
print(count)




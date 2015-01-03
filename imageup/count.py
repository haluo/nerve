__author__ = 'zhufeng'

import os;
from sys import argv;

def getFile(path):
    print("dddd")


try:
    script,path = argv;
except:
    print("with path please")

print "listing path:%s"%path
getFile(path)



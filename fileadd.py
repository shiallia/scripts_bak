'''
改变视频文件的md5
'''

import os
import sys


rootdir = r'D:/test'

list = os.listdir(rootdir) 
for i in list:
    path = os.path.join(rootdir,i)
    if os.path.isfile(path):
        if i.startswith("00_"):
            continue
        with open(path, 'a') as f:
            f.write("00")
        os.rename(path,rootdir+r"\00_"+i)

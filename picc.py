#coding=gbk 
#coding:utf-8
import requests
import os
url = "https://apis.jxcxin.cn/api/dmimg"
dir = "F://pics//"
for i in range(1,51):
    path = dir + str(i) + '.jpg'
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
        if not os.path.exists(path):
               r = requests.get(url)
               with open(path,'wb') as f:
                   f.write(r.content)
                   f.close()
                   print(path + "下载成功")
        else:
            print(path + "已存在")
    except IOError as e:
        print(str(e))
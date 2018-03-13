# 检查本地文件夹大小工具
import os

__file = 'C:'

__totalSize = 0

__sortMap = {}

__list = []


def iterFile(path):
    global __totalSize
    files = os.listdir (path)
    for f in files:
        try:
            p1 = path + '/' + f
            if os.path.isdir (p1):
                # 遍历目录
                iterFile (p1)
            else:
                # 遍历文件
                fsize = os.path.getsize (p1)
                f = fsize / float (1024)
                __totalSize = __totalSize + f
        except:
            pass


def getPathSize(path):
    global __totalSize
    files = os.listdir (path)
    for p in files:
        try:
            allpath = path + '/' + p
            iterFile (allpath)
            # print('路径：' + allpath + '，大小：' + str(round(__totalSize / float(1024) / float(1024), 2)) + 'GB')
            global __sortMap
            __sortMap[allpath] = str (round (__totalSize / float (1024) / float (1024), 2))
            __totalSize = 0
        except:
            pass


def sort():
    for k, v in __sortMap.items ():
        l = []
        l.append (v)
        l.append (k)
        __list.append (l)

    __list.sort (reverse=True)
    for i in __list:
        formatPrint (i[1], i[0])


def formatPrint(key, value):
    key = '路径：' + key
    value = '，大小：' + value + 'GB'

    kedLen = 100
    s = kedLen - len (key)
    for si in range (s):
        key = key + ' '

    print (key + value)


getPathSize ('C:\dxlc/')
sort ()

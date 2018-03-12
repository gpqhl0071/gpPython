# 检查本地文件夹大小工具
import os

__file = 'C:'

__totalSize = 0

__sortMap = {}


def iterFile(path):
    global __totalSize
    files = os.listdir(path)
    for f in files:
        try:
            p1 = path + '/' + f
            if os.path.isdir(p1):
                # 遍历目录
                iterFile(p1)
            else:
                # 遍历文件
                fsize = os.path.getsize(p1)
                f = fsize / float(1024)
                __totalSize = __totalSize + f
        except:
            pass


def getPathSize(path):
    global __totalSize
    files = os.listdir(path)
    for p in files:
        try:
            allpath = path + '/' + p
            iterFile(allpath)
            # print('路径：' + allpath + '，大小：' + str(__totalSize / float(1024) / float(1024)) + 'GB')
            global __sortMap
            __sortMap[allpath] = __totalSize / float(1024) / float(1024)
            __totalSize = 0
        except:
            pass


getPathSize('C:\dxlc/')

for v in __sortMap.values():
    print(v)

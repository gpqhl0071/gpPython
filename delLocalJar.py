# -*- coding:utf-8 -*-
import os
import re
import shutil

__format1_prefix = '[^\s]*dx-[^\s]*'
__format1_suffix = '[^\s]*'
__format1 = ''
__mavenFileList = []


def iterFile(path):
    files = os.listdir(path)
    for f in files:
        p1 = path + '/' + f
        if os.path.isdir(p1):
            # 遍历目录
            iterFile(p1)
            if re.match(__format1, p1):
                print(p1)
                __mavenFileList.append(p1)
        else:
            # 遍历文件
            pass


def handleDelMavenJar():
    flag = input('请输入是否删除（Y or N）：')
    if 'Y' is flag:
        for mavenFile in __mavenFileList:
            # 删除目录开关
            shutil.rmtree(mavenFile)
            print('已删除：' + mavenFile)
    else:
        print('结束')


def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            # print(f)
    return size


def delMavenJar():
    try:
        path = 'C:/Users/Administrator/.m2/repository'
    except Exception as e:
        print('异常', e)

    version = input('请输入大象版本号：')
    global __format1
    __format1 = __format1_prefix + version + __format1_suffix

    iterFile(path)
    handleDelMavenJar()


if __name__ == '__main__':
    i = input('1、删除maven仓库多余jar \n2、查看文件夹大小 \n请输入命令码：')
    i = int(i)
    if i == 1:
        delMavenJar()
    elif i == 2:
        print('查看文件夹大小')
    else:
        print('无此命令...')
# print(getFileSize(path))
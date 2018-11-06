import os
import re


def handleUnix(command):
    str = os.popen(command).read()
    a = str.split("\n")
    for b in a:
        print(b)
    return a


def getProcessId(str):
    for b in str:
        if ('redis-server' in b):
            pattern = re.compile('-?[1-9]\d*')
            items = re.findall(pattern, b)
            print('进程ID：' + items[0])
            return items[0]


busi = input("stop | start:")

if busi == 'start':
    handleUnix('./redis-4.0.10/src/redis-server redis-4.0.10/redis.conf')
    handleUnix('./redis-4.0.10.slave1/src/redis-server redis-4.0.10.slave1/redis.conf')
    handleUnix('./redis-4.0.10.slave2/src/redis-server redis-4.0.10.slave2/redis.conf')

    for processID in handleUnix('ps -ef | grep redis'):
        print('-- ' + processID)

    print(handleUnix('./redis-4.0.10.slave2/src/redis-cli -p 6379 info Replication'))
elif busi == 'stop':
    for processID in handleUnix('ps -ef | grep redis'):
        id = getProcessId(processID)
        print('kill -9 ' + id)
        handleUnix('kill -9 ' + id)

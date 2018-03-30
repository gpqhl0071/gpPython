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
        if '/www/tomcatdx/bin/tomcat-juli.jar' in b:
            pattern = re.compile('-?[1-9]\d*')
            items = re.findall(pattern, b)
            print('tomcatdx进程ID：' + items[0])
            return items[0]


war_name = input('请输入要升级的war包名称:')
a = handleUnix("unzip /www/webapp/dx-web/work/" + war_name)

if len(a) > 0:
    print('解压成功...')

tomcatdx = handleUnix("ps -ef | grep tomcatdx")
processId = getProcessId(tomcatdx)

if input("是否重启dx-web（Y or N）") == 'Y':
    handleUnix("kill -9 " + processId)
    handleUnix("sh /www/tomcatdx/bin/startup.sh")

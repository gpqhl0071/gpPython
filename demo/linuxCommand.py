import os
import re

_program = 'dx-web'
_tomcatProgram = 'tomcatdx'


def handleUnix(command):
    str = os.popen(command).read()
    a = str.split("\n")
    for b in a:
        print(b)
    return a


def getProcessId(str):
    for b in str:
        if ('/bin/tomcat-juli.jar' in b and '/www/' + _tomcatProgram + '/conf/' in b):
            pattern = re.compile('-?[1-9]\d*')
            items = re.findall(pattern, b)
            print(_tomcatProgram + '进程ID：' + items[0])
            return items[0]


dx_num = input("请输入要升级的项目（1:dx-web、2:dx-aps、3:dx-agent、4:dx-mt、5:dx-auto）:")

if dx_num == '1':
    _program = 'dx-web'
    _tomcatProgram = 'tomcatdx'
elif dx_num == '2':
    _program = 'dx-aps'
    _tomcatProgram = 'tomcataps'
elif dx_num == '3':
    _program = 'dx-agent'
    _tomcatProgram = 'tomcatAgent'
elif dx_num == '4':
    _program = 'dx-mt'
    _tomcatProgram = 'tomcatMT3'
elif dx_num == '5':
    _program = 'dx-autotask'
    _tomcatProgram = 'tomcatauto'
else:
    print('未匹配到您输入的序号...')

print('当前目录下war:')
for war1 in handleUnix("ls /www/webapp/" + _program + "/work/*.war"):
    if len(war1) == 0:
        continue
    print('  | ----' + war1)

war_name = input('请输入要升级的war包名称:')
a = handleUnix("unzip /www/webapp/" + _program + "/work/" + war_name + " -d /www/webapp/" + _program + "/work/")

if len(a) > 0:
    print('解压成功...')

tomcatdx = handleUnix("ps -ef | grep " + _tomcatProgram)
processId = getProcessId(tomcatdx)

if input("是否重启" + _program + "（Y or N）") == 'Y':
    handleUnix("kill -9 " + processId)
    handleUnix("sh /www/" + _tomcatProgram + "/bin/startup.sh")

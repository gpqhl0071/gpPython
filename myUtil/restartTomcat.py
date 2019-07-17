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


def handleBusiType():
    global _program, _tomcatProgram
    if busi_flag in '1':
        dx_num = input("请输入要重启的tomcat项目（1:dx-web、2:dx-aps、3:dx-agent、4:dx-mt、5:dx-auto、6:dx-dm）:")
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
        elif dx_num == '6':
            _program = 'dx-dm'
            _tomcatProgram = 'tomcatadmin'
        else:
            print('未匹配到您输入的序号...')
            return "false"
    elif busi_flag in '2':
        dx_num = input(
            "请输入要重启的service项目（1：dx-public-service、2：dx-assets-service、3：dx-activity-service、4:dx-user-service、5:dx-strategy-service）:")
        if dx_num == '1':
            _program = 'dx-public-service'
        elif dx_num == '2':
            _program = 'dx-assets-service'
        elif dx_num == '3':
            _program = 'dx-activity-service'
        elif dx_num == '4':
            _program = 'dx-user-service'
        elif dx_num == '5':
            _program = 'dx-strategy-service'
        else:
            print('未匹配到您输入的序号...')
            return "false"
    else:
        print('未匹配到您输入的序号...')
        return "false"
    return "true"


busi_flag = input("请输入要重启的项目（1:tomcat server 2:servie server）:")

result = handleBusiType()

if result in 'true':
    tomcatdx = handleUnix("ps -ef | grep " + _tomcatProgram)
    processId = getProcessId(tomcatdx)

    if input("是否重启" + _program + "（Y or N）") == 'Y':
        if busi_flag in '1':
            handleUnix("kill -9 " + processId)
            handleUnix("sh /www/" + _tomcatProgram + "/bin/startup.sh")
            print("tail -f /www/" + _tomcatProgram + "/logs/catalina.out")

        elif busi_flag in '2':
            handleUnix("sh /www/webapp/" + _program + "/work/bin/restart.sh")
            print("tail -f /www/webapp/" + _program + "/work/logs/stdout.log")
        else:
            print('未匹配到您输入的序号...')
    else:
        print('终止')
else:
    print('终止')


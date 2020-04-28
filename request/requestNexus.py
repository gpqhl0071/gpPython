import requests
import json
import os
import re

_dx_name = ''
_download_top_url = 'http://nexus.1001dx.com/repository/'
_download_group = 'maven-snapshots/'
_suffix = '.jar'
_version = '6.0.0'
download_url = ''
snapshotVersion = ''

_projectList = ['dx-web', 'dx-aps', 'dx-autotask', 'dx-dm', 'dx-mt', 'dx-agent']
_projectServerList = ['dx-public-api-service', 'dx-assets-api-service', 'dx-user-api-service',
                      'dx-activity-api-service', 'dx-strategy-api-service', ]


def getProcessId(str):
    for b in str:
        if ('/bin/tomcat-juli.jar' in b):
            pattern = re.compile('-?[1-9]\d*')
            items = re.findall(pattern, b)
            # print(_tomcatProgram + '进程ID：' + items[0])
            return items[0]


def handleUnix(command):
    str = os.popen(command).read()
    a = str.split("\n")
    for b in a:
        print(b)
    return a


def requestSnapshotVersion():
    param2 = {"action": "coreui_Component", "method": "readComponentAssets", "data": [
        {"page": 1, "start": 0, "limit": 25, "filter": [{"property": "repositoryName", "value": "maven-snapshots"},
                                                        {"property": "componentModel",
                                                         "value": "{\"id\":\"maven-snapshots:com.redhorse:" + _dx_name + ":" + _version + "-SNAPSHOT\",\"repositoryName\":\"maven-snapshots\",\"group\":\"com.redhorse\",\"name\":\"" + _dx_name + "\",\"version\":\"" + _version + "-SNAPSHOT\",\"format\":\"maven2\",\"healthCheckLoading\":true}"}]}],
              "type": "rpc", "tid": 12}

    # param2 = {"action":"coreui_Component","method":"readComponentAssets","data":[{"page":1,"start":0,"limit":25,"filter":[{"property":"repositoryName","value":"maven-snapshots"},{"property":"componentModel","value":"{\"id\":\"maven-snapshots:com.redhorse:dx-web:6.1.0-SNAPSHOT\",\"repositoryName\":\"maven-snapshots\",\"group\":\"com.redhorse\",\"name\":\"dx-web\",\"version\":\"6.1.0-SNAPSHOT\",\"format\":\"maven2\",\"healthCheckLoading\":true}"}]}],"type":"rpc","tid":12}
    url = 'http://nexus.1001dx.com/service/extdirect'

    r = requests.post(url, json=param2)
    rs = r.text
    jsonLoad = json.loads(rs)
    print(jsonLoad['result']['data'][0]['attributes']['maven2']['version'])
    return jsonLoad['result']['data'][0]['attributes']['maven2']['version']


def requestNexus():
    global r
    param1 = {"action": "coreui_Search", "method": "read", "data": [
        {"page": 1, "start": 0, "limit": 300, "sort": [{"property": "version", "direction": "DESC"}],
         "filter": [{"property": "format", "value": "maven2"},
                    {"property": "attributes.maven2.artifactId", "value": _dx_name}]}], "type": "rpc", "tid": 13}
    # 公司内部地址
    url = 'http://nexus.1001dx.com/service/extdirect'
    r = requests.post(url, json=param1)
    return r


def tranResult(r):
    print(r)
    result = json.loads(r)
    data = result['result']['data']

    if len(data) == 0:
        print('未匹配到内容！！！')
        return

    rs_list = []
    for d in data:
        if d['version'] != _version + '-SNAPSHOT':
            continue

        path1 = d['group'].replace('.', '/') + '/'
        path2 = _dx_name + '/'
        path3 = (d['version'].split('-'))[0] + '-SNAPSHOT/'
        # path4 = _dx_name + '-' + d['version']
        path4 = _dx_name + '-' + snapshotVersion

        global _download_group
        if d['repositoryName'] == 'maven-snapshots':
            _download_group = 'maven-snapshots/'
        elif d['repositoryName'] == 'maven-releases':
            _download_group = 'maven-releases/'
            path3 = d['version'] + '/'

        setSuffix()

        download_url = _download_top_url + _download_group + path1 + path2 + path3 + path4 + _suffix

        rs = d['name'] + '-' + d['version'] + ": " + download_url
        # print(rs)

        map = {'name': path4 + _suffix, 'value': download_url}

        rs_list.append(map)

    return rs_list


def setSuffix():
    global _suffix
    if _projectList.__contains__(_dx_name):
        _suffix = '.war'
    else:
        _suffix = '-assembly.tar.gz'


def getUrl(value):
    global _dx_name
    _dx_name = value
    r = requestNexus()
    rs = r.text
    return tranResult(rs)


if __name__ == "__main__":
    print("可录入项目：dx-web, dx-aps, dx-autotask, dx-dm, dx-agent")
    _dx_name = input('请输入项目名字：')
    _version = input('请输入分支版本号：')
    target_name = ''

    r = requestNexus()
    snapshotVersion = requestSnapshotVersion()

    rs = r.text
    _list = tranResult(rs)
    for _map in _list:
        tempName = _map['name'][len(_dx_name): len(_map['name'])]

        temps = tempName.split('-')
        if temps[1] == _version:
            # print(tempName + " = " + _map['name'] + ':' + _map['value'])
            target_name = _map['name']
            download_url = _map['value']
            break

    print('wget ' + download_url)
    handleUnix('wget ' + download_url)
    if _dx_name in _projectList:
        print('mv ' + target_name + ' /www/webapp/' + _dx_name + '/work/')
        handleUnix('mv ' + target_name + ' /www/webapp/' + _dx_name + '/work/')
    if _dx_name in _projectServerList:
        print('mv ' + target_name + ' /www/webapp/service/')
        handleUnix('mv ' + target_name + ' /www/webapp/service/')

    # 针对tomcat服务脚本话重复工作------------ begin
    # _projectList = ['dx-web', 'dx-aps', 'dx-autotask', 'dx-dm', 'dx-mt', 'dx-agent']
    tomcatName = ''
    if _dx_name == 'dx-web':
        tomcatName = 'tomcatdx'
    elif _dx_name == 'dx-aps':
        tomcatName = 'tomcataps'
    elif _dx_name == 'dx-autotask':
        tomcatName = 'tomcatauto'
    elif _dx_name == 'dx-dm':
        tomcatName = 'tomcatadmin'
    elif _dx_name == 'dx-agent':
        tomcatName = 'tomcatAgent'
    else:
        print("非tomat服务")

    if tomcatName != '':
        print("rm -rf /www/webapp/" + _dx_name + "/work/WEB-INF/lib/")
        handleUnix("rm -rf /www/webapp/" + _dx_name + "/work/WEB-INF/lib/")

        print('unzip -o /www/webapp/' + _dx_name + '/work/' + target_name + ' -d /www/webapp/' + _dx_name + '/work/')
        handleUnix(
            'unzip -o /www/webapp/' + _dx_name + '/work/' + target_name + ' -d /www/webapp/' + _dx_name + '/work/')

        print("ps -ef | grep " + tomcatName)
        tomcatdx = handleUnix("ps -ef | grep " + tomcatName)

        processId = getProcessId(tomcatdx)

        if processId != '':
            print("kill -9 " + processId)
            handleUnix("kill -9 " + processId)
            print("sh /www/" + tomcatName + "/bin/startup.sh")
            handleUnix("sh /www/" + tomcatName + "/bin/startup.sh")
            print("tail -n 50 -f /www/" + tomcatName + "/logs/catalina.out")
        else:
            print("服务没有启动，请手动启动服务" + tomcatName)
    # 针对tomcat服务脚本话重复工作----------- end

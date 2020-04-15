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

_projectList = ['dx-web', 'dx-aps', 'dx-autotask', 'dx-dm', 'dx-agent']
_projectServerList = ['dx-public-api-service', 'dx-assets-api-service', 'dx-user-api-service',
                      'dx-activity-api-service', 'dx-strategy-api-service']


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
        path1 = d['group'].replace('.', '/') + '/'
        path2 = _dx_name + '/'
        path3 = (d['version'].split('-'))[0] + '-SNAPSHOT/'
        # path4 = _dx_name + '-' + d['version']
        path4 = _dx_name + '-' + requestSnapshotVersion()

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

        map = {'name': d['name'] + '-' + d['version'] + _suffix, 'value': download_url}

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
    # print("可录入项目：dx-web, dx-aps, dx-autotask, dx-dm, dx-agent")
    # _dx_name = input('请输入项目名字：')
    _version = input('请输入分支版本号：')
    handleUnix('rm -rf dx-* ')

    for _dx_name in _projectList:
        target_name = ''

        r = requestNexus()

        rs = r.text
        _list = tranResult(rs)
        for _map in _list:
            tempName = _map['name'][len(_dx_name): len(_map['name'])]

            temps = tempName.split('-')
            if temps[1] == _version:
                target_name = _map['name']
                download_url = _map['value'];
                break

        print('wget ' + download_url)
        handleUnix('wget ' + download_url)

        print(target_name)
        handleUnix('mkdir ' + _dx_name)
        handleUnix('unzip -o ' + target_name + ' -d /www/peng/online_test/' + _dx_name + "/")
        handleUnix('rm -rf ' + target_name)
        handleUnix('rm -rf /www/peng/online_test/' + _dx_name + '/WEB-INF/classes/jdbc.properties')
        handleUnix('rm -rf /www/peng/online_test/' + _dx_name + '/WEB-INF/classes/redis.properties')
        handleUnix('rm -rf /www/peng/online_test/' + _dx_name + '/WEB-INF/classes/tradeCenter.properties')
        handleUnix('rm -rf /www/peng/online_test/' + _dx_name + '/WEB-INF/classes/properties/')
        handleUnix('rm -rf /www/peng/online_test/' + _dx_name + '/WEB-INF/classes/spring/')

    for _dx_name in _projectServerList:
        target_name = ''

        r = requestNexus()

        rs = r.text
        _list = tranResult(rs)
        for _map in _list:
            tempName = _map['name'][len(_dx_name): len(_map['name'])]

            temps = tempName.split('-')
            if temps[1] == _version:
                target_name = _map['name']
                download_url = _map['value']
                break

        print('wget ' + download_url)
        handleUnix('wget ' + download_url)
        handleUnix('tar -zxvf ' + target_name)

        if _dx_name in 'dx-public-api-service':
            handleUnix('mv ' + _dx_name + '-' + _version + '-SNAPSHOT dx-public-service/')
            handleUnix('rm -rf dx-public-service/conf/dubbo.properties')
        elif _dx_name in 'dx-assets-api-service':
            handleUnix('mv ' + _dx_name + '-' + _version + '-SNAPSHOT dx-assets-service/')
            handleUnix('rm -rf dx-assets-service/conf/dubbo.properties')
            handleUnix('rm -rf dx-assets-service/conf/jdbc.properties')
        elif _dx_name in 'dx-user-api-service':
            handleUnix('mv ' + _dx_name + '-' + _version + '-SNAPSHOT dx-user-service/')
            handleUnix('rm -rf dx-user-service/conf/dubbo.properties')
            handleUnix('rm -rf dx-user-service/conf/jdbc.properties')
        elif _dx_name in 'dx-activity-api-service':
            handleUnix('mv ' + _dx_name + '-' + _version + '-SNAPSHOT dx-activity-service/')
            handleUnix('rm -rf dx-activity-service/conf/dubbo.properties')
            handleUnix('rm -rf dx-activity-service/conf/jdbc.properties')
        elif _dx_name in 'dx-strategy-api-service':
            handleUnix('mv ' + _dx_name + '-' + _version + '-SNAPSHOT dx-strategy-service/')
            handleUnix('rm -rf dx-strategy-service/conf/dubbo.properties')
            handleUnix('rm -rf dx-strategy-service/conf/jdbc.properties')
        else:
            print("项目名称有误。")

        handleUnix('rm -rf ' + target_name)

    # 针对tomcat服务脚本话重复工作----------- end

# 1 从nexus下载所有产物
# 2 遍历解压所有 unzip / tar -zxvf
# 3 所有文件夹重命名，保持和正式环境一致 mv
# 4 删除敏感文件 或 文件夹

# 5 本地打包online环境遍历配置，覆盖当前目录所有项目。

import requests
import json

_dx_name = ''
_download_top_url = 'http://nexus.td.internal/nexus/repository/'
_download_group = 'maven-snapshots/'
_suffix = '.jar'

_projectList = ['dx-web', 'dx-aps', 'dx- ', 'dx-dm', 'dx-mt', 'dx-agent']


def requestNexus():
    global r
    param1 = {"action": "coreui_Search", "method": "read", "data": [
        {"page": 1, "start": 0, "limit": 300, "sort": [{"property": "name", "direction": "ASC"}],
         "filter": [{"property": "format", "value": "maven2"},
                    {"property": "attributes.maven2.artifactId", "value": _dx_name}]}], "type": "rpc", "tid": 13}
    # 公司内部地址
    url = 'http://nexus.td.internal/nexus/service/extdirect'
    r = requests.post(url, json=param1)
    return r


def tranResult(r):
    result = json.loads(r)
    data = result['result']['data']

    if len(data) == 0:
        print('未匹配到内容！！！')
        return

    for d in data:
        path1 = d['group'].replace('.', '/') + '/'
        path2 = _dx_name + '/'
        path3 = (d['version'].split('-'))[0] + '-SNAPSHOT/'
        path4 = _dx_name + '-' + d['version']

        global _download_group
        if d['repositoryName'] == 'maven-snapshots':
            _download_group = 'maven-snapshots/'
        elif d['repositoryName'] == 'maven-releases':
            _download_group = 'maven-releases/'
            path3 = d['version'] + '/'

        setSuffix()

        download_url = _download_top_url + _download_group + path1 + path2 + path3 + path4 + _suffix

        rs = d['name'] + '-' + d['version'] + ": " + download_url
        print(rs)


def setSuffix():
    if _projectList.__contains__(_dx_name):
        global _suffix
        _suffix = '.war'


if __name__ == "__main__":
    _dx_name = input('请输入jar名字：')

    r = requestNexus()

    rs = r.text
    tranResult(rs)

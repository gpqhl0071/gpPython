import requests
import json
import os
import re


# 根据jar名称版本号获取snapshot 全名称，包含小版本号
def requestSnapshotVersion(name, version):
    param2 = {"action": "coreui_Component", "method": "readComponentAssets", "data": [
        {"page": 1, "start": 0, "limit": 25, "filter": [{"property": "repositoryName", "value": "maven-snapshots"},
                                                        {"property": "componentModel",
                                                         "value": "{\"id\":\"maven-snapshots:com.redhorse:" + name + ":" + version + "-SNAPSHOT\",\"repositoryName\":\"maven-snapshots\",\"group\":\"com.redhorse\",\"name\":\"" + name + "\",\"version\":\"" + version + "-SNAPSHOT\",\"format\":\"maven2\",\"healthCheckLoading\":true}"}]}],
              "type": "rpc", "tid": 12}

    url = 'http://nexus.1001dx.com/service/extdirect'

    r = requests.post(url, json=param2)
    rs = r.text
    jsonLoad = json.loads(rs)
    print(jsonLoad['result']['data'][0]['attributes']['maven2']['version'])
    return jsonLoad['result']['data'][0]['attributes']['maven2']['version']


def requestNexus(name):
    global r
    param1 = {"action": "coreui_Search", "method": "read", "data": [
        {"page": 1, "start": 0, "limit": 300, "sort": [{"property": "version", "direction": "DESC"}],
         "filter": [{"property": "format", "value": "maven2"},
                    {"property": "attributes.maven2.artifactId", "value": name}]}], "type": "rpc", "tid": 13}
    # 公司内部地址
    url = 'http://nexus.1001dx.com/service/extdirect'
    r = requests.post(url, json=param1)
    return r


if __name__ == "__main__":
    # print(requestSnapshotVersion('dx-web', '6.1.0'))
    r = requestNexus('dx-web')
    j = json.loads(r.text)
    print(j)
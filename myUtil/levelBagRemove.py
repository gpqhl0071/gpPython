# 工具类，异常项目开发中，升级包中的关键配置文件
# author：gaopeng

import os
import re

_PATH = 'G:\levelBag\dx-autotask-4.2.0-SNAPSHOT-dev'
__format1 = ''

__map = {}
__aps_remove_list = ['jdbc.properties', 'logback.xml', 'mongoDB.properties', 'dubbo-consumer-config.xml',
                     'redis.properties', 'tradeCenter.properties', 'acp_sdk.properties',
                     'acp_sdk898150107630858.properties']


def iterFile(path):
    files = os.listdir(path)
    for f in files:
        p1 = path + '/' + f
        if os.path.isdir(p1):
            # 遍历目录
            iterFile(p1)
            pass
        else:
            # 遍历文件
            # print(p1)
            __map[f] = p1


if __name__ == '__main__':
    iterFile(_PATH)
    for removeFile in __aps_remove_list:
        if removeFile in __map:
            print('handle delete path 【' + __map[removeFile] + '】')
            os.remove(__map[removeFile])

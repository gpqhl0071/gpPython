# 工具类，异常项目开发中，升级包中的关键配置文件
# author：gaopeng

import os

_PATH = 'G:\levelBag\dx-autotask-4.2.0-SNAPSHOT-dev'
__format1 = ''

__map = {}
__aps_remove_list = ['jdbc.properties', 'logback.xml', 'mongoDB.properties', 'dubbo-consumer-config.xml',
                     'redis.properties', 'tradeCenter.properties', 'acp_sdk.properties',
                     'acp_sdk898150107630858.properties', 'dubbo.properties']


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


def delete():
    handleDelList = []

    for removeFile in __aps_remove_list:
        if removeFile in __map:
            print('path 【' + __map[removeFile] + '】')
            handleDelList.append(__map[removeFile])

    handle = input('是否删除全部 是-Y， 否-N ：')

    if handle != 'Y':
        print("stop handle delete.")
        return

    for handleDel in handleDelList:
        print('delete path 【' + handleDel + '】success...')
        os.remove(handleDel)

    print("handle delete end.")


if __name__ == '__main__':
    _PATH = input('输出目标项目路径：')

    iterFile(_PATH)

    delete()

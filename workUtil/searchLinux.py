# auther: gaopeng
# version: python3
# 用于快速锁定要查找文件所在的目录，输出全路径

import os

# 目标搜索路劲
_srcPath = '/www/webapp'


# 要查找文件的后缀
# _suffix = 'jdbc.properties'


def extract(path, suffix):
    resultList = []
    for root, dirs, files in os.walk(path):
        # 增加过滤不必要的扫描
        if 'backup' in root:
            continue
        if len(files) == 0:
            continue
        else:
            for file in files:
                if file.endswith(suffix):
                    resultList.append(root + "\\" + file)
                    print(root + "/" + file)
    return resultList


_suffix = input("请输入要查找的文件:")

resultList = extract(_srcPath, _suffix)

import os
import shutil

# 导出到目录
_targetPath = 'D:\war'
# 目标搜索路劲
_srcPath = 'D:\IdeaProjects\dx-service'
# 要查找文件的后缀
_suffix = '.tar.gz'


def mkdir():
    folder = os.path.exists(_targetPath)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(_targetPath)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("create path : %s success " % (_targetPath))
    else:
        print("path : %s exist " % (_targetPath))


def extract(path, suffix):
    resultList = []
    for root, dirs, files in os.walk(path):
        if len(files) == 0:
            continue
        else:
            for file in files:
                if file.endswith(suffix):
                    print(root + "\\" + file)
                    resultList.append(root + "\\" + file)
    return resultList


mkdir()

resultList = extract(_srcPath, _suffix)

# 完成文件的复制
for srcFile in resultList:
    print("复制源文件..." + srcFile)
    shutil.copy(srcFile, _targetPath)

# 文件重命名.zip
for root, dirs, files in os.walk(_targetPath):
    for file in files:
        # 拼接全路径
        srcName = root + "\\" + file
        # 修改文件后缀
        targetName = root + "\\" + file.replace('.war', '.zip')
        # 重命名
        os.rename(srcName, targetName)
        print('%s replace %s' % (srcName, targetName))

import os
import shutil

_targetPath = 'D:\war'
_srcPath = 'D:\IdeaProjectsNew\dx-web-app'
_suffix = '.war'


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

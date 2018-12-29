import os
import shutil


def extract(path, suffix):
    resultList = []
    for root, dirs, files in os.walk(path):
        if len(files) == 0:
            continue
        for file in files:
            if file.endswith(suffix):
                print(root + "\\" + file)
                resultList.append(root + "\\" + file)

    return resultList


resultList = extract("D:\WORK\dx-new1", ".war")

for srcFile in resultList:
    print("复制..." + srcFile)
    shutil.copy(srcFile, "D:\war")

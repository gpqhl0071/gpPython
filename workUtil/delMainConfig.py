import os

delList = [
    "jdbc.properties",
    "redis.properties",
    "tradeCenter.properties",
    "jmx.properties",
    "mongoDB.properties",
    "logback.xml",
]

for root, dirs, files in os.walk("E:\dx-web-3.8.4-SNAPSHOT-dev"):
    # 过滤敏感文件
    if len(files) > 0:
        for file in files:
            if file in delList:
                print(root + ", " + file)

    # 遍历lib目录下的jar
    if (len(dirs) > 0):
        for dir in dirs:
            if dir == 'lib':
                handlePath = root + "/" + dir
                for root1, dirs1, files1 in os.walk(handlePath):
                    for file in files1:
                        print(root1 + ", " + file)

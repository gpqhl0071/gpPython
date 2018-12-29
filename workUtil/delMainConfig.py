import os

delList = [
    "jdbc.properties",
    "redis.properties",
    "tradeCenter.properties",
    "jmx.properties",
    "mongoDB.properties",
    "logback.xml",
]

jarList = [
    "hutool-all"
]

for root, dirs, files in os.walk("D:\dx-dm-3.7.2-SNAPSHOT-dev"):
    # 过滤敏感文件
    if len(files) > 0:
        for file in files:
            if file in delList:
                print(root + ", " + file)

    # 遍历lib目录下的jar
    if (len(dirs) > 0):
        for dir in dirs:
            # 锁定lib目录
            if dir == 'lib':
                handlePath = root + "/" + dir
                # 遍历目录下的所有jar
                for root1, dirs1, files1 in os.walk(handlePath):
                    for file in files1:
                        # 保留一下开头的JAR，其他删除
                        if file.startswith('dx-') or file.startswith('hutool'):
                            print(root1 + ", " + file)
                        else:
                            os.remove(root1 + "/" + file)

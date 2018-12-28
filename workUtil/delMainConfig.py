import os

delList = [
    "jdbc.properties",
    "redis.properties",
    "tradeCenter.properties",
    "jmx.properties",
    "mongoDB.properties",
    "logback.xml",
]

for root, dirs, files in os.walk("D:\IdeaProjectsNew1\dx-web3.8.0"):
    # print('root:' + root + ' ， dirs size:' + len(dirs).__str__())
    # print("files = ", files)
    if len(files) > 0:
        for file in files:
            if file in delList:
                print(root + ", " + file)

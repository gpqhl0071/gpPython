# author：gaopeng
import urllib.request

_PATH = 'G:/levelBag/1.txt'


def download_img(img_url, api_token):
    header = {"Authorization": "Bearer " + api_token}  # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        img_name = "1.jpg"
        filename = "G:/levelBag/" + img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())  # 将内容写入图片
            return filename
    except:
        return "failed"


f = open(_PATH)  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
while line:
    line = f.readline()
    str = line.split('"')
    for s in str:
        if "dm.1001.co" in s:
            print(s)
            download_img(s, '1')

f.close()

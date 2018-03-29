import ssl
import urllib.request
import chardet  # 需要导入这个模块，检测编码格式

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
chaper_url = "https://howtodoinjava.com/spring-aop-tutorial/"
req = urllib.request.Request(url=chaper_url, headers=headers)
page = urllib.request.urlopen(req)

html = page.read()
encode_type = chardet.detect(html)
html = html.decode(encode_type['encoding'])

print(html)

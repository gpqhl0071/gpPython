import cookielib
import urllib2

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib2.Request("http://xwiki.td.internal/bin/get/WIKI%E7%9F%A5%E8%AF%86%E5%BA%93/%E5%A4%A7%E8%B1%A1%E7%90%86%E8%B4%A2/%E5%A4%A7%E8%B1%A1%E7%90%86%E8%B4%A2%E4%BA%A7%E5%93%81%E8%AE%BE%E8%AE%A1%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86/%E9%9C%80%E6%B1%82%E6%96%87%E6%A1%A3/WebHome?outputSyntax=plain&sheet=XWiki.DocumentTree&root=document%3Axwiki%3AWIKI%E7%9F%A5%E8%AF%86%E5%BA%93.%E5%A4%A7%E8%B1%A1%E7%90%86%E8%B4%A2.%E5%A4%A7%E8%B1%A1%E7%90%86%E8%B4%A2%E4%BA%A7%E5%93%81%E8%AE%BE%E8%AE%A1%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86.%E9%9C%80%E6%B1%82%E6%96%87%E6%A1%A3.WebHome&showAttachments=true&showTranslations=false&root=document%3Axwiki%3AWIKI%E7%9F%A5%E8%AF%86%E5%BA%93.%E5%A4%A7%E8%B1%A1%E7%90%86%E8%B4%A2.%E5%A4%A7%E8%B1%A1%E7%90%86%E8%B4%A2%E4%BA%A7%E5%93%81%E8%AE%BE%E8%AE%A1%E8%A7%84%E5%88%92%E7%AE%A1%E7%90%86.%E9%9C%80%E6%B1%82%E6%96%87%E6%A1%A3.WebHome&data=children&id=%23&offset=30")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()

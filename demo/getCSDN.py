# -*- coding:utf-8 -*-

import os
import re
import urllib.request

import chardet  # 需要导入这个模块，检测编码格式

from demo import saveCSDNToWordPress


class Spider:

    def __init__(self, blogURL):
        self.num = 0
        self.blogURLHead = 'http://blog.csdn.net'
        self.siteURL = blogURL
        self.basePath = './GetContent'
        self.seq = 1000
        if os.path.exists(self.basePath) == False:
            os.mkdir(self.basePath)

    # 获取有几页博客
    def getPageNum(self):
        pattern = re.compile('page-item')
        # page = urllib.urlopen (self.siteURL)

        req = urllib.request.Request(self.siteURL)
        page = urllib.request.urlopen(req)

        html = page.read()

        encode_type = chardet.detect(html)
        content = re.findall(pattern, html.decode(encode_type['encoding']))
        # contentList = content[0].split ()
        # string = contentList[-1]
        # pageNum = filter (str.isdigit, string)

        return len(content)

    # 找到所有的标题
    def getAllTitleURL(self, pageURL):
        pattern = re.compile('<span class="link_title">(\s*\n*\s*)<a href="(.*?)">(\s*\n*\s*.*)')
        # page = urllib.urlopen (pageURL)

        req = urllib.request.Request(pageURL)
        page = urllib.request.urlopen(req)

        html = page.read()
        encode_type = chardet.detect(html)
        html = html.decode(encode_type['encoding'])

        items = re.findall(pattern, html)
        return items

    # 获取一篇文章的内容
    def getBrief(self, pageURL):
        pattern = re.compile('<div id="article_content"(.*?)</div>', re.S)
        # page = urllib.urlopen (pageURL)
        req = urllib.request.Request(pageURL)
        page = urllib.request.urlopen(req)

        html = page.read()
        encode_type = chardet.detect(html)
        html = html.decode(encode_type['encoding'])

        result = re.search(pattern, html)
        content = result.group(0)
        return content.strip()

    # 保存文章
    def saveBrief(self, content, fileName, pageURL):
        dirPath = 'CSDN'
        if os.path.exists(dirPath) == False:
            os.mkdir(dirPath)
        fileName = 'D:\CSDN\/' + fileName
        f = open(fileName, mode='w')
        f.write(content)

    # 查找对应的文章的标题
    def findPageTitle(self, pageURI, pageURL):
        keyInfo = "<span class=\"link_title\"><a href=\"" + pageURI + "\">(.*?)</a>"
        pattern = re.compile(keyInfo, re.S);
        # page = urllib.urlopen (pageURL)
        # html = page.read ()

        req = urllib.request.Request(pageURL)
        page = urllib.request.urlopen(req)

        html = page.read()
        encode_type = chardet.detect(html)
        html = html.decode(encode_type['encoding'])

        title = re.findall(pattern, html)
        titlePattern = re.compile(r'<[^>]+>', re.S)
        result = titlePattern.sub('', title[0])
        return result.strip()

    def subHtmlLabel(self, context):
        # [^>]表示匹配除去‘>’符号外的所有其他符号，+表示这类符号出现次数不限，即该字符串匹配'<任意内容>'
        pattern = re.compile(r'<[^>]+>', re.S)
        result = pattern.sub('', context)
        return result

    def savePerPageInfo(self, pageURL):
        contents = self.getAllTitleURL(pageURL)

        for item in contents:
            self.seq += 1
            self.num += 1
            perPageURL = item[1]
            pageTitle = item[2].replace(" ", "").replace("</a>", "").replace("\n", "")
            brief = self.getBrief(perPageURL)
            brief = brief.replace("'", "\\\'")
            # result = self.subHtmlLabel (brief)
            print('标题：' + pageTitle + ",内容：" + brief)
            saveCSDNToWordPress.saveWordPress(pageTitle, brief, str(self.seq))
            # self.saveBrief (result, pageTitle, item)

    def savePageInfo(self):
        pageNum = self.getPageNum()
        for i in range(1, int(pageNum) + 1):
            pageURL = self.siteURL + "/article/list/" + str(i)
            self.savePerPageInfo(pageURL)


# _name = input ('输入博客后缀:')
spider = Spider('http://blog.csdn.net/gaopeng0071/')
spider.savePageInfo()

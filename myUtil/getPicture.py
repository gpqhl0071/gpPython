# author：gaopeng
import os
import urllib
import urllib.request

_PATH = 'G:/levelBag/1.txt'


def from_url( url, filename = None ):
    '''Store the url content to filename'''
    if not filename:
        filename = os.path.basename( os.path.realpath(url) )

    req = urllib.request.Request( url )
    try:
        response = urllib.request.urlopen( req )
    except urllib.error.URLError as e:
        if hasattr( e, 'reason' ):
            print( 'Fail in reaching the server -> ', e.reason )
            return False
        elif hasattr( e, 'code' ):
            print( 'The server couldn\'t fulfill the request -> ', e.code )
            return False
    else:
        with open( filename, 'wb' ) as fo:
            fo.write( response.read() )
            print( 'Url saved as %s' % filename )
        return True


f = open(_PATH)  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
while line:
    line = f.readline()
    str = line.split('"')
    for s in str:
        if "dm.1001.co" in s:
            print(s)
            t = s.split('=')[1].split('&')

            from_url(s, 'G:/levelBag/'+t[0])

f.close()

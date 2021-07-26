from html.parser import HTMLParser
import urllib.request
import re

liststr = list()	#创建list存放车次信息

class MyHTMLParser(HTMLParser):
    tempstr=str()
    def handle_starttag(self, tag, attrs):
        if tag=='tr':
            self.tempstr=''

    def handle_endtag(self, tag):
        if tag=='tr':
			 #匹配列车类型 过滤无用的tr标签
            matchObj = re.match( r'G|D|K|T|Z|\d', self.tempstr)
            if matchObj:
                liststr.append(self.tempstr)

    def handle_data(self, data):
        if(data.isspace()==False):
            self.tempstr+=data+'\t'

url = 'http://qq.ip138.com/train/anhui/HeFei.htm'
data = urllib.request.urlopen(url).read()
data = data.decode('gb2312') #根据抓取页面设置数据编码
par = MyHTMLParser()
par.feed(data)
for value in liststr:
    print(value)
print(liststr.__len__())
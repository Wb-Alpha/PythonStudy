import urllib.request
import urllib.parse

#打开指定需要爬取的网页
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()      #读取网页代码
print(html)


#将数据使用urlencode编码处理后，再使用encoding设置为utf-8编码
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf-8')
#打开指定需要爬取的页面
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
html = response.read()
print(html)


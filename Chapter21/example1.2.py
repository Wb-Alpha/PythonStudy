import urllib3
#创建PoolManage对象，用于处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
#对需要爬取的网页发送请求
response = http.request('GET', 'http://www.baidu.com/')
print(response.data)
#post请求实现获取网页信息的内容，以下对需要爬取的网页发送请求
response = http.request('POST', 'http://httpbin.org/post', fields={'word': 'hello'})
import requests

#以GET请求方式为例，打印多种请求信息的示例
response = requests.get('http://baidu.com')
print("打印状态码", response.status_code)             #打印状态码
print("打印请求url", response.url)                    #打印请求url
print("打印头部信息", response.headers)               #打印头部信息
print("打印cookie信息", response.cookies)             #打印cookie信息
print("以文本形式打印网页源码", response.text)         #以文本形式打印网页源码
print("以字节流形式打印网页源码", response.content)     #以字节流形式打印网页源码

#以POST请求方式，发送HTTP网络请求的示例代码
print('以POST请求方式，发送HTTP网络请求的示例代码')
data = {'word': 'hello'}
#对需要爬取的网页发送请求
response = requests.post('http://httpbin.org/post', data=data)
print(response.content)


#有参数时的传递参数方法
payload = {'key1': 'value1', 'key2': 'value2'}
#对需要爬取的页面发送请求
response = requests.get("http:/httpbin.org/get", params=payload)
print(response.content)


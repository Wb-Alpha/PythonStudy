from bs4 import BeautifulSoup   #导入库
import lxml

#创建模拟HTML代码的字符串
html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their name were
<a href="http://example.com/elise" class="sister" id="link1">Elisa</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well</p>

<p class="story">...</p>
</body>
"""

#创建一个BueautifulSoup对象，获取页面正文
soup = BeautifulSoup(html_doc, features="lxml")
print(soup)
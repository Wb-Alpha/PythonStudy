a = 100
b = 50
print(a)
print(a+b)#在控制台打印字符串的方法

print("\u751f\u5316\u673a")
print("\u4e2d\u56fd")#一种直接输入Unicode编码并且转化成对应文字的方法

#使用print函数将内容输出到指定文件
fp = open(r'D:\PythonCode\TestFile\Chapter3-1Test.txt')
print("Go Big Or Go Home",file=fp)
fp.close()

#使用input函数输入
tip = input("你想要屏幕显示什么？")
print(tip)
inp = input("输入一个字符。将会输出ASCII码")
print(inp + "的ASCII码是",ord(inp))

#这是单行注释
'''
这是
多行注释
'''
"""
这
也是
多行注释
"""

#中文编码声明注释（防止乱码）
#-*-coding=utf-8-*-

#print函数使出多行数据的简便方法
print("*"*53+"\n")+("*"*53+"\n")+("*"*53+"\n")
print(((50*"*"+"\n")*10))


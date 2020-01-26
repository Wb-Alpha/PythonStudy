# 打开或者创建文件
# 格式： 被创建的文件对象 = open("文件地址+文件名"[,"读写模式"[,缓存模式]])
# 若文件不存在而且读取模式为 w,w+,a,a+的时候就会自动新建文件，否则抛出异常
f = open("createFile.txt", "r")

# 以二进制的形式打开文件,返回一个BufferedReader
'''
问题：使用一个文件对象打开多个文件会怎样？
覆盖 or 并存
'''
file1 = open('createFile.txt', 'rb')
print(file1)

# 打开文件的时候指定打开方式
file = open('FileEncoding.txt', 'r', encoding='utf-8')

# 关闭文件
file.close()
f.close()

'''打开文件的时候使用with语句

print("\n", "=" * 10, "Python经典应用", "=" * 10)
with open('message.txt', 'w') as file2:
    pass
print("\n即将显示\n")
'''
# 读取信息
record = file1.read()
print(record)

# 移动指针
file1.seek(3)

with open('createFile.txt', 'r') as file3:
    string = file3.read(9)
    print(string)

# 读取一行
file3 = open('createFile.txt', 'r')
record = file3.readline()
print("只读一行", record)
# 例子
print("\n", "=" * 20, "Python经典应用2", "=" * 20)
with open('message.txt', 'r') as file1:
    number = 0
    while True:
        number += 1
        line = file1.readline()
        if line == '':
            break
        print(number, line, end="\n")
print("====================over==================\n")

# 读取所有行
print("\n=========例子3================")
with open('message.txt', 'r') as file1:
    message = file1.readlines()
    print(message)
    print("\n================over=============")

print("\n==========例子4==============")
with open('message.txt', 'r') as file1:
    messageall = file1.readlines()
    for message in messageall:
        print(message)
print("\n=============over===========\n")

# 目录操作
# 用于对目录或者文件的模块
import os
import os.path

# 用于获取操作系统类型
type = os.name
# 用于获取当前操作系统上的换行符
change = os.linesep
# 用于获取当前操作系统上所使用的路径分隔符
record = os.sep
print(type, change, record)

# 输出当前目录
print(os.getcwd())

# 获取绝对路径
print(os.path.abspath('message.txt'))

# 判断目录是否存在
print(os.path.exists("C:/demo"))

# 创建一级目录
#os.mkdir("..\createDir")

#创建多级目录
path = "..\createDir\\new"
if not os.path.exists(path):
    os.mkdir(path)
    print("目录创建成功")
else:
    print("该目录已经存在")

#删除目录
path = "..\"

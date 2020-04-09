'''
string.format使用方法
第一种情况，不指定序号和格式说明符，按顺序将变量填入字符串中
'''
a = 'hi'
b = 3
print("{},an integer{},a float{}".format(a, b, 3.14))

'''第二种，只指定序号，可以省略冒号
    按序号将变量填入字符串
    Tips:所有占位符都要有指定序号
'''
print("{1},an integer{0},a float{2}".format(a, b, 3.14))

'''
第三种，使用格式符，不能省略冒号
[[fill] align][sign][width][,][.precision][type]
fill:设置填充的字符，可省略，默认为空格
align:是指对齐方式^、<、>分别是剧中，左对齐，右对齐，可省略
sign:设置数值型数据前的符号，+表示需要在正数前加正号，-表示在正数前不变，空格表示加空格，可省略
width:设置格式化后的字符串所占宽度，可省略
逗号(,):为数字添加千位分隔符，可省略
type:设置格式化类型
'''
print('{:6.2f}'.format(3.1415926))

#常用运算符
s = "Python"
one = "P" in s
print("P 包含着 Python中", one)
# 序列的创建和查询
verse = ["马刺", "湖人", "火箭", "勇士"]
print(verse[2])
print(verse[-1])

# 在列表中插入元素
verse.insert(1, 123)

# 反转列表函数
verse.reverse()

# 排序列表函数.没有返回值，改变原列表
lst12 = [12, 32, 43, 56, 234]
lst12.sort()  # 升序
lst12.sort(reversed=True)  # 降序

# 序列的切片
car = ["Lexus EX260", "BMW 340M", "Audi A4 GT", "Audi RS4", "BMW 700", "BMW M3"]
print(car[1:3])
print(car[0:5:2])

# 序列相加
fightjet = ["F/A-18E", "F15E", "F-22", "J10C", "J16", "J20", "Su27SM", "M2K"]
muti = car + fightjet
print(muti)

# 序列乘法
car = ["Lexus EX260", "BMW 340M", "Audi A4 GT", "Audi RS4", "BMW 700", "BMW M3"]
print(car * 3)

# 检查某个元素是否是序列的成员
car = ["Lexus EX260", "BMW 340M", "Audi A4 GT", "Audi RS4", "BMW 700", "BMW M3"]
print("BMW M3" in car)
print("Audi RS4" not in car)

# 计算序列长度、最大值和最小值
num = [7, 14, 21, 28, 35, 42, 49, 56, 63]
print("序列", num, "中最小值为", min(num))
print("序列", num, "中最大值为", max(num))
print("序列", num, "长度为", len(num))

# 创建列表
list = ['Python', 28, '人生苦短，我用Python', ['爬虫', '自动化运维', '云计算', 'Web开发']]
print(list)
print(list[2])
# for循环遍历列表
for item in list:
    print(item)
# 添加元素进列表中
list.append("FA-18C")
print("after add", list)
# 修改元素和Java中修改数组元素一致
# 删除元素
del list[-1]
print("after delete", list)

# 获取指定元素的出现次数
list.count("FA18C")

# 获取指定元素首次出现的下标
list.index(3)

# 统计数值列表的元素之和
grade = [98, 99, 97, 100, 100, 96, 94, 80, 95, 100]
total = sum(grade)
print("Python理论总成绩为：", total)

# 利用sort函数对列表进行排序
grade = [98, 99, 97, 100, 100, 96, 94, 80, 95, 100]
print("源列表", grade)
grade.sort()
print("升序", grade)
grade.sort(reverse=True)
print("降序", grade)

# 使用内置的sorted函数实现对列表的排序
grade = [98, 99, 97, 100, 100, 96, 94, 80, 95, 100]
grade_as = sorted(grade)
print("升序", grade_as)
grade_des = sorted(grade, reverse=True)
print("降序：" + grade_des)
print("原序列：", grade)

# 列表生成式
# 新列表对象= {表达式 for 变量 in 可迭代对象 <if条件>]
lst = [0, 1, 2, 3, 4]
lst2 = [x ** 2 for x in lst]
lst3 = [x for x in lst2 if x not in lst]
lst4 = [x for x in range(20) if x % 3 == 0]

# 拉链函数.zip
# 产生一个以两个列表元素聚合成元组的新迭代对象
z = zip(['a', 'b', 'c'], [1, 2, 3])

# 元组
# 和列表十分相似，可以看作为轻量化的列表，但和列表不同的是，元组元素值不能被修改
# 元组的轻量化使得他的运行速度较快，对内存的使用较少
# 使用赋值运算符直接创建元组
Graphics = ("RTX2070S", "RX580X", "GTX690", "HD9800", "QuadroP3000")
Num = (12, 433, 25, 34, 24, 2436, 56)

# 利用range函数创建一个数值元组
tuple(range(10, 20, 2))

# 使用索引访问元组中得元素
print(Num[1])

# 切片法访问数组元素
print(Graphics[:3])

# 合并两个元组
print((1, 2, 3) + (4, 5))

# 重复元组
print((1, 2) * 3)

# 迭代元组中的所有元素
for x in Num:
    print(x)

# 删除元组
del Graphics

# 统计元素在元组中出现的次数
print(Num.count())

# 列表和元组相互转换函数:tuple(list)和list(tuple)
tql = (1, 2, 3)
lst = list(tql)
lst[1] = 5
tql = tuple(lst)
print(tql)

# 创建字典
dictionary = {'qq': '1415839632', 'phone': '14718155972', 'name': "GDUF_Alpha"}
print(dictionary)
run = dict()

#重复
print([1, 2]*2)

# 利用zip函数将两个列表或者元组合成字典
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 4, 9, 16, 25, 36]
dict1 = dict(zip(list2, list2))
print(dict1)

# 通过关键字赋值创建字典
dict2 = dict(us='America', cn='China', jp='Japanse', un='UnionKingdom')
print(dict2)

# 添加和修改:如果存在则修改，不存在则添加
dict2['us'] = 'UniteState'

# 通过键值对访问字典
print(dictionary['qq'])
print(dict2.get('us'))
print(dict2['asd'] if 'asd' in dict2 else "没有查询到相关国家")

# 遍历字典
for item in dictionary.items():
    print(item)

# 添加一个元素
dict1[7] = 49
print("增加一个元素后：", dict)
dict2['cn'] = 'Canada'
print("当添加的元素存在时，添加相当于修改：", dict2)

# 使用字典推导式快速生成一个字典
import random

randomdict = {i: random.randint(10, 100) for i in range(1, 5)}
print("生成的字典是：", randomdict)

# 复制字典和删除字典
dict1.clear()
dict1 = dict2.copy()

#删除字典对象中的元素
dict3 = dict(us='America', cn='China', jp='Japanse', uk='UnionKingdom')
print(dict3)
del dict3['jp']
print(dict3)

#获得键对应的值
print(dict3.get('cn'))

#遍历字典
#遍历字典中所有的键
dict3.keys()
#遍历字典中所有的值
dict3.values()
#遍历字典里所有的键值对
dict3.values()

#批量更新字典中的元素
#利用字典d中的键值对批量更改dict3中的键值对
d = dict(us='UniteState', uk='England')
dict3.update(d)



#集合
#无需组合，元素不允许重复，可用于快速去重
#由于他是无序的，故没有索引概念，不能用索引下标访问
# 创建集合
set1 = {'紧凑型轿车', '跑车', '越野车', 'SUV', 'B级轿车'}
set2 = {1, 2, 3, 4, 5, 76}

# 使用set函数将列表元组等对象转换为集合
set3 = set("也许我只是一道微光，却像给你耀眼的光芒")
set4 = set((3.14, 1.23, 54.654))
set5 = set(['人生苦短', '我用Python'])
print(set3, "\n", set4, "\n", set5)

# 添加元素
set5.add("但我还是要说JAVA天下第一")
print(set5)
# 删除元素
# 删除指定元素
set5.remove("但我还是要说JAVA天下第一")
print(set5)
set4.pop()
print(set4)
set1.clear()
print(set1)
print("Change")

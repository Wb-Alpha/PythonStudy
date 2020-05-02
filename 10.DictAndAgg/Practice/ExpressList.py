judge = 1
name = set()
print("如果需要结束则输入1")
print("如果需要查询则输入2")
while(1):
    var = input("请输入需要收取快递的人员的名单")
    if var == "1":
        break
    elif var == "2":
      print(name)
    else:
        name.add(var)
print("程序退出")
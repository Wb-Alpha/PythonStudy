name = {"黄楚浩":"14718155972","曹栩滔":"13423537338"}
print("电话簿")

def search():
    judge = False
    var = input("请输入需要查询的人的姓名")
    for item in name:
        if var == item:
            print(item,"的电话号码是",name[item])
            judge = True
            break
        else:
            continue
    if judge == False:
        print("查无此人")

def delete():
    var = input("请输入需要删除的联系人姓名")
    judge = False
    for item in name:
        if var == item:
            del name[var]
            judge = True
            print("已删除联系人  ",var)
            break
        else:
            continue
    if judge == False:
        print("查无此人")

def add():
     var = input("请输入添加的联系人姓名")
     tel = input("请输入联系人电话号码")
     name[var] = tel
     print("联系人添加已成功：",var,tel)

def showAll():
    for item in name.items():
        print(item)

def default():
    print("输入了无效的指令")





function = {"1":search,"2":add,"3":delete,"4":showAll,"5":exit}
test = {1:2,2:4}
judge = True
while(judge):
    order = input("查询联系人 1， 添加联系人 2 ， 删除联系人 3 ， 电话簿显示 4 , 退出 5")
    function.get(order,default)()
print(" 通讯录 已退出")



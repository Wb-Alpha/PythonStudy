import datetime
import os


def login():
    name = input("用户名")
    filename = "record\\" + name + ".txt"
    print(filename)
    time = datetime.datetime.now()
    with open(filename, "a+") as file:
        write = "上次登录时间" + str(time) + "\n\n"
        file.write(write)
    return True


def search():
    name = input("请输入需要查找的用户登录日志")
    filename = "record\\" + name + ".txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            message = file.readlines()
            print(message)
    else:
        print("查无此人" )
    return True


def exit():
    return False


def default():
    print("输入了无效的命令")
    return True


code = {"1": login, "2": search, "3": exit}
judge = True
while judge:
    order = input("按1为登录，按2为查看用户登录日志，按3退出")
    judge = code.get(order, default)()

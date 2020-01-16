#定义函数
def fun_bmi(person = "匿名", height = 1.70 ,weight = 60):#为参数设置默认值
    print(person,"的身高是:"+str(height)+"米 \t 体重"+str(weight)+"千克")
    bmi = weight/(height*height)
    print(person+"的BMI指数是:"+str(bmi))
    if bmi<18.5:
        print("您的体重过轻，请注意保持摄入营养")
    elif bmi>=18.5 and bmi<=24.9:
        print("您的体重正常，注意保持")
    elif bmi>24.9 and bmi<=29.9:
        print("您的体重过重，请节制饮食")
    elif bmi>29.9:
        print("超重")

#引用函数
fun_bmi("黄楚浩",1.75,65)
fun_bmi()

#实际参数和形式参数的例子
def demo(obj):
    print("原值",obj)
    obj+=obj
print("==========值传递==========")
mot = "唯有被追赶的时候，你才能真正地奔跑"
print("函数调用前",mot)
demo(mot)       #采用不可变对象：字符串
print("函数被调用后")
print("==========引用函数传递========")
list1 = ['邓肯','吉诺比利','帕克']
print("函数调用前：",list1)
demo(list1)     #采用可变对象：列表
print("函数调用后：",list1)

#关键字参数：没有严格的参数位置限制
fun_bmi(height=1.82,weight=74,person="曹栩滔")

#查看参数默认值
print(fun_bmi.__defaults__)

#使用可变参数作为函数参数的默认值时可能会导致意料之外的情况
def demo(obj = []):#以可变参数作为参数
    print("obj的值：",obj)
    obj.append(1)
#连续调用obj函数
demo()
demo()
print("从上面结果看，这显然不是我们想要的结果。为了防止出现这种情况，最好是使用None作为可变对象的默认值,修改后的代码如下：")
def demo1(obj=None):
    if obj==None:
        obj=[]
    print("obj的值为：",obj)
    obj.append(1)
#再次连续调用
demo1()
demo1()
#2.**parameter表示接受多个显式赋值的实际参数，并将其放到一个字典中
def printsign(**sign):
    print()
    for key,value in sign.items():
        print("["+key+"]的绰号是："+value)
printsign(邓肯="石佛",罗宾逊="海军上将")

#返回值
def fun_checkout(name):
    nickname=""
    if name == "邓肯":
        nickname = "石佛"
    elif name =="吉诺比利":
        nickname = "妖刀"
    elif name == "罗宾逊":
        nickname = "海军上将"
    else:
        nickname = "无法找到你输入的消息"
    return nickname
#**********************调用函数**********************#

name = input("请输入NBA球员名称:")
nickname = fun_checkout(name)
print("球员：",name,"绰号:",nickname)


#可变参数
#有两种形式：一种是*parameter，一种是**parameter
#1.*parameter:表示接受多个实际参数并将其放入到一个元组中
def printplayer(*name):
    print("\n我喜欢的车有：")
    for item in name:
        print(item)

printplayer("BMW M3","Audi RS4","Tesla ModelS")
printplayer("Lexus ES260","BMW 330li")


#局部变量：在函数内部定义并且使用的变量
def f_demo():
    message = "唯有被追赶的时候，你才能真正奔跑"
    global tip
    tip = "幸福是奋斗出来的"
    print('局部变量message:',message)
    print(tip)
f_demo()
print("在函数外引用在函数内使用gobal修饰的参数",tip)
#print('局部变量message:',message)   在函数外调用会报错

#全局变量：能够作用于函数之外的任意函数的变量
message = '唯有被追赶的时候，你才能真正奔跑'
def f_demo():
    print('在函数体内：全局变量message=',message)
f_demo()
print('函数外:全局变量message:',message)


#匿名函数：指没有名字的函数。主要用于只需要使用一次的函数
import math
r = 10
result = lambda r:math.pi*r*r
print('半径为',r,'的元的面积为',result(r))

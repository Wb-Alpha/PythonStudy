password = "123678"
user_inp = str(input("请输入验证码："))
for item in user_inp:
    if ord(item) > 57 or ord(item) < 48:
        tip = "输入数字格式错误"
    else:
        if user_inp == password:
            tip = "支付密码正确"
        else:
            tip = "支付密码不正确"
print(tip)
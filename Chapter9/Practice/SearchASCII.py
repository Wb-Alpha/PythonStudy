index = input("请输入字母或数字，输出非字母或数字则退出程序")
asc = ord(index)
while ( (asc<58 and asc>49) or (asc<91 and asc>64) or (asc<123 and asc>96)):
    print(index,"的ASCII码为",asc)
    index = input("请输入字母或数字，输出非字母或数字则退出程序")
    asc = ord(index)
print("退出程序")


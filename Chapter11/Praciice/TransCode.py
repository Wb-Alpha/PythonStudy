def trans(code):
    dict = {"0": "O", "1": 'I', "2": 'Z', "3": 'E', "4": 'Y', "5": 'S', "6": 'G', "7": 'L', "8": 'B', "9": 'P'}
    codelist = list(code)
    answ = []
    for item in codelist:
        answ.append(dict[item])
    output = ''.join(answ)
    print(output)

code = input("请输入密码")
trans(code)

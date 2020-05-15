import random


# 自动整理
def autoSort():
    poker = []
    for i in range(4):
        for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            poker.append(j)
    return poker


num = 1  # 发牌次数
nums = 14  # 牌种
# 14种牌型标记
marklist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 统计函数
def count(l, nums, marklist):
    sum = 0
    temp = 0
    temp1 = 0
    l2 = list(l)
    for i in l2:
        if l2.count(i) == 4:
            if marklist[13] == 0:
                print('炸弹出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[13] = 1
            return nums, marklist

        elif i == 'J' or i == 'Q' or i == 'K':
            temp += 1
            temp1 += 1
            sum += 10

        elif i == '10':
            temp1 += 1
            sum += 10

        else:
            sum += int(i)
    # 五张牌结果<=10，五小
    if sum <= 10:
        if marklist[2] == 0:
            print('五小出现在第' + str(num) + '轮')
            print('p1:', li['p1'])
            print("=" * 30)
            nums -= 1
            marklist[2] = 1
        return nums, marklist
    # 其它牌型
    else:
        # 金牛
        if temp == 5:
            if marklist[0] == 0:
                print('金牛出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[0] = 1
            return nums, marklist
        # 银牛
        elif temp1 == 5:
            if marklist[1] == 0:
                print('银牛出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[1] = 1
            return nums, marklist
        # 牛0
        elif sum % 10 == 0:
            if marklist[3] == 0:
                print('牛0出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[3] = 1
            return nums, marklist
        # 牛9
        elif sum % 10 == 9:
            if marklist[4] == 0:
                print('牛9出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[4] = 1
            return nums, marklist
        # 牛8
        elif sum % 10 == 8:
            if marklist[5] == 0:
                print('牛8出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[5] = 1
            return nums, marklist
        # 牛7
        elif sum % 10 == 7:
            if marklist[6] == 0:
                print('牛7出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[6] = 1
            return nums, marklist
        # 牛6
        elif sum % 10 == 6:
            if marklist[7] == 0:
                print('牛6出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[7] = 1
            return nums, marklist
        # 牛5
        elif sum % 10 == 5:
            if marklist[8] == 0:
                print('牛5出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[8] = 1
            return nums, marklist
        # 牛4
        elif sum % 10 == 4:
            if marklist[9] == 0:
                print('牛4出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[9] = 1
            return nums, marklist
        # 牛3
        elif sum % 10 == 3:
            if marklist[10] == 0:
                print('牛3出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[10] = 1
            return nums, marklist
        # 牛2
        elif sum % 10 == 2:
            if marklist[11] == 0:
                print('牛2出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[11] = 1
            return nums, marklist
        # 牛1
        elif sum % 10 == 1:
            if marklist[12] == 0:
                print('牛1出现在第' + str(num) + '轮')
                print('p1:', li['p1'])
                print("=" * 30)
                nums -= 1
                marklist[12] = 1
            return nums, marklist


while True:
    # 如果14种牌型都出现了
    if nums <= 0:
        break
    # 扑克牌序列
    poker = autoSort()
    li = {}

    for k in ['p1', 'p2', 'p3', 'p4']:
        # 随机得到5张牌
        b = random.sample(poker, 5)
        for s in b:
            poker.remove(s)
        li.setdefault(k, b)
    # 统计p1的牌型
    t = count(li['p1'], nums, marklist)
    # 用作下一次统计
    nums = t[0]
    marklist = t[1]
    num += 1

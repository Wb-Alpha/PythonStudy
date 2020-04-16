def TransRMB(RMB):
    rouble = float(RMB) * 9.912
    print(RMB, "人民币等于", rouble, "卢布")


def TransRUB(RUB):
    RMB = float(RUB) / 9.912
    print(RUB, "卢布等于", RMB, "人民币")


judge = input("按1：人民币转俄罗斯卢布  按2:：俄罗斯卢布转人民币")
if judge == "1":
    RMB = input("请输入人民币金额")
    TransRMB(RMB)
elif judge == "2":
    rouble = input("请输入俄罗斯卢布金额")
    TransRUB(rouble)

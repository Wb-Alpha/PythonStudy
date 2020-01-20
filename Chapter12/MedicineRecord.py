import datetime
import time


class medicine:
    name = "无"
    price = 0
    PD = datetime.datetime.strptime("1940/1/1", "%Y/%m/%d")
    Exp = datetime.datetime.strptime("1943/11/23", "%Y/%m/%d")


    def __init__(self , name, price, PD, Exp):
        medicine.name = name
        medicine.price = int(price)
        medicine.PD = datetime.datetime.strptime(PD, "%Y/%m/%d")
        medicine.Exp = datetime.datetime.strptime(Exp, "%Y/%m/%d")

    def get_name(self):
        return medicine.name

    def get_GP(self):
        return medicine.Exp - medicine.PD


med = medicine("格列宁", 1040, "2018/6/23", "2021/3/1")
name = med.get_name()
BaoZhi = med.get_GP()
print(name, "   ", BaoZhi)

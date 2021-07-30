'''
#1 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end="  ")
    print()


#2 数组分为小数组
a = [34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56]
b = []
c = []
for i in range(len(a)):
    if a[i] <= 100:
        b.append(a[i])
    else:
        c.append(a[i])
print("小于100的数组为:",b)
print("大于100的数组为:",c)


#3 发红包
money = input("请输入红包金额：")#15.987
for i in money:
    if i not in "0123456789.":
        print("输入的值不合法，请重新输入")
        exit()
x = money.count(".")
if x > 1:
    print("请输入正确的值")
else:
    if "." in money:
        y = money.index(".") + 1
        z = len(money)
        floatlen = z - y
        if floatlen > 2:
            print("小数点后只能有两位，请重新输入")
        else:
            money =float(money)
            if money >= 0.01 and money <= 200:
                print("发送红包成功")
            else:
                print("发送红包失败，请输入合理值")
    else:
        money =float(money)
        if money >= 0.01 and money <= 200:
            print("发送红包成功")
        else:
            print("发送红包失败，请输入合理值")
'''

#4 判断这一天是一年中的第几天 
p_list = [0,31,59,90,120,151,181,212,243,273,304,334]#平年
r_list = [0,31,60,91,121,152,182,213,244,274,305,335]#闰年
year = int(input("请输入年份"))
month = int(input("请输入月"))
day = int(input("请输入号数"))
if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    days = r_list[month-1]+day
else:
    days = p_list[month-1]+day
print("{}年{}月{}日是今年中的第{}天".format(year,month,day,days))

'''
#5 将5位数的数字颠倒
a = 34567
a = list(str(a))
a.reverse()
c = ""
for i in a:
    c = c + i
c = int(c)
print(c)
'''
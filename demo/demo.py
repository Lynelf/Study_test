'''
print("你好")
a = int (input("输入第一个数字："))
b = int (input ("输入第二个数字："))
c = a + b
print ("a与b的和为:", c)
print("布尔值的产生：", a > b)


x = ["哈哈",45,"想念","知乎","什么",2,4]
print(x[2])
x.append(345)
print(x)
x.insert(3,"魅力")
print(x)
qu = x.pop(5)
print (qu)
print (x.reverse())

xx = {"name":"李梅","age":23,"high":"167cm",3:"可惜"}
print(xx.get("high"))
print(xx["name"])
print(xx.pop(3))
xx[4]= "meili"
print(xx)
del xx["age"]
print(xx)
print(xx.clear())


name = input("请输入姓名：")
high = input("请输入身高：")
age = input("请输入年龄")
xx = "大家好，我是{name},我今年{age}岁了，我身高是{high}cm".format(\
    name=name,age=age,high=high)
print(xx)

yy =(2,5,6,7,5,["hah","嘻嘻"],("为什么","只是","y"))
print(yy[3])
print(yy[5][1])
print(yy[6][2])



age = int(input("请输入年龄："))
if age > 25:
    print("好好生活")
elif age > 18:
    print("好好学习")
elif age >12:
    print("不要早恋")
else:
    print("好好玩耍吧")
  ''' 

money = input("请输入金额：")
for i in money:
    if i not in "0123456789." :
        print("输入的值不合法，请输入数字")
        exit()
xx = money.count(".")
if xx > 1:
    print("输入的值不合法!")
else:
    if "." in money:
        yy = money.index(".") + 1
        zz = len(money)
        floatlen = zz - yy
        if floatlen > 2:
            print("只能有两位小数")
        else:
            money = float(money) 
            if money >= 0.01 and money <=200:
                print("红包发送成功，金额为{}元".format(money))
            else:
                print("红包发送失败，{}元不在范围内".format(money))
    else:
        money = float(money) 
        if money >= 0.01 and money <=200:
            print("红包发送成功，金额为{}元".format(money))
        else:
            print("红包发送失败，{}元不在范围内".format(money))



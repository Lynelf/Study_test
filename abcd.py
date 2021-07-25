from sys import stderr
from typing import AbstractSet, Hashable
import time

'''基本的数据类型
#print(878979)
#print("hello world")

print("哈哈哈"+"为什么")
print("a"*5)

print(1+2)
print(2>3)
快捷注释 ctrl + /

'''

# pythons数据类型-------------------------------------
# a = input("请输入内容1：")
# b = input("请输入内容2：")
# print("输入的内容1的类型是",type(a))
# a = float(a)
# b = float(b)
# print("获取的内容：",a+b)

# c = "true167"
# print(type(c))
# d = bool(c)
# print(type(d))

# xx = input("请输入：")
# print(bool(type(xx) == str))

# a = "a"
# print(bool(type(a) == int))


# 元组--------------------------------------------------------
# htuple = (1,"haha","啦啦","lala","333","haha")
# print(htuple.count("haha"))
# print(htuple.index("啦啦"))


# 数组---------------------------------------------------
# hlist = ["keyi","阿里里","aaa","魅力",3]
# a = hlist.append("lov")
# print(hlist)
# b = hlist.count("keyi")
# print(b)
# c = hlist.index(3)
# print(c)
# d = hlist.insert(3,"漂亮")
# print(hlist)
# e = hlist.pop(2) #取走
# print("取走的值为：",e)
# f = hlist.remove("阿里里")
# print(hlist)


# 字典------------------------------------------------
# hdict = {"name":"张三","high":183,"sex":"男"}
# print(hdict["high"])
# hdict["age"] = 19
# print(hdict)


# for循环，遍历----------------------------------------
# hdict = {
#     "name":"zhangsan",
#     "age":34
# }

# for i in hdict:
#     print(i)
#     print(hdict[i])
#     # print("这是获取到的值",hdict.get(i))

# for i in range(0,3):
#     print(i)


# for循环例子-------------------------------------------------
# hlist  = []
# llist = []
# hahalist = [23,45,67,55,77,89,32,12,98,76,88,90,3.9,21]
# for i in hahalist:
#     if i >= 60:
#         hlist.append(i)
#     else:
#         llist.append(i)
# print("大于等于60的数组是",hlist)
# print("小于60的数组是",llist)


# while循环例子---------------------------------------------
# a = 0
# while a <  10:
#     print("a的值",a)
#     a = a +1


adict = {"红灯":30,"绿灯":15,"黄灯":3}
for i in adict:
    for j in range(adict[i]):
        print("{}已经运行{}秒了".format(i,j))
        time.sleep(1)
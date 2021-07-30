import time

'''
# a = 'hello, \'adam\''
# b = r'hello,"bart"'
# print(a)
# print(b)
# print(c)

# a = "hello,%s %s"%('world',348)
# print(a)

# name = "小明"
# s1 = 72
# s2 = 85
# r = (s2-s1)/s1*100
# print("{0}今年成绩提高了{1:.1f}%".format(name,r))

'''


# 。。。。。。。。。。。。。。。。。。。。。。。。。。。
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != j) and (i != k) and (j != k):
#                 x=str(i)+str(j)+str(k)
#                 print (x)


# 。。。。。。。。。。。。。。。。。。。。。。。。。
# 输入三个整数x,y,z，请把这三个数由小到大输出。
# L = []
# for i in range(3):
#     x = int(input("请输入数字："))
#     L.append(x)
# L.sort()
# print("从小到大输出三个数：",L)


# ...............................
# 斐波那契数列实现  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
# def fib(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     fibs = [1, 1]
#     for i in range(2,n):
#         fibs.append(fibs[-1] + fibs[-2])
#     return fibs
# print(fib(15))  



# ...........................................
# 把数组切片操作
# a = ['a','b','c','d','e','f','g','h','i','j','k']
# b= a[:]
# print(b)
# b1 = a[:3:-1] #从末尾数到a[3]不包括。['k', 'j', 'i', 'h', 'g', 'f', 'e']
# print("b1",b1)

# b2 = a[3::-1] #从a[3]往前数 包括。['d', 'c', 'b', 'a']
# print("b2",b2)


# ...........................................
# 暂停一秒输出
# for i in range(5):
#     print(i)
#     time.sleep(1)

# 10...........................................
# 暂停一秒输出，并格式化当前时间。
# print (time.strftime('%Y-%m-%d %H:%M:%S'))
# 暂停一秒
# time.sleep(1)
# print (time.strftime('%Y-%m-%d %H:%M:%S'))


# 12.........................................................
# 判断101-200之间有多少个素数，并输出所有素数。
# L = []
# for i in range(101, 201):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         L.append(i)
# print(L)


# .........................................
# 99 乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(j,i,j*i),end=" ")
#     print()


# 13...............................................
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# L = []
# for n in range(100,1000):
#     i = int(n / 100)
#     j = int(n / 10 % 10)
#     k = int(n % 10)
#     if n == i ** 3 + j ** 3 + k ** 3:
#         L.append(n)
# print("水仙花数有",L,"   个数为",len(L))


# 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
# 翻转字符串
# def reverseWords(input):
     
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")
#     inputWords=inputWords[-1::-1]

#     # 重新组合字符串
#     output = ' '.join(inputWords)
     
#     return output

# input = "i love you"
# rw = reverseWords(input)
# print(rw)

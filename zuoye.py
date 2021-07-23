'''
作业：
1、请用python打印出99乘法表。
2、有这么一个数组,[34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56],请以100为分界线，讲小于等于100的放到一个新数组中，将大于100的放到另一个新数组中。
3、重新自己实现一遍，我们课堂上讲的【发红包】功能。
4、输入某年某月某日，判断这一天是这一年的第几天？
5、有一个5 位数的任意数字，请将数字的顺序颠倒。（不是长的像数字的字符串哦）


for i in range(1,10):
    for j in range(1,i+1):
        print("{}X{}={}".format(i,j,i*j),end = "  ")
    print()


hlist = [34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56]
lowlist = []
highlist = []
for i in hlist:
    if i > 100:
        highlist.append(i)
    else:
        lowlist.append(i)
print(lowlist,highlist)
'''
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入号数："))
monthlist = [31,28,31,30,31,30,31,31,30,31,30,31]
days = 0
if (year%4 == 0 and year%100 != 0) or (year%100 == 0 and year%400 == 0):
    monthlist[1] = 29
    for i in range(month-1):
        days = days + monthlist[i]
else:
    for i in range(month-1):
        days = days + monthlist[i]
days = days + day
print("{}年{}月{}日是今年的第{}天！".format(year,month,day,days))

'''
xx = 86765465
xx = list(str(xx))
newxx = []
for i in range(len(xx)):
    x = xx.pop(-1)
    newxx.append(x)
newx = ""
for i in newxx:
    newx = newx + i
xx = int(newx)
print(xx)
'''




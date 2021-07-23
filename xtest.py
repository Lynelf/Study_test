'''
a = int(input("输入a："))
b = float(input("输入b："))
c = input("输入c：")

print("a类型为：",type(a))
print("b类型为：",type(b))
print("c类型为：",type(c))
d = "{0}{1}{2}".format(a,c,b)
print(d)

xx = input("请输入：")
print(bool(type(xx) == str))

a = ["啦啦","哈哈","嘻嘻","yaya","一一"]
for i in range(0,5,2):
    print(a[i])



a = (1,2,"lali",5)
b = [1,2,"lali",5,2,2,2,"haha","嘻嘻"]
b.append(3)
b.insert(2,222)
print(b)
print(b.index(2))
print(b[3])
print(b[1:5])
print(b[-3:-1])
print(b.pop(1))
print(b)


c = {"name":"大大","age":"22","sex":"男"}
print(c["name"])
print(c.get("11"))
c["name"] = "姓名"
c["name123"] = "123xingm"
print(c)


score = int(input("请输入分数："))
if score < 60:
    print("不及格")
elif score < 75:
    print("及格")
elif score < 85:
    print("良")
else:
    print("优秀")


c = {"name":"大大","age":"22","sex":"男"}
for i in c:
    print(i,c[i])
'''

'''
0、打印99乘法表
1、判断今天是今年的第几天。
2、通过代码来模拟一个红绿灯的过程，其中红灯输出30次，绿灯输出35次，黄灯输出3次。
3、模拟一个用户登录和用户注册的程序。其中账号密码都存到字典中。


# 0、打印99乘法表
for i in range (1,10):
    for j in range (1,i + 1):
        print(j,"*",i,"=",i*j,end="  ")
    print()


# 1、判断今天是今年的第几天。
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入号数："))
ping = [31,28,31,30,31,30,31,31,30,31,30]
rin = [31,29,31,30,31,30,31,31,30,31,30]
days = 0
if (year%400 == 0) or (year%100 != 0 and year % 4 == 0):
    for i in range(month - 1):
        days = rin[i] + day
else:
    for i in range(month - 1):
        days = ping[i] + day
print("{}月{}日是{}年的第{}天".format(month,day,year,days))
'''

# 2、通过代码来模拟一个红绿灯的过程，其中红灯输出30次，绿灯输出35次，黄灯输出3次。

'''
for i in range(30):
    print("红灯")
for j in range(35):
    print("绿灯")
for k in range(5):
    print("黄灯")
        i = 1


import time
light = {"红灯":30,"绿灯":35,"黄灯":3}
for i in light:
    for j in range(light[i]):
        print("{}距离结束时间{}秒".format(i,light[i]-j))
        time.sleep(1)




# 3、模拟一个用户登录和用户注册的程序。其中账号密码都存到字典中。
xx = {"张三":"123456a","李四":"123456b"}
a = input("请输入注册的用户名：")
b = input("请输入注册的密码：")
xx[a] = b
print("注册成功，可以登录啦")
usr = input("请输入登录用户名：")
psd = input("请输入登录密码：")
if xx.get(usr) == psd:
    print("登录成功")
else:
    print("登录失败")
print(xx)


import pymysql

def query(sql):

    db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")
    cursor = db.cursor()  #获取游标
    cursor.execute(sql)  #执行sql语句
    res = cursor.fetchall()  #获取所有结果
    for i in res:
        print(i)
    db.commit()   #应用提交
    db.close()   #关闭数据库连接

query("insert t_studnet set ")


db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")
cursor = db.cursor()
cursor.execute("select * from t_student;")
db.commit()   #应用提交
db.close()   #关闭数据库连接
'''

#-------------------------------------------------------------------

import pymysql

def chaxun(sql):
    '''
    这是数据库的查询方法
    '''
    db = pymysql.connect(host="122.51.194.146",user="root",password="123456",db="testdb")
    cursor = db.cursor()  # 获取游标
    try:
        cursor.execute(sql)  # 执行SQL
        res = cursor.fetchall()  # 获取所有结果
        db.close()  # 关闭数据库连接
        return res
    except Exception as e:
        print("你的SQL语句写错啦",e)


print(chaxun("show tables;"))



# query("select * from t_class;")
# query("select * from t_student;")
# query("show tables;","ljtestdb")
# query("desc t_class;")

def gaibian(sql):
    '''
    数据库的修改，新增，删除的方法
    '''
    db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()  # 应用/提交
    db.close()



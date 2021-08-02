from typing import AsyncGenerator


class Work:
    '''
    写了一个类
    '''
    def __init__(self,worker,year):
        self.worker = worker
        self.address = "天府三街"
        self.pay = 5000
        self.year = year

    def project1(self,x):
        print("在{}工作了{}年时间".format(self.address,self.year))
        print("这是我传入的变量:",x)

# work = Work(23,1) #类的实例化
# work.project1(343)

# # 类的继承
# class newWork(Work):
#     pass
# newwork = newWork(67,2)
# newwork.project1(45)

# 类的重写
class Cwork(Work):
    def project1(self, x):
        print("传入",x)
Cwork = Cwork(67,2)
Cwork.project1(3)


# # 写一写------------------------------------
# class Actor:
#     def __init__(self,age,movies) :
#         self.age = age
#         self.movies = movies

#     def act(self):
#         print("年龄为{}岁的演员已经演了{}部电影了。".format(self.age,self.movies))

# actor = Actor(29,10)
# actor.act()
# class A2(Actor):
#     def act(self):
#         print("gaixiele")

# a2 = A2(23,4)
# a2.act()
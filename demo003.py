import pymysql


class Db:
    '''
    这是一个用来操作数据库的类
    '''
    def __init__(self,host11,username11,password11,db11):  # 用来接受一些下面的方法会用到的公共参数
        self.host = host11
        self.user = username11
        self.password = password11
        self.db = db11

    def chaxun(self,sql):
        '''
        这是数据库的查询方法
        '''
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cursor = db.cursor()  # 获取游标
        try:
            cursor.execute(sql)  # 执行SQL
            res = cursor.fetchall()  # 获取所有结果
            db.close()  # 关闭数据库连接
            return res
        except Exception as e:
            print("你的SQL语句写错了！",e)

    def gaibian(self,sql):
        '''
        数据库的修改，新增，删除的方法
        '''
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()  # 应用/提交
            db.close()
            return True
        except Exception as e:
            print(e)
            return False

# host="192.144.148.91",user="root",password="1qaz!QAZ",db="testdb"

# db = Db("192.144.148.91","root","1qaz!QAZ","testdb")  # 类的实例化
# b = db.gaibian("update t_class set cname = '哈哈哈' where id = 4;")  #使用类下面的方法
# print(b)
# a = db.chaxun("select * from t_class;")
# print(a)
# print(db.host)

# 类的继承
# class Hahaha(Db):
#     pass

# hah = Hahaha("192.144.148.91","root","1qaz!QAZ","testdb")
# a = hah.chaxun()
# print(a)


# 类的重写
# class Hehehe(Db):
#     def chaxun(self):
#         print("这不是原来的查询了")

# hehe = Hehehe("192.144.148.91","root","1qaz!QAZ","testdb")
# hehe.chaxun()
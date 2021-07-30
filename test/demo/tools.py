import pymysql

def query(sql):
    '''
    这是数据库的查询方法。
    '''
    db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb") #连接并选择数据库
    cursor = db.cursor() #获取游标
    cursor.execute(sql) #执行sql语句
    res = cursor.fetchall() #获取查询结果
    db.close() #关闭数据库
    return res #返回结果

xx = query("select * from s_student;")
print(xx)
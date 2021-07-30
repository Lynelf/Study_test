import pymysql
from pymysql import cursors

def query(sql):
    '''
    这是数据库的查询方法
    '''
    db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="db_morning")
    cursor = db.cursor()  #获取游标
    try:
        cursor.execute(sql)  #执行sql
        res  = cursor.fetchall()  #获取所有结果
        db.close()
        return(res)
    except:
        print("sql语句写错了")


def gaibian(sql):
    '''
    数据库的修改、删除、新增的方法
    '''
    db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="test")
    cursors = db.cursor()
    cursors.execute(sql)
    db.commit() #应用/提交
    db.close()